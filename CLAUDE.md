# UFABC 2026.2 — Central de Estudos do Enzo

Este projeto é o **antro central** de todo o conteúdo do quadrimestre 2026.2.
Serve para: (1) gerar guias de estudo, (2) ser a principal fonte de estudo,
(3) lembrar prazos e (4) ser de onde a informação é extraída.

## Aluno
- **Enzo Pastore** — Bacharelado em Ciência e Tecnologia (BC&T), UFABC, Campus Santo André, turno **noturno**.

## Calendário do quadrimestre 2026.2 (fonte: Prograd UFABC)
- **Início das aulas:** 25/05/2026
- **Reajuste de matrículas:** 03–04/06/2026
- **Fim do trancamento sem justificativa:** 05/07/2026
- **Conclusão do quadrimestre:** 24/08/2026
- **Lançamento de conceitos:** 24/08–01/09/2026
- **Revisão de conceito (2026.2):** 15–22/09/2026
- **Avaliação das disciplinas:** 28/09–02/10/2026
- **Recuperação — lançamento de conceitos:** 05–11/10/2026

> Datas de provas, entregas e listas de cada matéria saem do **plano de ensino**
> de cada disciplina e devem ser preenchidas no `CLAUDE.md` da respectiva pasta.

### Mapa de provas 2026.2 (consolidado dos planos de ensino)
| Data | Matéria | Avaliação |
|---|---|---|
| 29/06 (seg) | Matemática Discreta II | Prova 1 (Sem. 1–4) |
| 03/07 (sex) | EDO | Prova 1 _(remarcada de 30/06)_ |
| 07/08 (sex) | EDO | Prova 2 |
| 14/08 (sex) | Práticas de Ensino de Química I | Prova escrita individual |
| **17/08 (seg)** | **Matemática Discreta II** | **Prova 2 (Sem. 5–11)** — _remarcada de 10/08_ |
| **25/09 (sex)** | **EDO (IEDO)** | **🚨 Exame de Recuperação (REC)** — _19h; sala a confirmar_ |

> 📌 Ao remarcar uma prova, a data está **em vários lugares dentro dos guias já gerados**
> (cabeçalho, plano de estudo, "véspera", rodapé) — não só no `CLAUDE.md` e no painel.
> Em 14/08/2026 o `guia-p2-completo.html` ainda mostrava 10/08 em 3 pontos. Varrer com
> `grep` a data antiga em `guias/*.html` sempre que uma data mudar.

> 📌 **Lista nova perto da prova é sinal de ESCOPO, não dever de casa.** Em 15/08/2026 a Lista 7 de
> Discreta (método da alteração) contradizia o escopo registrado — o guia dizia, em 3 lugares, que
> §5.4–5.7 "não cai". Ao receber material novo, **checar se ele contradiz o escopo do `CLAUDE.md`
> antes de gerar conteúdo**, e confirmar com o Enzo. O mesmo `grep` da nota acima vale para frases
> de escopo ("não cai", "fora do escopo", "provavelmente"), que também se espalham pelos guias.

Substitutivas/REC: EDO SUB 11/08, ~~REC 18/08~~ → **REC de EDO remarcada para 25/09** (confirmado com o
Enzo em 22/08/2026 — ele ficou de REC em IEDO) · Discreta SUB 12/08, REC 19/08 · Química REC 19–21/08.

> 🚨 **REC de IEDO em 25/09/2026** — plano de revisão de 5 semanas em
> `Disciplinas/BCN0405 - EDO/guias/plano-rec-iedo.html` (13 guias curtos + 2 simulados, agendado no
> Google Calendar). Formato acordado com o Enzo para **todo** guia da REC:
> **teoria enxuta → exemplos resolvidos passo a passo → só então exercícios do mesmo assunto**
> (recomendados do professor + 2–3 inéditos). Escopo: **P1 + P2**. **NF = 3,0 → precisa de REC ≥ 6,0**;
> o plano mira **7,0** para ter margem. Guias 1 e 2 prontos em 22/08.
ESMA001 (projeto): entregas por aula (Relatório Final ≈13/08) — **datas exatas a confirmar**.

