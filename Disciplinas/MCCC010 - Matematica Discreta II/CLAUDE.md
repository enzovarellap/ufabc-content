# MCCC010-23 — Matemática Discreta II

## Ficha
- **Sigla:** MCCC010-23
- **Turma:** A1 — Noturno
- **Campus:** Santo André
- **TPI:** 4 - 0 - 4 (Teórica 4 / Prática 0 / Individual 4)
- **Professor:** Renzo Gonzalo Gómez Diaz
- **Turma:** NA1 — Sala Auditório A-102-0 (Bloco A)
- **Horários:**
  - Segunda-feira, 19:00–21:00 (semanal)
  - Quarta-feira, 21:00–23:00 (semanal)

## Ementa / Tópicos
Foco em **teoria dos grafos** e **probabilidade discreta / método probabilístico**:
definições e conexidade, isomorfismo, bipartidos, árvores, vértices/arestas de corte,
k-conexidade; grafos eulerianos e hamiltonianos; emparelhamentos (Teorema de Berge,
bipartidos); coloração de arestas (Vizing) e vértices (Brooks); variáveis aleatórias
e esperança; desigualdades de Jensen, Markov, Chebyshev; modelo Erdős-Rényi; métodos
do primeiro/segundo momento, alteração e concentração.

## Datas-chave (do plano de ensino)
| Data | Avaliação / Entrega | Peso |
|---|---|---|
| **29/06/2026** (seg) | **Prova 1 (P1)** — Semanas 1–4 | 50% |
| **17/08/2026** (seg) | **Prova 2 (P2)** — Semanas 5–11 · ⚠️ **remarcada** (era 10/08) | 50% |
| 12/08/2026 (qua) | Prova Substitutiva (SUB) — data do plano original | — |
| 19/08/2026 (qua) | Prova de Recuperação (REC) | — |

> ⚠️ **P2 remarcada para 17/08/2026** (informado pelo Enzo em 13/08/2026). O plano de ensino
> original marcava 10/08 e 17/08 era "vista de provas". **Datas de SUB/REC e a vista provavelmente
> deslizaram junto — a confirmar com o professor.** Não houve aula de Discreta entre o aviso e a
> prova (a última foi qua 12/08), então a confirmação teve de ser por e-mail/turma.

## Critério de avaliação
Pré-REC = P1·0,5 + P2·0,5. Conceitos: A ≥ 8,5; B ≥ 7,0; C ≥ 6,0; D ≥ 5,0; F < 5,0.
REC para D/F: Pós-REC = Pré-REC·0,5 + REC·0,5 (conceito máx. C).

## Material em `material/`
- `plano-ensino-md2.pdf`, `intro.pdf`, `aula1.pdf`, `aula2.pdf`, `aula3.pdf`, `aula3.2.pdf`,
  `aula4e5.pdf`, `aula6e7.pdf`, `aula8e9.pdf`, `aula10.pdf`, `aula11.pdf`,
  `aula14.pdf`, `aula15.pdf`, `aula16.pdf`, `aula17.pdf`.
- ⚠️ **Não existem `aula12.pdf` nem `aula13.pdf`** — Enzo confirmou em 27/07/2026 que não os tem.
  Conteúdo provável (a confirmar): Teorema de Tutte / emparelhamentos em grafos gerais, ou
  números de Ramsey (o cap. 5 do livro cita "R(k) […] visto no Capítulo 4"). O guia da P2 tem um
  bloco `#lacuna` sinalizando isso — se os slides aparecerem, incorporar lá.
- Listas em `listas/`: `lista1-md2.pdf`, `lista2-md2.pdf`, `gabarito-lista3.pdf`,
  `lista4.pdf` (emparelhamentos + coloração de arestas, E1–E5),
  `lista5.pdf` (coloração por vértices, E1–E6), `lista-p1.pdf`,
  **`lista6.pdf`** (introdução ao método probabilístico e primeiro momento, E1–E5) e
  **`lista7.pdf`** (método da alteração, E1–E3) — as duas entregues em 15/08/2026 e
  **resolvidas por inteiro dentro do `guia-p2-mestre.html`** (PRO-10…14 e ALT-01…03).

