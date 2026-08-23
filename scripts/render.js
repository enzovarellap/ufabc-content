// Pre-render de formulas TeX -> SVG (mathjax-full, fontCache global).
// Uso: node render.js entrada.html saida.html
const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages});
const svgOut = new SVG({fontCache: 'global'});
const doc = mathjax.document('', {InputJax: tex, OutputJax: svgOut});

const IN = process.argv[2], OUT = process.argv[3];
let html = fs.readFileSync(IN, 'utf8');

let nInline = 0, nDisplay = 0, nWide = 0, nPromoted = 0;
const erros = [];

function unesc(t) {
  return t.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
}
function limpa(t) {
  return unesc(t).replace(/\\mathbb\{1\}/g, '\\mathbf{1}');
}
function largura(svg) {                    // largura em ex do <mjx-container>
  const m = svg.match(/width="([\d.]+)ex"/);
  return m ? parseFloat(m[1]) : 0;
}
function conv(t, display) {
  const node = doc.convert(limpa(t), {display: display});
  return adaptor.outerHTML(node);
}

// --- display: \[ ... \] ---
html = html.replace(/\\\[([\s\S]*?)\\\]/g, (m, t) => {
  try { nDisplay++; return conv(t, true); }
  catch (e) { erros.push('display: ' + t.slice(0, 60) + ' -> ' + e.message); return m; }
});

// --- inline: \( ... \) ---
html = html.replace(/\\\(([\s\S]*?)\\\)/g, (m, t) => {
  try {
    let out = conv(t, false);
    const w = largura(out);
    if (w >= 45) {                          // inline larga demais: vira display (rola sozinha)
      nPromoted++;
      out = conv(t, true);
    } else if (w >= 30) {                   // larga: encolhe ate caber
      nWide++;
      out = out.replace('<mjx-container', '<mjx-container class="wide"');
    }
    nInline++;
    return out;
  } catch (e) { erros.push('inline: ' + t.slice(0, 60) + ' -> ' + e.message); return m; }
});

// --- cache global de glifos: injetar UMA vez, logo apos <body> ---
const cache = adaptor.outerHTML(svgOut.fontCache.getCache());
if (!/<body[^>]*>/.test(html)) { console.error('ERRO: sem <body>'); process.exit(1); }
html = html.replace(/<body([^>]*)>/, (m, attrs) =>
  `<body${attrs}>\n<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">${cache}</svg>`);

fs.writeFileSync(OUT, html, 'utf8');
console.log(`${IN} -> ${OUT}`);
console.log(`  inline=${nInline} (wide=${nWide}, promovidas a display=${nPromoted}) display=${nDisplay}`);
console.log(`  cache de glifos: ${(cache.length/1024).toFixed(1)} KB`);
if (erros.length) { console.error('  ERROS DE TeX (' + erros.length + '):'); erros.forEach(e => console.error('   - ' + e)); process.exit(1); }
else console.log('  0 erros de TeX');