> ⚠️ **Práticas de Química** proíbe uso de IA em atividades avaliadas — guias só para estudo, nunca para produzir entregas.
> **Professores:** EDO=Edson A. Arrázola · Discreta II=Renzo G. Gómez Diaz · ESMA001=Humberto de Paiva Jr. · Química=Rafaela Valero.

## Disciplinas (4)
| Sigla | Nome | Pasta |
|---|---|---|
| BCN0405-15 | Introdução às Equações Diferenciais Ordinárias | `Disciplinas/BCN0405 - EDO` |
| ESMA001-23 | Soluções para Desafios em Engenharia | `Disciplinas/ESMA001 - Solucoes Desafios Eng` |
| NHLQ002-22 | Práticas de Ensino de Química I | `Disciplinas/NHLQ002 - Praticas Ensino Quimica I` |
| MCCC010-23 | Matemática Discreta II | `Disciplinas/MCCC010 - Matematica Discreta II` |

> Matérias **trancadas em 29/06/2026:** Modelagem e Controle (ESTA020) e Métodos Experimentais (ESTO017) — removidas do quadrimestre.
> ✅ **Eventos do Google Calendar dessas duas matérias foram apagados em 01/08/2026** (série recorrente
> de aulas do ESTO017 + lembrete "Revisar Métodos Experimentais"). ESTA020 já não tinha eventos.
> Ao trancar/alterar matérias, lembrar de limpar **também** o Calendar, não só o CLAUDE.md.

## Grade de horários (noturno, Santo André)
| Dia | 19:00–21:00 | 21:00–23:00 |
|---|---|---|
| Segunda | Matemática Discreta II | — |
| Terça | — | EDO |
| Quarta | Práticas Ens. Química I *(quinzenal I)* | Matemática Discreta II |
| Quinta | Soluções p/ Desafios em Eng. | — |
| Sexta | EDO | Práticas Ens. Química I |

## Organização de cada disciplina
Cada pasta em `Disciplinas/` tem:
- `CLAUDE.md` — ficha da matéria (ementa, datas, professor, progresso)
- `material/` — PDFs brutos (slides, ementa, plano de ensino, provas antigas)
- `guias/` — guias de estudo em **HTML interativo** gerados aqui
- `listas/` — listas de exercícios e suas resoluções

## Convenções de trabalho
- Guias de estudo são gerados em **HTML interativo** (não Markdown/PDF), salvos em `guias/`.
- Sempre que um plano de ensino for adicionado em `material/`, extrair datas-chave e
  atualizar o `CLAUDE.md` da matéria **e** o `_dashboard/index.html`.
- Lembrete **semanal** automático: panorama de prazos, provas próximas e prioridades.
- O painel central é `_dashboard/index.html` (abrir no navegador).

### Fórmulas matemáticas nos guias HTML — padrão (decidido em 29/06/2026)
- **Padrão do projeto: MathJax 3 (saída `tex-svg`) via CDN jsDelivr.** É o que todos os guias
  de EDO/Discreta já usam — manter consistente. Sempre usar este bloco no `<head>`:
  ```html
  <script>MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']]},svg:{fontCache:'global'}};</script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
  ```
- **Delimitadores:** inline com `\( ... \)`, display com `\[ ... \]`. Em LaTeX dentro do HTML,
  escapar a barra (`\\(`, `\\frac`) só na config JS; no corpo do texto basta `\(` normal.
- 🐞 **Armadilha de CSS (achada em 05/08/2026, guia da P2 de Discreta) — nunca estilizar `figure svg`.**
  O seletor pega **também** os SVGs de fórmula que o MathJax gera dentro da `<figcaption>`.
  Com `*{box-sizing:border-box}`, o `padding:8px` + borda do estilo de diagrama **zeravam a caixa**
  das fórmulas curtas (`\(G\)`, `\(M\)`, `\(\delta\)`) e, como `mjx-container>svg` é `overflow:visible`,
  o glifo vazava em **tamanho gigante (600–1000 px)** por cima do texto — a tela ficava coberta.
  ✅ Usar sempre **`figure > svg`** (filho direto) + a trava
  `figure mjx-container svg{max-width:none;background:none;border:0;padding:0}`.