### Conteúdo coberto até 27/07/2026 (escopo da P2 — confirmado pelo Enzo)
A P2 cobre **das aulas 8e9 até a 17**, ou seja:
- **Hamiltonianos** (aula8e9): c(G−S)≤|S|, Dirac, Ore, fecho de Bondy–Chvátal. *A P2 é cumulativa a partir daqui.*
- **Emparelhamentos** (aulas 10–11): maximal×máximo, caminho alternante/aumentante, **Berge**,
  **Hall** (+ versão com defeito), bipartidos k-regulares → k emparelhamentos perfeitos,
  cobertura por vértices, **König** (ν=τ), **SDR**.
- **Coloração de arestas** (aula14): χ′, χ′(Cₙ), χ′(Kₙ), χ′≥Δ, χ′≤2Δ−1, **Vizing**, Classe 1/2, bipartido ⟹ Classe 1.
- **Coloração de vértices** (aulas 15–16): χ, χ≥ω, χ·α≥n, e(G)≥C(χ,2), guloso, χ≤Δ+1,
  **Brooks**, **Nordhaus–Gaddum**.
- **Método probabilístico** (aula17 = cap. 5 do livro): **§5.1–5.5**
  (fundamentos, cota da união, prova probabilística — Erdős R(k)>2^{k/2}, hipergrafos, torneios —,
  esperança/linearidade/indicadoras, primeiro momento, Jensen; **+ §5.4 modelo G(n,p) e desigualdade
  de Markov e §5.5 método da alteração**). **§5.6 (Chebyshev) e §5.7 (Chernoff) NÃO caem.**

> ⚠️ **Escopo do cap. 5 mudou em 15/08/2026** (confirmado pelo Enzo). Até 14/08 o registro era
> "§5.4–5.7 inteiro fora do escopo"; o professor liberou a **Lista 7 — Método da alteração** dois
> dias antes da prova e o Enzo confirmou: **§5.4 e §5.5 caem, §5.6 e §5.7 não**. Lição: *lista nova
> perto da prova é sinal de escopo, não de dever de casa* — ao receber uma, checar se ela contradiz
> o escopo registrado **antes** de gerar material.

### Conteúdo coberto até 06/06/2026 (Semanas 1–4 → cai na P1)
Cap. 1 (conceitos básicos): grafo, grau, **aperto de mãos** (Σd=2|E|) e paridade;
isomorfismo, complemento e auto-complementar; passeios/trilhas/caminhos/ciclos (+ lema
passeio⟹caminho); subgrafos (induzido, gerador, remoção); conexidade e componentes;
δ(G)≥2 ⟹ caminho de comp. δ e ciclo ≥ δ+1; distância, diâmetro, **cintura** e
circunferência (g≤2·diam+1); **bipartidos** (⟺ sem ciclo ímpar); **Teorema de Mantel**
(⌊n²/4⌋) e subgrafo bipartido ≥|E|/2. Cap. 3: **árvores** (e=n−1, 4 caracterizações,
folhas, árvore geradora, ponte/vértice de corte). Clássicos: festa de 6 (R(3,3)≤6) e paridade.

