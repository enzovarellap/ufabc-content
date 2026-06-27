#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-site.py — Monta a pasta `publish/` (site estático) a partir do projeto.

O que faz:
  1. Copia o dashboard (_dashboard/index.html) para publish/index.html,
     ajustando os caminhos ../Disciplinas/ -> Disciplinas/.
  2. Copia os guias/listas (HTML) e os materiais (PDF/DOCX) para publish/Disciplinas/.
  3. Injeta as tags de PWA (manifest, ícones, theme-color) e o registro do
     service worker em todas as páginas HTML.
  4. Gera manifest.webmanifest, sw.js, offline.html e os ícones.

Os arquivos-fonte NÃO são alterados — tudo é escrito apenas em publish/.

Uso:  python3 build-site.py      (rode de novo sempre que adicionar guias)
"""
import os, re, shutil, json, sys, zipfile, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(ROOT, "publish")
DISC = os.path.join(ROOT, "Disciplinas")

# Extensões que entram no site
COPY_EXT = (".html", ".pdf", ".docx", ".png", ".jpg", ".jpeg", ".svg", ".csv")

# --- Tags injetadas no <head> de cada página (caminhos absolutos = funcionam de qualquer subpasta)
HEAD_INJECT = """
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#0f1419">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Estudos UFABC">
<link rel="apple-touch-icon" href="/icon-180.png">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/icon-512.png">
"""

SW_REGISTER = """
<script>
if('serviceWorker' in navigator){
  addEventListener('load',function(){navigator.serviceWorker.register('/sw.js').catch(function(){});});
}
</script>
"""

# --------------------------------------------------------------------------- #
# Slug: nomes de pasta/arquivo viram ASCII limpo (sem espaço, sem acento,
# minúsculo). Hospedagem estática (Cloudflare etc.) erra com espaços/acentos
# em caminhos aninhados, então publicamos tudo "slugificado".
def slug_part(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = re.sub(r"[^a-z0-9._-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-._") or "x"
    return s


def slug_name(filename: str) -> str:
    base, ext = os.path.splitext(filename)
    return slug_part(base) + ext.lower()


def slug_relpath(relpath: str) -> str:
    """Slugifica cada componente; o último (com extensão) preserva a extensão."""
    parts = relpath.replace("\\", "/").split("/")
    out = []
    for i, p in enumerate(parts):
        if i == 0 and p == "Disciplinas":
            out.append("Disciplinas")   # mantém a caixa do topo (no Windows "disciplinas"
                                        # colidiria com a pasta "Disciplinas" já existente)
        elif i == len(parts) - 1 and "." in p:
            out.append(slug_name(p))
        else:
            out.append(slug_part(p))
    return "/".join(out)


def slugify_dashboard_paths(html: str) -> str:
    """Reescreve os caminhos do painel para casar com os arquivos slugificados."""
    def repl_dir(m):
        return "'" + slug_relpath("Disciplinas/" + m.group(1)) + "'"
    html = re.sub(r"'\.\./Disciplinas/([^']+)'", repl_dir, html)

    def repl_file(m):
        folder, fname = m.group(1), m.group(2)
        return "'" + slug_part(folder) + "/" + slug_name(fname) + "'"
    html = re.sub(r"'(guias|listas|material)/([^']+)'", repl_file, html)
    return html


def write_html(path: str, content: str) -> None:
    """Escreve HTML e re-lê pra garantir que não truncou (OneDrive às vezes corta a escrita)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if len(back) != len(content) or not back.rstrip().endswith("</html>"):
        raise RuntimeError(
            "ESCRITA INCOMPLETA em %s (esperado %d chars, lido %d). "
            "Provável lock/sync do OneDrive — feche o arquivo no OneDrive e rode o build de novo."
            % (path, len(content), len(back))
        )


def inject(html: str) -> str:
    if "manifest.webmanifest" not in html:
        if "</head>" in html:
            html = html.replace("</head>", HEAD_INJECT + "</head>", 1)
        else:
            html = HEAD_INJECT + html
    if "serviceWorker" not in html:
        if "</body>" in html:
            i = html.rfind("</body>")
            html = html[:i] + SW_REGISTER + html[i:]
        else:
            html = html + SW_REGISTER
    return html