- 📱 **Fórmula inline longa quebra o layout no celular.** SVG pré-renderizado não quebra linha:
  uma fórmula de ~50ex estoura a coluna (~45ex no celular) e empurra a **página inteira** para o lado.
  ✅ Marcar no build as inline com `width ≥ 30ex` com `class="wide"` e usar
  `mjx-container.wide{max-width:100%;overflow-x:auto}` + `mjx-container.wide>svg{max-width:100%;height:auto;min-width:260px}`
  (encolhe proporcionalmente até caber; só rola se ainda não couber). Não afeta o desktop.
- 🐞 **Armadilha nova (13/08/2026, caderno prático da P2) — `<table>` estoura a página no celular.**
  Uma célula com fórmula inline larga (SVG **não quebra linha**) estica a `<table>` além da coluna e
  empurra a **página inteira** para o lado — mesmo com todo o CSS de MathJax correto. O diagnóstico
  aponta para a `<table>`, não para o `mjx-container`.
  ✅ No build, embrulhar **toda** `<table>` num `<div class="tabwrap">` e usar
  `.tabwrap{max-width:100%;overflow-x:auto}` + `.tabwrap table{margin:0;min-width:100%}` —
  o scroll fica preso dentro da caixa.
- 🐞 **Armadilha nova (13/08/2026) — não redeclarar `counter-increment` ao herdar o tema.**
  O CSS do `guia-p2-completo.html` já traz `.passos` completo (`counter-reset` + `counter-increment`
  no `li` + bolinha no `::before`). Ao reaproveitar esse tema e redeclarar `.passos > li::before
  {counter-increment:passo}`, os dois somam e a numeração dos passos sai **2, 4, 6, 8**.
  ✅ Ao herdar o tema, **só acrescentar** o que falta; conferir com `grep counter theme.css` antes.
- 📱 **Piso de legibilidade das `.wide` (13/08/2026).** O `min-width:260px` do padrão deixa uma
  fórmula inline de ~55ex com **10 px de altura** a 390 px — ilegível. ✅ Subir para
  `mjx-container.wide>svg{min-width:300px}` **e** promover a display (`\[...\]`) toda inline com
  `width ≥ 45ex`: acima disso, encolher nunca fica bom, e display já rola sozinho.
- **Como conferir a visualização:** abrir o guia no Chromium headless (Playwright) em 390 / 768 / 1280 px e
  checar (a) `document.documentElement.scrollWidth == window.innerWidth` em cada largura e
  (b) para todo `mjx-container > svg`, a razão `rect.width/rect.height` bate com a do `viewBox` (±5%).
  Distorção nessa razão = alguma regra de CSS está vazando em cima do MathJax.
  ⚠️ **Usar o seletor de filho direto (`>`), não o descendente.** `mjx-container svg` pega também os
  `<svg>` **aninhados** que o MathJax cria para delimitadores esticáveis (parênteses grandes, chaves,
  somatórios), que são distorcidos **de propósito** — deram 33 falsos positivos em 13/08/2026.
  - 🐞 **Screenshot do Playwright sai em branco (15/08/2026).** Os guias têm `scroll-behavior:smooth`
    no CSS, então `scrollIntoView()` **anima** — num arquivo de 4 MB a rolagem não termina antes do
    `screenshot()` e a imagem sai só com a cor de fundo (parece bug de renderização, não é).
    ✅ `page.addStyleTag({content:'html,body,*{scroll-behavior:auto!important}'})` antes de rolar,
    e usar `locator.scrollIntoViewIfNeeded()`. Lembrar de abrir os `<details>` antes de medir.
  - ⚠️ **Não alarmar com "fórmula de altura < 11 px" na varredura geral.** A maioria são inline de
    um glifo só (`\(n\)`, `\(x\)`), que legitimamente têm caixa baixa. O piso de legibilidade de
    14 px só faz sentido medido em **`mjx-container.wide > svg`**.
- **Por que `tex-svg` (e não CHTML):** renderiza em **SVG** → nítido em qualquer zoom, imprime
  bem e **não depende de baixar fontes** (essencial para a releitura **offline via PWA** do site
  publicado). `fontCache:'global'` deixa rápido em páginas com muitas fórmulas.