## Guias gerados em `guias/`
- **`guias/quiz-emparelhamentos.html`** — **QUIZ interativo de Emparelhamentos** (gerado 16/08/2026,
  128 KB). Pedido pelo Enzo: quiz rápido pra treinar reconhecimento de tema + ordem de resolução,
  não teoria nova. Fonte: só exercícios oficiais da **Lista 4** (E1(a)(b), E1(c), E2, E3, E4) — sem
  inventar enunciado. 5 cards, cada um em duas etapas progressivas: (1) múltipla escolha da
  ferramenta certa (Diferença simétrica, único emp. perfeito em árvore, troca por caminho
  aumentante, coloração de arestas/emparelhamento por dia, 1-fatoração do Petersen), liberando
  (2) ordenar por clique os passos da resolução (chips movem entre "passos"/"sua ordem", "conferir"
  pinta certo/errado por posição). Cada card linka pro exercício correspondente no Guia Mestre
  (EMP-03, EMP-09, EMP-10, ARE-06, ARE-10) e tem um `<details>` com a resposta certa como fallback
  offline. Barra de placar fixa no topo (temas × passos).
  - Escopo por enquanto: **só Emparelhamentos** — Hamiltonianos/Coloração/Probabilístico ficam
    pra depois, se o formato validar.
  - ⚠️ **CDN do MathJax bloqueado no sandbox onde foi gerado** (jsDelivr nega no proxy do ambiente,
    403 de política — não deu pra confirmar se é só o sandbox ou reproduz na máquina do Enzo, mas já
    havia o precedente de 02/07 com o guia de véspera de EDO). Pré-renderizado com `mathjax-full`
    (mesma receita do guia mestre): **110 fórmulas, 0 erros**, cache de glifos de ~22 KB injetado uma
    vez após `<body>`. **Armadilha nova:** o `<script>` de config do MathJax no `<head>` guarda os
    delimitadores como `'\\('`/`'\\)'` (barra dupla, string JS) — um regex ingênuo de conversão que
    varre o arquivo inteiro casa a segunda barra desse literal com um `\(` de verdade e devora o
    arquivo a partir dali. Corrigido restringindo a conversão ao conteúdo **depois** de `<body>`
    (o `<head>` nunca é tocado) — vale para qualquer pré-render futuro que reaproveite esse bloco de
    config no `<head>`.
  - **Verificado** (Playwright headless, 390/768/1280 px): sem rolagem horizontal, 0 SVG com razão
    de aspecto distorcida, 0 sobra de LaTeX cru no texto visível, fluxo completo testado (clique na
    opção certa/errada libera os passos, ordenar corretamente pinta os 6 chips de verde, placar
    atualiza, `<details>` de resposta abre com a lista de fallback).
  - Linkado no `_dashboard/index.html`.