def main():
    if os.path.isdir(OUT):
        # ignore_errors: alguns ambientes (ex.: OneDrive) podem travar a exclusão de
        # arquivos sincronizados; os arquivos são reescritos em seguida de qualquer forma.
        shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)

    # 1) index.html  (a partir do dashboard)
    with open(os.path.join(ROOT, "_dashboard", "index.html"), encoding="utf-8") as f:
        idx = f.read()
    idx = slugify_dashboard_paths(idx)
    idx = inject(idx)
    write_html(os.path.join(OUT, "index.html"), idx)

    # 2) Disciplinas (guias, listas, materiais) — pula CLAUDE.md e arquivos internos
    copied = {"html": 0, "pdf": 0, "outros": 0}
    for dirpath, _dirs, files in os.walk(DISC):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext not in COPY_EXT:
                continue
            src = os.path.join(dirpath, name)
            rel = os.path.relpath(src, ROOT)            # ex: Disciplinas/BCN0405 - EDO/guias/x.html
            slug_rel = slug_relpath(rel)                # ex: disciplinas/bcn0405-edo/guias/x.html
            dst = os.path.join(OUT, *slug_rel.split("/"))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if ext == ".html":
                with open(src, encoding="utf-8") as f:
                    h = f.read()
                write_html(dst, inject(h))
                copied["html"] += 1
            else:
                shutil.copy2(src, dst)
                copied["pdf" if ext == ".pdf" else "outros"] += 1

    # 3) manifest
    manifest = {
        "name": "UFABC 2026.2 — Central de Estudos",
        "short_name": "Estudos UFABC",
        "description": "Guias de estudo interativos do Enzo — UFABC 2026.2",
        "start_url": "/index.html",
        "scope": "/",
        "display": "standalone",
        "orientation": "portrait-primary",
        "background_color": "#0f1419",
        "theme_color": "#0f1419",
        "lang": "pt-BR",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    with open(os.path.join(OUT, "manifest.webmanifest"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # 4) service worker
    with open(os.path.join(OUT, "sw.js"), "w", encoding="utf-8") as f:
        f.write(SW_JS)

    # 5) offline fallback
    with open(os.path.join(OUT, "offline.html"), "w", encoding="utf-8") as f:
        f.write(OFFLINE_HTML)

    # 6) ícones (opcional — requer Pillow; se faltar, segue sem ícones)
    try:
        make_icons(OUT)
    except Exception as e:
        print("AVISO: icones nao gerados (%s). O site funciona normalmente." % e)

    # 6.5) verificação de links: todo href do painel aponta para um arquivo existente?
    missing = []
    for block in re.split(r"\{code:", idx)[1:]:
        mdir = re.search(r"dir:'([^']+)'", block)
        if not mdir:
            continue
        d = mdir.group(1)
        for folder, fname in re.findall(r"'(guias|listas|material)/([^']+)'", block):
            href = d + "/" + folder + "/" + fname
            if not os.path.exists(os.path.join(OUT, *href.split("/"))):
                missing.append(href)
    if missing:
        raise RuntimeError("Links do painel sem arquivo correspondente:\n  " + "\n  ".join(missing))

    # 7) publish.zip (para upload por arrastar-e-soltar na Cloudflare)
    zip_path = os.path.join(ROOT, "publish.zip")
    if os.path.exists(zip_path):
        try:
            os.remove(zip_path)
        except OSError:
            pass
    nzip = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _d, fs in os.walk(OUT):
            for fn in fs:
                full = os.path.join(dp, fn)
                z.write(full, os.path.relpath(full, OUT))
                nzip += 1
    # verificação: o zip abre e tem o index na raiz?
    with zipfile.ZipFile(zip_path) as z:
        assert z.testzip() is None, "publish.zip corrompido"
        assert "index.html" in z.namelist(), "index.html não está na raiz do zip"

    print("OK -> publish/  +  publish.zip")
    print("  HTML  :", copied["html"])
    print("  PDF   :", copied["pdf"])
    print("  outros:", copied["outros"])
    print("  no zip:", nzip, "arquivos")


# --------------------------------------------------------------------------- #
SW_JS = r"""/* UFABC 2026.2 — service worker (releitura offline) */
const VERSION = 'v1';
const CORE = 'core-' + VERSION;
const RUNTIME = 'runtime-' + VERSION;
const PRECACHE = ['/','/index.html','/manifest.webmanifest','/offline.html','/icon-192.png','/icon-512.png'];

self.addEventListener('install', (e) => {
  self.skipWaiting();
  e.waitUntil(caches.open(CORE).then((c) => c.addAll(PRECACHE).catch(() => {})));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k !== CORE && k !== RUNTIME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  let url;
  try { url = new URL(req.url); } catch (_) { return; }
  if (url.pathname.startsWith('/cdn-cgi/')) return;          // não tocar no login do Cloudflare Access

  // Navegação: rede primeiro, cai pro cache, cai pra offline.html
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).then((r) => { const cp = r.clone(); caches.open(RUNTIME).then((c) => c.put(req, cp)); return r; })
                .catch(() => caches.match(req).then((r) => r || caches.match('/offline.html')))
    );
    return;
  }

  // Mesmo domínio: cache primeiro, atualiza em segundo plano
  if (url.origin === location.origin) {
    e.respondWith(
      caches.match(req).then((cached) => {
        const net = fetch(req).then((r) => { const cp = r.clone(); caches.open(RUNTIME).then((c) => c.put(req, cp)); return r; }).catch(() => cached);
        return cached || net;
      })
    );
    return;
  }

  // CDN (MathJax, Google Fonts): cache primeiro
  e.respondWith(
    caches.match(req).then((cached) => cached || fetch(req).then((r) => { const cp = r.clone(); caches.open(RUNTIME).then((c) => c.put(req, cp)); return r; }).catch(() => cached))
  );
});
"""

OFFLINE_HTML = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Offline — Estudos UFABC</title>
<style>
  body{font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;background:#0f1419;color:#e6edf3;
       display:flex;min-height:100vh;align-items:center;justify-content:center;margin:0;padding:24px;text-align:center}
  .box{max-width:420px}
  h1{font-size:1.3rem;margin:0 0 10px}
  p{color:#9bb0c0;line-height:1.6}
  a{color:#4da3ff;text-decoration:none;font-weight:600}
</style></head>
<body><div class="box">
  <h1>Você está offline</h1>
  <p>Os guias que você já abriu continuam disponíveis mesmo sem internet.
     Quando a conexão voltar, tudo volta ao normal.</p>
  <p><a href="/index.html">↻ Voltar ao painel</a></p>
</div></body></html>
"""


def make_icons(out_dir):
    from PIL import Image, ImageDraw, ImageFont
    def font(sz):
        for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
            if os.path.exists(p):
                return ImageFont.truetype(p, sz)
        return ImageFont.load_default()

    def grad(size, c1, c2):
        img = Image.new("RGB", (size, size), c1)
        top = Image.new("RGB", (size, size), c2)
        mask = Image.new("L", (size, size))
        md = mask.load()
        for y in range(size):
            v = int(255 * y / max(1, size - 1))
            for x in range(size):
                md[x, y] = v
        img.paste(top, (0, 0), mask)
        return img

    def draw_icon(size, pad_ratio=0.0):
        # fundo arredondado com leve gradiente
        bg = grad(size, (26, 32, 39), (15, 20, 25))   # #1a2027 -> #0f1419
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        r = int(size * 0.22)
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(15, 20, 25, 255))
        img.paste(bg, (0, 0))
        # re-aplica cantos arredondados via máscara
        mask = Image.new("L", (size, size), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=255)
        out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        out.paste(img, (0, 0), mask)
        d = ImageDraw.Draw(out)

        inset = int(size * pad_ratio)
        usable = size - 2 * inset
        # "UF" em destaque (degradê azul->verde aplicado por máscara de texto)
        f1 = font(int(usable * 0.42))
        txt = "UF"
        bbox = d.textbbox((0, 0), txt, font=f1)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        tx = (size - tw) / 2 - bbox[0]
        ty = inset + usable * 0.16 - bbox[1]
        # camada de texto colorida via gradiente
        tlayer = grad(size, (77, 163, 255), (126, 231, 135))  # #4da3ff -> #7ee787
        tmask = Image.new("L", (size, size), 0)
        ImageDraw.Draw(tmask).text((tx, ty), txt, font=f1, fill=255)
        out.paste(tlayer, (0, 0), tmask)
        d = ImageDraw.Draw(out)
        # "ABC" pequeno
        f2 = font(int(usable * 0.17))
        sub = "ABC"
        b2 = d.textbbox((0, 0), sub, font=f2)
        sw = b2[2] - b2[0]
        d.text(((size - sw) / 2 - b2[0], inset + usable * 0.60), sub, font=f2, fill=(155, 176, 192, 255))
        # "2026.2"
        f3 = font(int(usable * 0.12))
        yr = "2026.2"
        b3 = d.textbbox((0, 0), yr, font=f3)
        yw = b3[2] - b3[0]
        d.text(((size - yw) / 2 - b3[0], inset + usable * 0.78), yr, font=f3, fill=(126, 231, 135, 255))
        return out

    draw_icon(512).save(os.path.join(out_dir, "icon-512.png"))
    draw_icon(512).resize((192, 192), Image.LANCZOS).save(os.path.join(out_dir, "icon-192.png"))
    draw_icon(512).resize((180, 180), Image.LANCZOS).save(os.path.join(out_dir, "icon-180.png"))
    # maskable: conteúdo dentro da zona segura (padding ~14%)
    draw_icon(512, pad_ratio=0.14).save(os.path.join(out_dir, "icon-512-maskable.png"))
    # favicon
    draw_icon(512).resize((32, 32), Image.LANCZOS).save(os.path.join(out_dir, "favicon.png"))


if __name__ == "__main__":
    main()
