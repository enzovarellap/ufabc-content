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
- `plano-ensino-md2.pdf`, `intro.pdf`, `aula1.pdf`, `aula2.pdf`, `aula3.pdf`, `aula3.2.pdf`, `aula4.pdf`
- Lista de exercícios em `listas/`: `lista1-md2.pdf` (E1–E7).

### Conteúdo coberto até 06/06/2026 (Semanas 1–4 → cai na P1)
Cap. 1 (conceitos básicos): grafo, grau, **aperto de mãos** (Σd=2|E|) e paridade;
isomorfismo, complemento e auto-complementar; passeios/trilhas/caminhos/ciclos (+ lema
passeio⟹caminho); subgrafos (induzido, gerador, remoção); conexidade e componentes;
δ(G)≥2 ⟹ caminho de comp. δ e ciclo ≥ δ+1; distância, diâmetro, **cintura** e
circunferência (g≤2·diam+1); **bipartidos** (⟺ sem ciclo ímpar); **Teorema de Mantel**
(⌊n²/4⌋) e subgrafo bipartido ≥|E|/2. Cap. 3: **árvores** (e=n−1, 4 caracterizações,
folhas, árvore geradora, ponte/vértice de corte). Clássicos: festa de 6 (R(3,3)≤6) e paridade.

## Guias gerados em `guias/`
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
- [ ] Material de probabilidade discreta (P2)