- **`guias/guia-p2-mestre.html`** — **GUIA MESTRE DA P2** (gerado 14/08/2026, **atualizado 15/08, 4,6 MB**).
  - 🆕 **Atualização de 15/08/2026** (Listas 6 e 7 + mudança de escopo). O arquivo já estava
    **pré-renderizado** (sem TeX no fonte) e os fragmentos de build da sessão anterior não estavam
    versionados, então o acréscimo foi feito **por patch**: fragmentos novos escritos em LaTeX,
    pré-renderizados à parte e injetados no HTML existente. Build em `scratchpad/mestre/`
    (`render.js` + 4 fragmentos + `patch.py` + `check.py` + `check.js`). **688 fórmulas novas,
    0 erros**; o cache global de glifos passou de 181 → **198** (só os 17 glifos inéditos foram
    acrescentados ao `<svg>` de cache já existente, sem duplicar id).
    - **Seção nova `#plano12` — "Plano de 12 h até a prova"**: roteiro hora a hora de sáb 15/08 a
      seg 17/08 (4h40 + 6h + 1h30), calibrado nas respostas do Enzo (inseguro nos 5 blocos, o que
      falta é **volume**). Checklist persistido em `localStorage` (mesma chave `md2-p2-mestre`;
      as caixas `.chk` são indexadas por `id`, então acrescentar não corrompe o estado salvo).
      Traz também uma **versão de 6 h** com o que cortar conscientemente.
    - **PRO-10…14 = Lista 6 inteira** (E1 K₄ mono ≤ C(n,4)2⁻⁵ · E3 corte balanceado mn/(2n−1) ·
      E4 sinais ±1 com |Σaᵢvᵢ| ≤ √n e ≥ √n · E2 jogo C×R · E5 α(G) ≥ Σ deg/(1+deg+deg₂)).
    - **Seção nova `#alt-ex` — "Bloco 6 · Método da alteração"**: §5.4 em 5 min (G(n,p), Markov,
      desigualdades de bolso), **esqueleto de 4 passos** (sorteie · conte defeitos · conserte ·
      conclua e otimize), tabela de gatilhos, **ALT-01…03 = Lista 7 inteira** e "erros que custam
      ponto". É o único bloco do guia que o Enzo **nunca estudou** — prioridade, não revisão.
    - Corrigidos os **3 pontos** que afirmavam o escopo antigo (caixa do topo, linha do G(n,p) no
      glossário, caixa "fora do escopo" do Bloco 5) e o kicker do bloco de coloração de vértices,
      que dizia "Bloco 5" igual ao do probabilístico (agora "Bloco 4").
    - **Verificado:** 198/198 glifos resolvem, 0 id duplicado, 276 âncoras internas + 317 links
      externos sem quebra, 63 `article.ex`, 0 LaTeX cru. Em 390/768/1280 px: sem rolagem
      horizontal, 0 SVG com razão distorcida (seletor de filho direto), toda `<table>` larga presa
      em `.tabwrap` e `.wide` com altura mínima de 14 px.
  Pedido pelo Enzo para **juntar as referências dos outros dois guias da P2**. Decisões dele:
  (a) **só reorganizar os exercícios existentes**, sem inventar nenhum; (b) **autocontido**
  (resolução inteira dentro do arquivo) **+ links** para a teoria; (c) cobrir os quatro
  formatos de "o que preciso saber"; (d) calibrar no que cai. Mesmo tema "Papel & Tinta".
  Tem duas partes:
  1. **"Tudo que você precisa saber"** — o núcleo do pedido:
     **glossário de 39 símbolos** em 5 tabelas (`Símbolo | Lê-se | O que é | Onde aparece`,
     com os 5 pares confundíveis marcados: ν×τ, α×ω, χ×χ′, δ×Δ, M×M*);
     **mapa de 30 resultados** (`Resultado | Enunciado | Gatilho no enunciado | Treinar em`);
     **checklist de domínio** com 33 itens × 3 caixas (enunciar/provar/aplicar, 99 caixas,
     persistido em `localStorage` na chave `md2-p2-mestre`); e **pré-requisitos da P1**
     (11 itens, cada um dizendo onde reaparece na P2).
  2. **63 exercícios reagrupados por conteúdo** (55 + 8 novos em 15/08), todos com resolução passo
     a passo e um bloco `ex-ref` de links para a teoria: HAM-01..06 (6), EMP-01..13 (13),
     ARE-01..12 (12), VER-01..15 (15), PRO-01..14 (14), **ALT-01..03 (3)**. Cada um traz a origem
     (Caderno Prático B*·E*, Lista 4/5/6/7 E*, Simulado Q*, Lista P1 E*) e o nível
     (aquecimento/prova/desafio).
     Cada bloco abre com tabela "gatilho no enunciado → ferramenta" e fecha com os erros
     que custam ponto daquele assunto.
  - Escrito por **6 agentes em paralelo** (um por bloco + um da seção de referência), a
    partir de fatias do conteúdo dos guias existentes. 3 588 fórmulas pré-renderizadas,
    0 erros, cache de glifos de 80 KB. **Verificado**: 18 350 links/âncoras conferidos
    (0 quebrados) e 390/768/1280 px sem scroll horizontal nem distorção de razão.
  - Build em `scratchpad/` (`build.js` + 8 fragmentos + `lint.py` de contrato +
    `links.py` de âncoras + `check.js` visual).
  - ⚠️ **Achados a conferir com o professor/monitor** (nenhum altera resultado; todos
    ficaram como `<p class="nota">` dentro do exercício):
    - **Gabarito do Simulado Q2(c) do guia completo diz "o único conjunto apertado é
      S={A,B,C}" — mas S={A,B,C,E} também é apertado.** Defeito 1 e máximo 4 continuam certos.
    - **B3·E3 do caderno prático afirma que o guloso dá a cor \(i\) a *todo* vértice de
      \(V_i\); a versão forte é falsa** (contraexemplo: aresta \(uv\) + isolado \(w\)). A prova
      só precisa de "cor ≤ \(i\)", que é como a Lista 5·E2 enuncia — as duas fontes divergem.
    - **Lista 5·E5 tem um buraco que o B3·E6 conserta:** pintar um circuito ímpar qualquer com
      3 cores novas só vale se ele não tiver cordas; escolher o de comprimento **mínimo** fecha.
    - **B4·E5 chama a propriedade de \(S_k\); a teoria (Teo. 5.2.3) chama de \(T_k\)** — mesmo objeto.
    - Duplicatas reais entre as fontes: B1·E8 ≡ Lista 4·E1(c); B2·E6 ≡ Lista 4·E4;
      B2·E8 ≡ Lista 4·E5. Mantidas as duas redações de cada, com nota explicando quando usar qual.
  - ⚠️ **Achados novos nas Listas 6 e 7 (15/08/2026)** — os três viraram nota dentro do exercício:
    - **Lista 7·E3 tem erro de digitação.** O parágrafo define o número de Ramsey assimétrico com
      **K₃ vermelho** (isto é, R(3,k)), mas o que se pede é **R(4,k) ≥ (ck/log k)²**. A alteração
      dá R(s,k) ≥ c(k/log k)^{s/2}, então o expoente 2 **só sai com s = 4** — resolvido como K₄.
      Com K₃ o método daria (k/log k)^{3/2}; a cota quadrática para R(3,k) é verdadeira, mas é
      Kim/Shearer, fora do alcance da alteração.
    - **Lista 6·E5 (α(G) ≥ Σ deg/(1+deg+deg₂), cintura ≥ 4): a construção natural tem um furo.**
      Sortear σ, tomar W = {v mínimo em B₂(v)} e S = ∪_{v∈W} N(v) dá a esperança certa, e dois
      centros ficam a distância ≥ 3 — o que garante que os N(v) são **disjuntos**, mas **não** que
      não há aresta entre eles. Contraexemplo: P₄ = v–u–b–v′ com σ = (v,v′,u,b) dá S = {u,b} com
      ub ∈ E. Independência exigiria distância ≥ 4. Conserto que registrei no guia: aceitar
      u ∈ N(v) só quando v for o centro σ-mínimo entre os centros a distância ≤ 2 de u (custa um
      pouco da esperança). **Confirmar com o professor qual fecho ele considera completo.**
    - **Lista 7·E1:** o `x = n − C(n,k)2^{1−C(k,2)}` do enunciado não é inteiro nem
      necessariamente positivo — ler como ⌈x⌉ / "existe T com |T| ≥ x"; a afirmação só tem
      conteúdo quando x ≥ 1, e é por isso que o passo de otimizar n existe.