- **Por que CDN e não copiar o JS local:** o build (`build-site.py`) + service worker já cacheiam
  o script no 1º acesso, então funciona offline depois — sem precisar versionar o MathJax no repo.
- **Alternativa (KaTeX):** mais rápida para páginas com pouca matemática, mas cobre menos LaTeX e
  exige renderização manual; **não usar** salvo necessidade específica. Manter MathJax como default.
- **Nunca** colar fórmula como imagem/PNG nem usar Unicode "na mão" para expressões — sempre LaTeX
  via MathJax, para ficar pesquisável, acessível e editável.
- ✅ **Atualização (27/07/2026) — receita definitiva de pré-render.** Usada no guia da P2 de Discreta
  (2 399 fórmulas, 0 erros). Node + `mathjax-full` (instalar em qualquer pasta, o require resolve):
  `liteAdaptor` + `TeX({packages: AllPackages})` + `SVG({fontCache:'global'})`, converter cada
  `\(…\)` (inline) e `\[…\]` (display) por regex e, **no fim, injetar UMA vez** o
  `svgOutput.fontCache.getCache()` dentro de um `<svg style="position:absolute;width:0;height:0">`
  logo após `<body>`.
  - **Use `fontCache:'global'`, nunca `'local'`.** O nº de nós no DOM é o mesmo, mas `'local'` duplica
    os `<path>` dos glifos em cada fórmula: o mesmo guia deu **7,5 MB** com `'local'` e **2,7 MB** com
    `'global'` (cache compartilhado de 89 KB).
  - Antes de converter: trocar `\mathbb{1}` por `\mathbf{1}` (MathJax só tem maiúsculas em `\mathbb`)
    e **tirar HTML de dentro do TeX** — `\tag*{<span class="qed"></span>}` quebra; extrair o span e
    concatenar depois do SVG. Des-escapar `&lt;`/`&gt;`/`&amp;` dentro do TeX.
  - No corpo do texto, preferir `\lt`/`\gt` a `<`/`>` para o parser de HTML não engasgar.
  - Escrever o guia em **fragmentos** numerados e concatenar num `build.js` — arquivo único de 200 KB+
    é frágil de escrever e impossível de revisar.
- 🐞 **Armadilha nova (22/08/2026, guias 1–2 da REC) — `mjx-container` pré-renderizado nasce `display:inline`.**
  Sem a folha de estilo do MathJax (que não é carregada quando se pré-renderiza), `<mjx-container>` é um
  **elemento desconhecido** para o CSS → `display:inline` → **`max-width` e `overflow-x` simplesmente não se
  aplicam**. Resultado no guia 1: `scrollWidth` de **719 px** num viewport de 390 px, com 834 elementos
  estourando — e nenhuma regra de `.wide`/`tabwrap` adiantava, porque o problema era o display.
  ✅ Declarar o display explicitamente **antes** de qualquer outra regra de MathJax:
  ```css
  mjx-container{display:inline-block;max-width:100%;vertical-align:-0.25ex;font-size:1.06em}
  mjx-container>svg{max-width:100%;height:auto}          /* height:auto preserva a razão do viewBox */
  mjx-container[display="true"]{display:block;max-width:100%;overflow-x:auto;overflow-y:hidden}
  mjx-container[display="true"]>svg{max-width:none}      /* display rola em vez de encolher */
  mjx-container.wide{overflow-x:auto}
  mjx-container.wide>svg{min-width:300px}
  ```
  O `font-size:1.06em` compensa o x-height da fonte sans do tema — sem ele a fórmula fica visivelmente
  menor que o texto ao redor (o `ex` do SVG resolve contra a fonte do pai).
- 🐞 **Armadilha nova (22/08/2026) — LaTeX dentro de string JavaScript não sobrevive ao pré-render.**
  Quiz e flashcards escritos como array JS com `\\(...\\)` quebram de duas formas: (a) a regex do
  pré-render casa `\(` e deixa a primeira barra órfã, corrompendo o arquivo; (b) mesmo que passasse, não há
  MathJax em runtime para renderizar conteúdo inserido via `innerHTML`.
  ✅ Escrever quiz/flashcards como **HTML estático** no documento (gerado por um script Python no build) e
  deixar o JS só com a interação (virar cartão, marcar acerto). Fechar o build com um assert de que **não há
  `\(` dentro de nenhum `<script>`**.
