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
| **10/08/2026** (seg) | **Prova 2 (P2)** — Semanas 5–11 | 50% |
| 12/08/2026 (qua) | Prova Substitutiva (SUB) — solicitar até 10/08 | — |
| 17/08/2026 (seg) | Vista de provas | — |
| 19/08/2026 (qua) | Prova de Recuperação (REC) | — |

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
  `lista5.pdf` (coloração por vértices, E1–E6), `lista-p1.pdf`.

### Conteúdo coberto até 27/07/2026 (escopo da P2 — confirmado pelo Enzo)
A P2 cobre **das aulas 8e9 até a 17**, ou seja:
- **Hamiltonianos** (aula8e9): c(G−S)≤|S|, Dirac, Ore, fecho de Bondy–Chvátal. *A P2 é cumulativa a partir daqui.*
- **Emparelhamentos** (aulas 10–11): maximal×máximo, caminho alternante/aumentante, **Berge**,
  **Hall** (+ versão com defeito), bipartidos k-regulares → k emparelhamentos perfeitos,
  cobertura por vértices, **König** (ν=τ), **SDR**.
- **Coloração de arestas** (aula14): χ′, χ′(Cₙ), χ′(Kₙ), χ′≥Δ, χ′≤2Δ−1, **Vizing**, Classe 1/2, bipartido ⟹ Classe 1.
- **Coloração de vértices** (aulas 15–16): χ, χ≥ω, χ·α≥n, e(G)≥C(χ,2), guloso, χ≤Δ+1,
  **Brooks**, **Nordhaus–Gaddum**.
- **Método probabilístico** (aula17 = cap. 5 do livro): **apenas §5.1–5.3** foram dadas em aula
  (fundamentos, cota da união, prova probabilística — Erdős R(k)>2^{k/2}, hipergrafos, torneios —,
  esperança/linearidade/indicadoras, primeiro momento, Jensen). **§5.4–5.7 (G(n,p), Markov/alteração,
  Chebyshev, Chernoff) NÃO caem** — ficaram como apêndice de reconhecimento no guia.

### Conteúdo coberto até 06/06/2026 (Semanas 1–4 → cai na P1)
Cap. 1 (conceitos básicos): grafo, grau, **aperto de mãos** (Σd=2|E|) e paridade;
isomorfismo, complemento e auto-complementar; passeios/trilhas/caminhos/ciclos (+ lema
passeio⟹caminho); subgrafos (induzido, gerador, remoção); conexidade e componentes;
δ(G)≥2 ⟹ caminho de comp. δ e ciclo ≥ δ+1; distância, diâmetro, **cintura** e
circunferência (g≤2·diam+1); **bipartidos** (⟺ sem ciclo ímpar); **Teorema de Mantel**
(⌊n²/4⌋) e subgrafo bipartido ≥|E|/2. Cap. 3: **árvores** (e=n−1, 4 caracterizações,
folhas, árvore geradora, ponte/vértice de corte). Clássicos: festa de 6 (R(3,3)≤6) e paridade.

## Guias gerados em `guias/`
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
- [ ] Conseguir `aula12.pdf` e `aula13.pdf` (lacuna sinalizada no guia)
- [ ] Rodar `python build-site.py` + publicar na Cloudflare para ler no celular