- **`guias/guia-p2-pratico.html`** — **CADERNO PRÁTICO DA P2** (gerado 13/08/2026, 1,5 MB).
  Complemento *de treino* do guia completo, pedido pelo Enzo quando faltavam 4 dias para a prova
  remarcada. Mesmo tema "Papel & Tinta" (CSS reaproveitado do `guia-p2-completo.html`). **Não repete
  teoria** — tem três coisas:
  1. **Roteiro hora a hora** de qui 13/08 a seg 17/08, calibrado na agenda real (entrega do ESMA001
     na quinta, prova de Química na sexta, trabalho na segunda) → ~12h30 concentradas em sáb+dom+
     tarde de segunda. Checklist persistido em `localStorage` (chave `md2-p2-pratico`).
  2. **Ficha de decisão "qual teorema usar"** — triagem de 30 s (gatilho no enunciado → bloco),
     15 "rotas" (gatilho → ferramenta → esqueleto) cobrindo emparelhamentos, coloração de arestas,
     coloração de vértices e método probabilístico, + **5 esqueletos de demonstração** para escrever
     de memória na véspera (Berge, Hall, cota de contagem de χ′, χ≤k+1 por degenerescência, cota da união).
  3. **Banco de 34 exercícios por tipo** (B1 emparelhamentos ×10, B2 coloração de arestas ×8,
     B3 coloração de vértices ×8, B4 método probabilístico ×8), em três níveis
     (aquecimento / prova / desafio), cada um com **Dica** e **Resolução passo a passo** colapsáveis.
  Fecha com "erros que custam ponto" (por bloco) e checklist da véspera. Contagem regressiva no topo.
  - **Gabaritos-chave do banco:** B1·E1 ν=τ=4, defeito 1 · B1·E3 sem SDR (I={1,2,3,4}, união {1,2,3}),
    máx. 4 conjuntos · B1·E5 ν≥m/Δ via τ+König · B1·E10 há ≥|M*|−|M| caminhos aumentantes disjuntos ·
    B2·E2 **χ′=8** (contagem ⌈30/4⌉=8 supera Δ=7) · B2·E3 grade horária = 5 horários (Δ do multigrafo
    bipartido) · B2·E5 bipartido⟹Classe 1 por cadeia de Kempe (a paridade do caminho é onde a
    bipartição entra) · B2·E6 Petersen χ′=4 · B2·E7 K₉ e K₁₀ dão **9 dias** os dois ·
    B3·E1(d) \(\overline{C_7}\) tem χ=4 — a cota que salva é n/α, não ω · B3·E4 degenerescência ·
    B3·E6 circuito ímpar **mínimo** (sem cordas) + resto bipartido ⟹ χ≤5 · B4·E1 E[X]=5 triângulos
    mono em K₆ · B4·E3 R(k)>2^{k/2} · B4·E4 propriedade B, m(k)≥2^{k−1} · B4·E5 torneios S_k ·
    B4·E6 Caro–Wei · B4·E7 Szele · B4·E8 soma-livre (sortear o **multiplicador**, não o subconjunto).
  - Build em `scratchpad/p2pratico/` (`build.js` + 8 fragmentos + `check.js` de verificação).
    1 464 fórmulas pré-renderizadas, 0 erros, cache de glifos de 75 KB. **Verificado** em
    390/768/1280 px: sem scroll horizontal e sem distorção de razão de aspecto.
