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
- `aula6-v2.pdf` (02/07/2026) — Autônomas **revisada**: vocabulário formal (ponto × solução de equilíbrio, **assintoticamente estável** com lim y(x)=c), **propriedades geométricas das curvas solução** (unicidade → curvas não se cruzam/tangenciam, nenhuma cruza equilíbrio), roteiro 5 passos, exemplos y'=y−1, y'=2−y, logística.
- `aula7.pdf` (02/07/2026) — **Modelos de população**: Malthusiano (P'=kP, limitações) e **logístico de Verhulst** P'=P(a−bP)=rP(1−P/K), K=a/b capacidade de carga, solução explícita P(t)=aP₀/(bP₀+(a−bP₀)e^{−at}), lim=K, curva em S; ref. Exercício 6.13 do livro do Santos.
- `aula8.pdf` (02/07/2026) — **TEU** formalizado: retângulo R, f e f_y contínuas → existência e unicidade local em J⊂(a,b), + consequências geométricas (mesmas da aula 6-v2).
- **Listas (`listas/`):** Lista 0 (revisão de derivadas/integrais), Lista 1 (classificação + 1ª ordem, Bernoulli/Riccati), Lista 2 (modelagem, autônomas, TEU). Todas com gabarito.

> Slides cobrem até substituições (Aula 4). Faltam para a P1 (só nas Listas): campo de direções, autônomas/estabilidade, modelagem e TEU.

## Guias gerados em `guias/`
- **`guia-edo-p1-fundamentos.html`** (07/06/2026) — Guia 1, **aprofundado**: fundamentos/classificação, separáveis e lineares de 1ª ordem (com dedução do fator integrante). Exemplos das Listas 0/1 + Feynman.
- **`guia-edo-p1-substituicoes.html`** (17/06/2026) — Guia 2, **aprofundado** (Aula 4): métodos de substituição — `y'=F(ax+by+c)`, homogêneas, Bernoulli e **Riccati** (tópico extra, da Lista 1 ex.12). Exemplos do slide + Lista 1, conferidos simbolicamente. Tem link cruzado com o Guia 1.
- **`guia-edo-p1-revisao.html`** (29/06/2026) — **Guia de revisão da P1**: mapa de todos os tópicos da P1 com link pro guia que aprofunda cada um, + aprofundamento condensado do conteúdo novo (aula5 modelagem + aula6 autônomas) com active recall, Feynman, cola de 1 página e quiz. Contas (Newton/mistura/logística) conferidas no sympy.
- **`guia-edo-p1-modelagem-autonomas-teu.html`** (27/06/2026) — Guia 3, **fecha a P1**: campo de direções/isóclinas, **equações autônomas** (reta de fase, equilíbrios, estabilidade atrator/repulsor/semiestável via sinal de `f(y)` e `f'(y₀)`), **modelagem de 1ª ordem** (exponencial + meia-vida, resfriamento de Newton, crescimento limitado/aprendizado/difusão, **Gompertz**, misturas em tanque) e **TEU** (Picard–Lindelöf, hipóteses de continuidade de `f` e `∂f/∂y`, falha de unicidade em `y'=y^{1/3}`, intervalo de validade). Exemplos resolvidos da Lista 2 (incl. Gompertz ex.8 com `r=0,71`, `K=80,5·10⁶`), conferidos no sympy. Math pré-renderizado em SVG (MathJax). Quiz + Feynman + cola.

- **`guia-edo-p1-vespera.html`** (02/07/2026) — **Guia de véspera da P1** (prova 03/07): plano de ataque
  de 5–6h calibrado por diagnóstico (Enzo errou as 4 questões-teste; base de cálculo fraca). Blocos com
  timer: base de cálculo de emergência → classificação → separáveis → fator integrante → autônomas →
  TEU → modelagem → substituições (opcional) → cola de 1 página + quiz de 8 questões. Contas conferidas
  no sympy. Meta explícita: garantir ≥ 4,5. **Math pré-renderizado em SVG** (mathjax-full/Node, sem CDN —
  o tex-svg via CDN não carregou na máquina do Enzo em 02/07; mesmo esquema do Guia 3).
  **Ampliado 02/07 (noite)** com as aulas 6-v2/7/8: vocabulário formal de estabilidade, propriedades
  geométricas das curvas, Malthus + logística (K, solução explícita, curva em S), consequências
  geométricas do TEU e 2 questões novas no quiz (análise qualitativa era o gap sentido pelo Enzo).
- **`guia-edo-p1-metro.html`** (02/07/2026, feito pelo Enzo) — revisão da P1 para ler no metrô.
- **`guia-edo-p1-quiz-caminho-certo.html`** (03/07/2026) — **Quiz "Escolha o caminho certo"**: 53 cartões / 60 passos
  interativos cobrindo os exercícios recomendados das Listas 0, 1 e 2 (+ Zill §2.5). Treina **reconhecimento de método**
  sem fazer contas: por exercício, escolhe-se a técnica → a substituição/1º passo → o próximo passo. Feedback imediato
  com o "porquê" de cada caminho; placar conta acertos de 1ª; barra de progresso. Cobre: Lista 0 (derivadas — cadeia/
  produto/quociente; integrais — substituição, partes incl. cíclica 8c, frações parciais incl. dividir-antes 9e/9f);
  Lista 1 (classificação ordem/linearidade; separável×homogênea×linear no Ex.5; fator integrante Ex.6/7; comportamento
  t→∞ Ex.8/9/10; Bernoulli 11e,f; Riccati 12a); Lista 2 (montar a EDO de modelagem Ex.1–6; autônomas/estabilidade
  incl. semiestável 9a,b,d,e,f,g). Respostas conferidas contra os gabaritos oficiais das listas. **Math pré-renderizado
  em SVG** (mathjax-full/Node, fontCache local — sem CDN, 100% offline, mesmo esquema do Guia 3/véspera). Testado no
  navegador (Playwright): fluxo, feedback e placar OK, 0 erros de console. Endereça diretamente o gap do diagnóstico da
  P1 (identificação de método).

Para resolver listas: `calculus-problem-set-solver`. **Prioridade alta** (matéria difícil).

> **Diagnóstico pré-P1 (02/07/2026):** Enzo errou as 4 questões-diagnóstico (identificação de método,
> fator integrante, estabilidade, TEU), não resolve separável simples e reporta base de Cálculo fraca —
> leu apenas parcialmente os Guias 1 e 3. Pós-P1: independente do resultado, planejar revisão de base
> de Cálculo + estudo espaçado desde o início do conteúdo da P2 (não repetir véspera).

## Exercícios recomendados pelo professor (do Moodle/aula)
> Fonte: listas oficiais em gradmat.ufabc.edu.br/disciplinas/iedo. Espelho em `listas/Exercicios Recomendados .txt`.
- **Lista 0** (rev. Cálculo): 1a,b,c · 7a,b,c,d · 8 · 9a,b,c,e,f — _atualizado 08/06/2026_
- **Lista 1** (classif. + 1ª ordem): 1 · 2b,e,f,g,h · 5a,b,c,d,e,f — _08/06_; 6 · 7 · 8 · 9 · 10 — _10/06_; **5g,h,i,j (homogêneas) · 11e,f (Bernoulli) · 12a (Riccati)** — _19/06/2026_
- **Lista 2** (modelagem/autônomas/TEU): 1 · 2 · 3 · 4 — _19/06_; 5 · 6 — _24/06_; **9a,b,d,e,f,g** — _27/06/2026_
- **Zill, Seção 2.5:** 3 · 13 · 17 · 21 · 24 · 26 · 27 — _19/06/2026_

## Progresso
- [x] Plano de ensino indexado
- [x] Datas-chave preenchidas
- [x] Guia 1 gerado — fundamentos, separáveis, lineares 1ª ordem (07/06/2026)
- [x] Guia 2 gerado — métodos de substituição + Riccati (17/06/2026)
- [x] Guia 3 gerado/auditado — campo de direções, autônomas/estabilidade, modelagem (incl. Gompertz) e TEU (fecha a P1) — `guias/guia-edo-p1-modelagem-autonomas-teu.html` (27/06/2026, conferido no sympy)
- [x] Resoluções passo a passo das listas recomendadas — `listas/resolucao-lista0.html` e `listas/resolucao-lista1.html` (17/06/2026, conferidas no sympy)
- [x] Resolução passo a passo da **Lista 2** (P1) — `listas/resolucao-lista2.html` (27/06/2026): 13 exercícios — modelagem (bactérias, Césio-137, aprendizado, Newton, misturas em tanque, publicidade, RC, Gompertz, Von Bertalanffy), equações autônomas/estabilidade e TEU. Todas as contas conferidas no sympy; MathJax; mesmo tema das Listas 0/1.
- [x] Guia de **revisão da P1** gerado — `guias/guia-edo-p1-revisao.html` (29/06/2026): mapa da P1 + foco modelagem/autônomas (aulas 5–6) + cola/quiz/Feynman. Aulas 5 e 6 indexadas; **P1 remarcada para sexta 03/07**.
- [x] **Quiz "Escolha o caminho certo"** — `guias/guia-edo-p1-quiz-caminho-certo.html` (03/07/2026): 53 cartões
  interativos de reconhecimento de método (sem contas) das Listas 0/1/2 + Zill §2.5; feedback imediato + placar;
  SVG pré-renderizado (offline); testado no navegador.
- [ ] Guia da P2: 2ª ordem (coef. constantes, Euler-Cauchy), variação de parâmetros, vibrações