- ⚠️ **Na varredura visual, não conte como falha o que está dentro de caixa que rola.** Elementos com
  `getBoundingClientRect().right > innerWidth` dentro de `.tabwrap` ou de `mjx-container` com
  `overflow-x:auto` são transbordo **proposital** e não empurram a página (deram 729 falsos positivos em
  22/08). ✅ Ignorar o elemento se algum ancestral tiver `overflow-x` diferente de `visible`; o veredito real
  é `document.documentElement.scrollWidth == window.innerWidth`.
- 🧰 **Pipeline dos guias da REC, versionado em `scripts/`** (22/08/2026): `build.py` (concatena os fragmentos
  numerados de uma pasta e injeta o `theme.css`), `render.js` (pré-render mathjax-full, `fontCache:'global'`,
  marca `.wide` ≥ 30ex e promove a display ≥ 45ex), `check.py` (todo `<use>` tem `<path>`) e `visual.py`
  (Chromium em 390/768/1280: estouro, razão do `viewBox`, piso de 14 px nas `.wide`, erros de console).
  Fluxo: escrever fragmentos → `build.py` → `render.js` → `check.py` → `visual.py`.
- ➕ **Como ACRESCENTAR conteúdo a um guia já pré-renderizado (15/08/2026).** Não precisa reconstruir
  o guia inteiro (nem recuperar o TeX com `svg2tex.py`): escreva só os **fragmentos novos** em LaTeX,
  pré-renderize à parte e injete por patch. Duas regras para o cache global não quebrar:
  - Ao renderizar, **compare os `id="MJX-…"` gerados com os que o guia já tem** e acrescente ao
    `<svg>` de cache existente **apenas os inéditos** (`<use xlink:href="#…">` de glifo ausente
    some **em silêncio** — nada de erro no build, a fórmula só fica com um buraco).
  - 🐞 **Rode todos os fragmentos numa ÚNICA chamada do renderer.** O cache global é acumulado por
    processo: rodar `render.js A B C` e depois `render.js D` faz a segunda rodada **sobrescrever** o
    arquivo de cache com os glifos só de `D`. Aconteceu em 15/08 — 17 glifos ficaram de fora e o
    patch aplicou "com sucesso" mesmo assim. O `check.py` (todo `<use>` tem `<path>`) pegou.
  - Fechar com um `patch.py` **idempotente** (aborta se o marcador da seção nova já existe) e que
    exija contagem exata de ocorrências em cada `replace` — assim o patch falha alto em vez de
    corromper o guia silenciosamente.
- 🔁 **Como recuperar o LaTeX de um guia já pré-renderizado (14/08/2026).** Pré-renderizar
  **destrói o TeX** — o arquivo publicado só tem SVG. Para reaproveitar conteúdo de um guia
  antigo (foi o caso do Guia Mestre da P2, que reorganiza exercícios dos guias anteriores),
  **não releia os PDFs**: o `mathjax-full` preserva a árvore MathML em `data-mml-node` e o
  codepoint de cada glifo em `data-c`, então dá para reconstruir o LaTeX andando na árvore.
  Script pronto em `scratchpad/svg2tex.py` (+ `extract.py`, que converte o guia inteiro em
  markdown com as fórmulas de volta em `\(…\)`). Recuperou **4 509 fórmulas dos 3 guias de
  Discreta com 0 falhas**. Duas armadilhas que custaram tempo:
  - 🐞 **Espaçar macro com regex genérica parte o nome no meio.** `\subseteqX` precisa virar
    `\subseteq X`, mas `re.sub(r"(\\[a-zA-Z]+)(?=[A-Za-z])", ...)` faz **backtracking**:
    em `\omega\le`, o casamento longo falha o lookahead, o regex recua para `\o` (omicron) e
    sai **`\o mega`** — que é LaTeX *válido* (`\o` = ø), então **renderiza errado em silêncio**,
    sem erro no build. ✅ Pegar a corrida inteira de letras e cortar no **prefixo conhecido
    mais longo**; e não mapear omicron como `\o` (é só a letra `o`).
  - 🐞 **`\binom` volta como `(\frac{a}{b})`.** No SVG, `\binom` é um `mfrac` **sem o `<rect>`**
    da barra, com parênteses como nós irmãos. ✅ Detectar a ausência do `<rect>` filho direto
    e colapsar o `mrow` `( mfrac-sem-barra )` num `\binom` só, senão os parênteses dobram.