- **`guias/guia-p2-completo.html`** — **GUIA PRINCIPAL DA P2** (gerado 27/07/2026, 2,7 MB).
  Tema visual **"Papel & Tinta"** (claro, bege/serifado, tinta carmim+azul) — *deliberadamente diferente*
  do azul-escuro `#0f1419`/`#6ea8fe` dos demais guias, a pedido do Enzo. Cobre integralmente as aulas
  8e9→17, com **todas as demonstrações**: Parte I Hamiltonianos (c(G−S)≤|S|, Dirac, Ore c/ rotação de
  caminho, fecho Bondy–Chvátal + unicidade), Parte II Emparelhamentos (Berge via M△M*, Hall completo
  via Z/caminhos alternantes, defeito de Hall, k-regular bipartido → k emp. perfeitos, união de
  emparelhamentos, ν≤τ, König via Hall, König⟹Hall, SDR, corolário |N(S)|≥|S|+1), Parte III Coloração
  de arestas (χ′(Cₙ), χ′(Kₙ) c/ 1-fatoração rotacional, χ′≤2Δ−1, **Vizing** — leque/deslocamento/Kempe,
  Classe 1×2, bipartido⟹Classe 1), Parte IV Coloração de vértices (χ≥ω, χ·α≥n, e(G)≥C(χ,2), guloso,
  **Brooks** c/ os 3 casos, **Nordhaus–Gaddum** as 4 desigualdades), Parte V Método probabilístico
  §5.1–5.3 (cota da união, Erdős R(k)>2^{k/2}, hipergrafos, torneios Tₖ, linearidade, subgrafo bipartido
  e(H)≥e(G)/2, Szele, soma-livre, α(G)≥Σ1/(1+d(v)), Jensen) + apêndice §5.4–5.7 marcado como
  "não cai". Inclui: **Listas 4 e 5 resolvidas passo a passo**, simulado cronometrado (100 min,
  5 questões × 20 pts + gabarito comentado), plano de 10 h em 2 fins de semana (checklist persistido
  em localStorage), quiz de 18 questões, 24 flashcards, 4 blocos Feynman com checklist do corretor,
  cola de teoremas imprimível, busca na navegação e CSS de impressão.
  - **Gabarito Lista 4:** E1(a) grau ≤2 + alternância ⟹ caminhos/ciclos pares; (b) só vértices isolados
    e ciclos pares; (c) árvore tem ≤1 emp. perfeito (senão haveria ciclo). E2 troca em componente-caminho
    favorável a M, |N′|=|N|+1 preservando cobertura. **E3 = 6 dias** (n=7, e=16, χ′≥16/3⟹6; Vizing dá ≤6;
    tabela 3/3/3/3/2/2). **E4 = 4 dias** — o grafo é o **Petersen** (Kneser K(5,2)); χ′=4 pois se fosse 3
    haveria 1-fatoração e o 2-fator restante seria C₁₀ (Petersen não é hamiltoniano) ou dois C₅ (ímpares);
    escala 5+4+4+2 via raios + pentágono + pentagrama. E5 = χ′(Kₙ), resolvido na Parte III.
  - **Gabarito Lista 5:** E1 e(G)≥C(χ,2); E2 ordenar por classes de cor ⟹ guloso usa χ; E3 Nordhaus–Gaddum
    por indução; E4 troca usando n≥2χ(G) (+ nota de rigor sobre o caso (1,2)↦(2,1)); **E5** remover um
    circuito ímpar C deixa G−V(C) bipartido ⟹ χ≤2+3=5; **E6** grafos de intervalos: remover o intervalo de
    maior extremo esquerdo, vizinhos contêm ℓ_v ⟹ formam clique ⟹ χ=ω.
  - **Fórmulas pré-renderizadas** com `mathjax-full` (Node) em SVG, `fontCache:'global'` — 2 399 fórmulas,
    0 erros, cache de glifos de 89 KB injetado uma vez após `<body>`. Funciona **100% offline, sem CDN**.
    Script de build em `scratchpad/p2/build.js` (concatena 12 fragmentos + converte `\(…\)` e `\[…\]`).
    ⚠️ Com `fontCache:'local'` o arquivo ia a **7,5 MB**; `'global'` derruba para **2,7 MB** com o mesmo
    número de nós — usar sempre `'global'` daqui em diante.
