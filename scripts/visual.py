#!/usr/bin/env python3
"""Confere layout e formulas no Chromium. Uso: visual.py guia.html"""
from playwright.sync_api import sync_playwright
import pathlib, sys, os
p = pathlib.Path(sys.argv[1]).resolve()
falhou = False
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    for w in (390, 768, 1280):
        errs = []
        pg = b.new_page(viewport={"width": w, "height": 900})
        pg.on("console", lambda m: errs.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(f"pageerror: {e}"))
        pg.goto(p.as_uri())
        pg.add_style_tag(content="html,body,*{scroll-behavior:auto!important}")
        pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
        pg.wait_for_timeout(500)
        r = pg.evaluate("""() => {
          const sw = document.documentElement.scrollWidth, iw = window.innerWidth;
          // razao largura/altura do <svg> filho direto vs a do viewBox
          let dist = [], baixas = [];
          document.querySelectorAll('mjx-container > svg').forEach(sv => {
            const rc = sv.getBoundingClientRect();
            const vb = (sv.getAttribute('viewBox')||'').split(/\\s+/).map(Number);
            if (rc.height < 1 || vb.length < 4 || !vb[2] || !vb[3]) return;
            const rr = rc.width/rc.height, rv = vb[2]/vb[3];
            if (Math.abs(rr-rv)/rv > 0.05) dist.push({tex:(sv.parentElement.getAttribute('aria-label')||'').slice(0,40), rr:+rr.toFixed(2), rv:+rv.toFixed(2)});
            if (sv.parentElement.classList.contains('wide') && rc.height < 14) baixas.push({h:+rc.height.toFixed(1)});
          });
          // elementos que estouram a largura do documento.
          // Ignora o que esta DENTRO de uma caixa que rola sozinha (.tabwrap, mjx-container
          // display/wide): ali o transbordo e proposital e nao empurra a pagina.
          const contido = el => {
            for (let n = el.parentElement; n && n !== document.body; n = n.parentElement) {
              const ox = getComputedStyle(n).overflowX;
              if (ox === 'auto' || ox === 'scroll' || ox === 'hidden') return true;
            }
            return false;
          };
          let estouro = [];
          document.querySelectorAll('body *').forEach(el => {
            const rc = el.getBoundingClientRect();
            if (rc.width > 0 && rc.right > iw + 1.5 && !contido(el))
              estouro.push(el.tagName + '.' + (el.className||'').toString().slice(0,28) + ' right=' + Math.round(rc.right));
          });
          return {sw, iw, nf: document.querySelectorAll('mjx-container').length, dist, baixas, estouro: estouro.slice(0,6), nEstouro: estouro.length};
        }""")
        ok_w = r["sw"] <= r["iw"]
        print(f"{w:>5}px scrollWidth={r['sw']} innerWidth={r['iw']} overflow={'NAO' if ok_w else 'SIM !!'}"
              f" formulas={r['nf']} distorcidas={len(r['dist'])} wide-baixas={len(r['baixas'])} elems-estourando={r['nEstouro']}")
        if r["dist"]: print("   distorcidas:", r["dist"][:5]); falhou = True
        if r["baixas"]: print("   .wide com altura < 14px:", r["baixas"][:5]); falhou = True
        if r["nEstouro"]: print("   estourando:", r["estouro"]); falhou = True
        if not ok_w: falhou = True
        if errs: print("   erros de console:", errs[:4]); falhou = True
        pg.close()
    b.close()
print("RESULTADO:", "FALHOU" if falhou else "OK — 0 estouro, 0 distorcao, 0 erro de console")
sys.exit(1 if falhou else 0)