- ⚠️ **Atualização (02/07/2026):** o `tex-svg.js` via CDN **falhou ao carregar** na máquina do Enzo
  (guia de véspera de EDO apareceu com LaTeX cru). Novo padrão preferido: **pré-renderizar** as
  fórmulas em SVG com `mathjax-full` (Node, `fontCache:'local'`) antes de entregar o guia — igual ao
  Guia 3 de EDO. Fica 100% offline, sem CDN. Escrever o guia com `\(`/`\[` normalmente e rodar o passo
  de pré-render no final (des-escapar `&lt;`→`<` dentro do TeX antes de converter).

## Deploy do GitHub Pages (dashboard público) — corrigido em 03/07/2026
- **Problema:** modo "Deploy from a branch" disparava um deployment do Pages a cada push
  na `main`, incluindo o commit-bot do `manifest.json` (segundos depois) → dois deployments
  corriam em paralelo, um cancelava o outro no meio → API do Pages retornava
  **"Deployment failed, try again later"** de forma intermitente. Foi o que deixou o painel
  publicado (`enzovarellap.github.io/ufabc-content`) desatualizado.
- **Correção:** novo workflow `.github/workflows/pages.yml`, deploy via **Actions**
  (`upload-pages-artifact` + `deploy-pages`), gera `manifest.json` direto no build (sem
  depender do commit automático) e usa `concurrency: cancel-in-progress: false` (deployments
  enfileiram, não brigam). `build-manifest.yml` continua existindo só para manter o
  `manifest.json` versionado atualizado (útil pra abrir `index.html` localmente).
- **⚠️ Passo manual pendente:** Settings → Pages → Source → trocar de "Deploy from a branch"
  para **"GitHub Actions"**. Sem isso o workflow novo não assume o deploy.

## Publicação dos guias (acesso web/celular) — decidido em 08/06/2026
- **Decisão:** publicar os guias como **site estático privado** (não recriar no Notion —
  perde MathJax/quizzes/tema). Notion fica só como segundo cérebro de anotações.
- **Host escolhido:** **Cloudflare Pages** (grátis) + **Cloudflare Access** com login por
  **código de uso único** liberado só para `enzovpastore@gmail.com` (privado de verdade, grátis).
- **Build:** `build-site.py` (na raiz) gera a pasta `publish/` = site pronto:
  `index.html` = o dashboard (caminhos `../Disciplinas/` → `Disciplinas/`); copia guias/listas
  (HTML) + materiais (PDF/DOCX); injeta **PWA** (manifest, ícones, service worker p/ releitura
  offline) em todas as páginas; gera `publish.zip` p/ upload. **Fontes não são alteradas** — só `publish/`.
- **Workflow ao criar guia novo:** rodar `python build-site.py` → na Cloudflare, projeto
  `estudos-ufabc` → novo deployment arrastando `publish.zip`. Login/proteção continuam valendo.
- ⚠️ **Ao adicionar link novo no `_dashboard/index.html`:** o `build-site.py` valida que **todo** link
  do painel tem arquivo correspondente em `publish/` e **aborta** se faltar. Ele só copia
  **HTML, PDF e DOCX** — linkar um `.txt` (ex.: `Exercicios Recomendados .txt`) quebra o build.
  Guardar esse tipo de conteúdo no `CLAUDE.md` da matéria, não como link do painel.