- **`guias/guia-p1-completo.html`** — **GUIA PRINCIPAL DA P1** (gerado 06/07/2026). Autocontido,
  cobre TODO o conteúdo até a aula8e9: Cap. 1 (básicos, isomorfismo, conexidade, distância/cintura,
  bipartidos, Mantel), Cap. 3 (árvores, lagartas), Cap. 2 (eulerianos: Teo 2.1 + Cor. 2.1/2.2 + Fleury)
  e Cap. 4 (hamiltonianos: Teo 4.1 c(G−S)≤|S|, Dirac, Ore, Bondy–Chvátal, fecho) — **todas com
  demonstrações completas didáticas**. Inclui: Lista P1 resolvida (E1–E11) com SVGs fiéis dos grafos,
  simulado cronometrado (100 min, 5 questões + gabarito), cola de teoremas, quiz (10), flashcards (16),
  bloco Feynman. Fórmulas **pré-renderizadas** (mathjax-full, SVG offline — padrão pós-02/07).
  - Gabarito lista-p1: E1 diam=3, ham sim (1 2 4 3 5 6 1), trilha euleriana sim (2→3), caminho euleriano
    não; E2 G6,1=K6, G5,2=Petersen, r=C(n−k,k); E3 n=22; E4 ℓ≥Δ (contagem); E5 triângulo+pêndulo;
    E6 diam(Ḡ)≤2; E7(a) **todas as 6 são lagartas**, (b) aranha S(2,2,2)+folha; E8 **Herschel, não-ham**
    (bipartido 5/6; S={1,2,3,8,9} dá c=6>5); E9 arestas forçadas por grau 2; E10 crossover bipartido;
    E11 via Ore, exemplo K(n−1)+pêndulo.
  - ⚠️ **Escopo da P1 mudou**: a lista oficial cobre até hamiltonianos (aula8e9), não só Semanas 1–4.
    Nova data da P1 a confirmar com o Enzo (a de 29/06 do plano original passou).
- **`guias/guia-teoria-semanas1-4.html`** — guia HTML interativo de teoria de grafos
  (Semanas 1–4 / P1): resumo enxuto que ensina do zero, com exemplos resolvidos
  colapsáveis, cola de teoremas, quiz, flashcards e bloco Feynman.
