# BCN0405-15 — Introdução às Equações Diferenciais Ordinárias

## Ficha
- **Sigla:** BCN0405-15
- **Turma:** A1 — Noturno
- **Campus:** Santo André
- **TPI:** 4 - 0 - 4 (Teórica 4 / Prática 0 / Individual 4)
- **Professor:** Edson Alex Arrázola Iriarte (atendimento Ter/Sex 17–18h, sala 821-B; Moodle)
- **Turma:** NA1 — Sala A103-0
- **Horários:**
  - Terça-feira, 21:00–23:00 (semanal)
  - Sexta-feira, 19:00–21:00 (semanal)

## Ementa / Tópicos
EDOs de 1ª ordem (separáveis, fator integrante, exatas, substituições: homogênea/Bernoulli,
PVI, campo de direções, autônomas/análise qualitativa); modelagem (decaimento, resfriamento,
populacional, misturas); Teorema de Existência e Unicidade; EDOs lineares de 2ª ordem
(Wronskiano, redução de ordem, coef. constantes, Euler-Cauchy); coeficientes indeterminados
e variação de parâmetros; vibrações mecânicas (massa-mola); sistemas convertidos a EDO de ordem superior.
Bibliografia base: Zill; Boyce & DiPrima; Edwards & Penney.

## Datas-chave (do plano de ensino)
| Data | Avaliação / Entrega | Peso |
|---|---|---|
| **03/07/2026** (sexta) | **Prova 1 (P1)** — _remarcada (era 30/06)_ | 50% |
| **07/08/2026** (sexta) | **Prova 2 (P2)** | 50% |
| 11/08/2026 (terça) | Prova Substitutiva (SUB) — só com justificativa | — |
| 18/08/2026 (terça) | Exame de Recuperação (REC) | — |

## Critério de avaliação
NF = (P1 + P2)/2. **Aprovação exige P1 ≥ 4,5 E P2 ≥ 4,5.** Conceitos: A ≥ 8,5; B ≥ 7,0;
C ≥ 5,5; D ≥ 4,5. Frequência < 75% → conceito O. REC só para F ou D (média (NF+REC)/2; conceito máx. C).

## Material em `material/`
- `plano de ensino.pdf`
- `aula1.pdf` — Fundamentos: terminologia, classificação (tipo/ordem/linearidade), forma geral/normal, solução (explícita/implícita/trivial), verificação, intervalo de definição.
- `aula2.pdf` — Equações separáveis: método, implícita × explícita, PVI, domínio.
- `aula3.pdf` — Lineares de 1ª ordem: forma padrão e fator integrante (com dedução).
- `aula4.pdf` (13/06/2026) — Métodos de substituição: `y'=F(ax+by+c)` (v=ax+by+c), homogêneas (v=y/x), Bernoulli (v=y¹⁻ⁿ) e Riccati* (y=y₁+1/z).
- `aula5.pdf` — Aplicações I (modelagem): modelo entrada−saída, exponencial (crescimento/decaimento), C-14 + meia-vida, ratos+predação, resfriamento de Newton, misturas em tanque (volume constante e variável). _Conteúdo já coberto pelo Guia 3._
- `aula6.pdf` — Equações autônomas: análise qualitativa pelo sinal de f(y), equilíbrios, reta de fase, estabilidade (estável/instável/semiestável), roteiro 5 passos, logística y'=y(1−y). _Conteúdo já coberto pelo Guia 3._
- **Listas (`listas/`):** Lista 0 (revisão de derivadas/integrais), Lista 1 (classificação + 1ª ordem, Bernoulli/Riccati), Lista 2 (modelagem, autônomas, TEU). Todas com gabarito.

> Slides cobrem até substituições (Aula 4). Faltam para a P1 (só nas Listas): campo de direções, autônomas/estabilidade, modelagem e TEU.