- 🐞 **Bug corrigido em 11/08/2026 no `build-site.py`.** O build abortava com
  "ESCRITA INCOMPLETA … (esperado N chars, lido N)" — com os **dois números iguais**, o que já
  denunciava que a mensagem estava errada. Causa real: `guia-edo-p1-vespera.html` tinha **3 bytes
  NUL (`\x00`) de padding** depois do `</html>` (lixo de sync do OneDrive). `str.rstrip()` sem
  argumento só tira *whitespace* e **não remove `\x00`**, então o teste `endswith("</html>")`
  falhava num arquivo íntegro, e o erro era atribuído a truncamento. ✅ Correção em duas frentes:
  (1) removidos os NULs do arquivo-fonte; (2) `write_html()` agora faz `rstrip("\x00").rstrip()` e
  **separa os dois diagnósticos** — tamanho diferente = escrita incompleta; tamanho igual mas sem
  `</html>` = HTML malformado (mensagem própria, mostrando o fim real do arquivo).
- Passo a passo completo em `COMO-PUBLICAR.md`. (Futuro opcional: automatizar com `wrangler`.)

## Perfil de estudo do Enzo (contexto que guia tudo)
- **Tempo:** ~5h/semana, concentradas nos **fins de semana**.
- **Disponibilidade real (do Google Calendar):** tem **compromissos de trabalho em horário comercial**
  nos dias úteis → ao agendar estudo, usar **fins de semana** ou **fim de tarde/noite antes das aulas**
  (as aulas ocupam 19–23h). Recorrentes fixos: bloco de estudo sáb 14–19h; psicóloga qua 15h.
- **Aulas:** em sua maioria **não serão aproveitadas por inteiro** → os guias são a
  **fonte principal de aprendizado** (ensinam do zero, não pressupõem a aula).
- **Meta:** **passar com tranquilidade** (não mira A) → calibrar ao essencial/cobrado.
- **Como aprende:** lendo resumo + fazendo exercícios + **ensinando (Feynman)**.
- **Prioridades:** **Matemática Discreta II** e **EDO** (as mais difíceis).
- **Foco do material:** resumos teóricos enxutos + listas resolvidas passo a passo + simulados.
- **Provas antigas:** não tem → buscar exemplos similares na web para montar simulados.
- **Apoio extra:** projeto da **ESMA001**.

## Ferramentas conectadas
- **Google Calendar** — aulas recorrentes, provas, prazos e **revisões espaçadas**.
  É também o único lugar de "tarefas" (Enzo não usa app de tarefas separado).
- **Notion** — segundo cérebro: resumos/anotações pesquisáveis.
- **Skills:** `university-study-guide` (guias HTML), `calculus-problem-set-solver`
  (listas EDO/Discreta), `pdf`/`pdf-viewer` (extrair planos/listas),
  `data:create-viz` (gráficos/regressão), `theme-factory`,
  `docx`/`pptx`/`xlsx`, `doc-coauthoring`.

## Workflows de IA (como o Claude deve trabalhar)
Baseados em evidência (active recall + repetição espaçada melhoram desempenho ~15–20%):
1. **Ingestão → guia:** PDF em `material/` → extrair com `pdf` → gerar guia HTML enxuto
   com `university-study-guide`. Atualizar CLAUDE.md da matéria + dashboard + (opcional) Notion.
2. **Loop Feynman:** todo guia tem bloco "explique com suas palavras"; o Claude faz o
   papel de aluno/corretor e aponta as lacunas.
3. **Recall + repetição espaçada:** quiz/flashcards no guia + criar no Google Calendar
   revisões em 1, 3 e 7 dias após cada tópico estudado.
4. **Listas:** resolver passo a passo com `calculus-problem-set-solver`, salvar em `listas/`.
5. **Simulados:** gerar prova-modelo cronometrada + gabarito a partir dos tópicos
   (buscar exemplos similares na web quando faltar prova antiga).
6. **Pacote de fim de semana:** a cada fim de semana, entregar um plano priorizado de ~5h
   (ordem do que estudar), começando por Discreta II e EDO conforme proximidade de provas.
7. **Projeto/relatórios:** apoiar ESMA001 (cronograma + entregas) com
   `doc-coauthoring` + `data:create-viz`.

> **Regra permanente:** sempre transcrever neste CLAUDE.md o contexto novo que surgir
> nas conversas (decisões, preferências, mudanças de escopo), para servir de steering file.