- **`listas/resolucao-lista1.html`** — resolução passo a passo (nível essencial) da
  Lista 1 (E1–E7), com os diagramas de E1 redesenhados e respostas conferidas.
  - Gabarito: E1(a) **G₁≅G₂ sim**; E1(b) **H₁≇H₂** (16 vs 17 vértices); E2 **n−1**;
    E3 **|V|=15**; E4 n≡0/1 (mod 4); E5 **não** (forçaria 2-ciclo no iso. c/ complemento);
    E6 **2 pontos** (5 times); E7 grafo é **regular**.
- **`guias/guia-grafos-avancados-p2.html`** — guia HTML interativo de **grafos avançados**
  (Semanas 5–9 / P2, base aula6e7.pdf + Bondy & Murty/Diestel). Ensina do zero, com
  exemplos colapsáveis, diagramas SVG, quiz (10), flashcards (14), Feynman e cola. Cobre:
  **eulerianos** (Teorema de Euler — graus pares; Fleury, regra da ponte), **hamiltonianos**
  (Dirac δ≥n/2, Ore d(u)+d(v)≥n — suficientes, não necessárias), **emparelhamentos**
  (caminho aumentante + Berge; Hall |N(S)|≥|S| e König ν=τ em bipartidos; emparelhamento
  perfeito), **coloração de arestas** (χ', Vizing Δ≤χ'≤Δ+1) e **de vértices** (χ, Brooks
  χ≤Δ salvo Kₙ e ciclo ímpar). MathJax v3.

_Próximo: bloco de probabilidade discreta / método probabilístico (Semanas 9–11, P2 — T4)._

## Progresso
- [x] Plano de ensino indexado
- [x] Datas-chave preenchidas
- [x] Conteúdo das Semanas 1–4 mapeado (intro + aulas 1–4)
- [x] Guia de teoria (Semanas 1–4) gerado
- [x] Lista 1 resolvida (E1–E7)
- [x] Guia de grafos avançados (Semanas 5–9, P2) gerado
- [x] Material de probabilidade discreta (P2) — `aula17.pdf` = cap. 5 do livro
- [x] **Guia completo da P2 gerado (27/07/2026)** — aulas 8e9→17, tema Papel & Tinta
- [x] Listas 4 e 5 resolvidas (dentro do guia da P2)
- [x] **Caderno prático da P2 gerado (13/08/2026)** — ficha de decisão + 34 exercícios + roteiro
- [x] **Guia Mestre da P2 gerado (14/08/2026)** — glossário + mapa + checklist + 55 exercícios por conteúdo
- [x] Data da P2 corrigida para 17/08 dentro do `guia-p2-completo.html` (estava 10/08 no cabeçalho,
      na véspera do plano de 10h e no rodapé)
- [x] **Escopo do cap. 5 corrigido (15/08/2026)** — §5.4 e §5.5 caem; §5.6 e §5.7 não
- [x] **Listas 6 e 7 indexadas e resolvidas (15/08/2026)** — PRO-10…14 e ALT-01…03 no Guia Mestre
- [x] **Bloco 6 (método da alteração) criado no Guia Mestre** — teoria de §5.4/§5.5 + esqueleto de
      4 passos + 3 exercícios (era o único assunto do escopo sem nenhum material)
- [x] **Plano de 12 h até a P2 (sáb 15 → seg 17) no Guia Mestre**, seção `#plano12`
- [x] **Quiz de Emparelhamentos gerado (16/08/2026)** — 5 exercícios da Lista 4, tema + passos, linkado no dashboard
- [ ] **Confirmar com o professor** a data/horário da P2 remarcada; o `K_3`×`K_4` da Lista 7·E3;
      e o fecho esperado da Lista 6·E5 (caso da distância 3)
- [ ] Só se sobrar tempo depois da P2: `guia-p2-completo.html` ainda marca o apêndice §5.4–5.7
      como "provavelmente não cai" — o Guia Mestre já corrige, mas o Completo não foi tocado
- [ ] Conseguir `aula12.pdf` e `aula13.pdf` (lacuna sinalizada no guia)
- [ ] Rodar `python build-site.py` + publicar na Cloudflare para ler no celular