## Guias gerados em `guias/`
- **`guia-edo-p1-fundamentos.html`** (07/06/2026) — Guia 1, **aprofundado**: fundamentos/classificação, separáveis e lineares de 1ª ordem (com dedução do fator integrante). Exemplos das Listas 0/1 + Feynman.
- **`guia-edo-p1-substituicoes.html`** (17/06/2026) — Guia 2, **aprofundado** (Aula 4): métodos de substituição — `y'=F(ax+by+c)`, homogêneas, Bernoulli e **Riccati** (tópico extra, da Lista 1 ex.12). Exemplos do slide + Lista 1, conferidos simbolicamente. Tem link cruzado com o Guia 1.
- **`guia-edo-p1-revisao.html`** (29/06/2026) — **Guia de revisão da P1**: mapa de todos os tópicos da P1 com link pro guia que aprofunda cada um, + aprofundamento condensado do conteúdo novo (aula5 modelagem + aula6 autônomas) com active recall, Feynman, cola de 1 página e quiz. Contas (Newton/mistura/logística) conferidas no sympy.
- **`guia-edo-p1-modelagem-autonomas-teu.html`** (27/06/2026) — Guia 3, **fecha a P1**: campo de direções/isóclinas, **equações autônomas** (reta de fase, equilíbrios, estabilidade atrator/repulsor/semiestável via sinal de `f(y)` e `f'(y₀)`), **modelagem de 1ª ordem** (exponencial + meia-vida, resfriamento de Newton, crescimento limitado/aprendizado/difusão, **Gompertz**, misturas em tanque) e **TEU** (Picard–Lindelöf, hipóteses de continuidade de `f` e `∂f/∂y`, falha de unicidade em `y'=y^{1/3}`, intervalo de validade). Exemplos resolvidos da Lista 2 (incl. Gompertz ex.8 com `r=0,71`, `K=80,5·10⁶`), conferidos no sympy. Math pré-renderizado em SVG (MathJax). Quiz + Feynman + cola.

Para resolver listas: `calculus-problem-set-solver`. **Prioridade alta** (matéria difícil).

## Exercícios recomendados pelo professor (do Moodle/aula)
> Fonte: listas oficiais em gradmat.ufabc.edu.br/disciplinas/iedo. Lista 2 ainda **sem recomendação**.
- **Lista 0** (rev. Cálculo): 1a,b,c · 7a,b,c,d · 8 · 9a,b,c,e,f — _atualizado 08/06/2026_
- **Lista 1** (classif. + 1ª ordem): 1 · 2b,e,f,g,h · 5a,b,c,d,e,f — _atualizado 08/06/2026_; 6 · 7 · 8 · 9 · 10 — _atualizado 10/06/2026_
- _Obs.: 5a–f são separáveis (5g–j homogêneas não foram pedidas); Bernoulli (11) e Riccati (12) ainda não recomendados._

## Progresso
- [x] Plano de ensino indexado
- [x] Datas-chave preenchidas
- [x] Guia 1 gerado — fundamentos, separáveis, lineares 1ª ordem (07/06/2026)
- [x] Guia 2 gerado — métodos de substituição + Riccati (17/06/2026)
- [x] Guia 3 gerado/auditado — campo de direções, autônomas/estabilidade, modelagem (incl. Gompertz) e TEU (fecha a P1) — `guias/guia-edo-p1-modelagem-autonomas-teu.html` (27/06/2026, conferido no sympy)
- [x] Resoluções passo a passo das listas recomendadas — `listas/resolucao-lista0.html` e `listas/resolucao-lista1.html` (17/06/2026, conferidas no sympy)
- [x] Resolução passo a passo da **Lista 2** (P1) — `listas/resolucao-lista2.html` (27/06/2026): 13 exercícios — modelagem (bactérias, Césio-137, aprendizado, Newton, misturas em tanque, publicidade, RC, Gompertz, Von Bertalanffy), equações autônomas/estabilidade e TEU. Todas as contas conferidas no sympy; MathJax; mesmo tema das Listas 0/1.
- [x] Guia de **revisão da P1** gerado — `guias/guia-edo-p1-revisao.html` (29/06/2026): mapa da P1 + foco modelagem/autônomas (aulas 5–6) + cola/quiz/Feynman. Aulas 5 e 6 indexadas; **P1 remarcada para sexta 03/07**.
- [ ] Guia da P2: 2ª ordem (coef. constantes, Euler-Cauchy), variação de parâmetros, vibrações
