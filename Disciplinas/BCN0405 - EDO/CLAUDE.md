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
| **07/08/2026** (sexta) | **Prova 2 (P2)** — _⚠️ conteúdo oficial (aulas 9-10, Listas 3-4) só chegou em 11/08, prazo já vencido → provavelmente remarcada, confirmar no Moodle_ | 50% |
| 11/08/2026 (terça) | Prova Substitutiva (SUB) — só com justificativa | — |
| **25/09/2026 (sexta), 19h** | **Exame de Recuperação (REC)** — _confirmado com o Enzo em 22/08/2026; a data 18/08 desta ficha era a antiga, de antes da P2 ser remarcada. **Sala ainda a confirmar no Moodle.**_ | — |

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
- `aula9.pdf` (Agosto 2026) — **EDOs lineares de 2ª ordem não-homogêneas**: operador diferencial `L = D²+p(x)D+q(x)` (linearidade, "anulador"), estrutura da solução geral `y = yh+yp` (complementar + particular), **método dos coeficientes a determinar** (polinômio/exponencial/seno-cosseno/produtos, tabela de chutes, caso de falha quando `yp` coincide com solução da homogênea → multiplicar por x), **método de variação dos parâmetros** (dedução via sistema de Cramer, fórmulas `u1'=-fy2/W`, `u2'=fy1/W`), exercícios resolvidos comparando os dois métodos.
- `aula10.pdf` (Agosto 2026) — **Aplicações de EDOs de 2ª ordem**: sistema massa-mola `mx''+γx'+kx=Fext`; oscilação livre sem amortecimento (forma alternativa `x(t)=A sen(ωt+φ)`, definições formais de período/frequência natural/amplitude/fase); oscilação livre com amortecimento e **classificação formal** super/critic./subamortecido via `Δ=γ²-4mk`; oscilação forçada sem amortecimento e **ressonância** (Exercício 14 da Lista 4 resolvido passo a passo) e **fenômeno de batimento** (`ω≠ω0`, envelope lento × oscilação rápida); circuitos **RLC em série** como analogia direta ao sistema massa-mola (`q`↔`x`, `L`↔`m`, `R`↔`γ`, `1/C`↔`k`).
- **Listas (`listas/`):** Lista 0 (revisão de derivadas/integrais), Lista 1 (classificação + 1ª ordem, Bernoulli/Riccati), Lista 2 (modelagem, autônomas, TEU), **Lista 3** (2ª ordem lineares homogêneas: PVI, Wronskiano/independência linear, redução de ordem, Euler-Cauchy, fórmula de Euler `e^{it}`, **PVC** — problema de valor de contorno), **Lista 4** (2ª ordem não-homogêneas: coef. indeterminados, variação de parâmetros, redução de ordem + não-homog., **aplicações massa-mola e circuitos RLC**, exs. 7–18). Todas com gabarito.

> Slides cobrem até substituições (Aula 4). Faltam para a P1 (só nas Listas): campo de direções, autônomas/estabilidade, modelagem e TEU.

## Guias gerados em `guias/`
- **`plano-rec-iedo.html`** (22/08/2026) — **Plano de revisão da REC (25/09)**: a régua de todo o resto.
  Traz a conta da nota-alvo, o método fixo de cada guia (**teoria enxuta → exemplos resolvidos → só então
  exercícios**, decidido com o Enzo), os **13 guias curtos** (45–60 min cada) com tópicos/fontes/porquê,
  o **cronograma de 5 semanas** (8–10h/semana, 24 blocos, 2 simulados) e os pontos de atenção (erros
  conhecidos dos gabaritos oficiais, ausência de provas antigas, os 2 gargalos do diagnóstico da P1).
  Checklist dos 13 guias com progresso salvo em `localStorage`. Sem MathJax de propósito (é um plano,
  não conteúdo — fórmulas em `<code>`, zero risco de CDN). Testado no navegador: 0 estouro horizontal
  em 390/768/1280 px, 0 erro de console.
- **`rec-guia-01-calculo-base.html`** (22/08/2026) — **REC · Guia 1: a base de Cálculo que a EDO exige** (~60 min).
  Não tem EDO nenhuma de propósito — ataca o gargalo nº 1 do diagnóstico pré-P1. Derivadas (cadeia, produto,
  quociente, `a^x`, truque do `ln`, implícita), integral por substituição (incl. troca de limites na definida),
  por partes com **LIATE** e o **caso cíclico** (`∫e^x cos x`, com a fórmula geral de `∫e^{at}sen(bt)`),
  **frações parciais** nos 3 casos (fatores simples, repetidos e **dividir antes**), e as integrais de socorro
  (`∫sec`, `∫tg`, `∫cotg`, `∫sen²`) que voltam em variação de parâmetros. 17 exemplos resolvidos passo a passo +
  exercícios recomendados (Lista 0: 1a,b,c · 7a,b,c,d · 8 · 9a,b,c,d,e,f · 11d) e 9 inéditos, todos com resolução
  em `<details>`. Erros comuns, 3 blocos Feynman (localStorage), 12 flashcards, quiz de 8 e cola de 1 página.
  **565 fórmulas pré-renderizadas em SVG**, 0 erro de TeX. Testado no navegador: 0 estouro horizontal e 0
  distorção de fórmula em 390/768/1280 px, 0 erro de console.
- **`rec-guia-02-linguagem-separaveis.html`** (22/08/2026) — **REC · Guia 2: a linguagem das EDOs e separáveis**
  (~50 min). Classificação (tipo/ordem/**linearidade** com os 4 assassinos da linearidade e a comparação
  `e^x·y` × `e^y`), forma geral × **forma normal**, PVI × PVC, o que é ser solução + roteiro de verificação em
  3 passos (incl. **intervalo de definição**), solução implícita, e **separáveis** (reconhecer pela fatoração,
  por que o método funciona via cadeia, os 2 passos, solução implícita × explícita, **escolha do ramo** pela
  condição inicial e domínio). 10 exemplos resolvidos + Lista 1 ex. 1 · 2b,e,f,g,h · 5a,b,c,d + 2 inéditos.
  Checklist de fechamento, erros comuns, 3 Feynman, 14 flashcards, quiz de 8 e cola. **531 fórmulas
  pré-renderizadas em SVG**, 0 erro de TeX; mesmos testes de navegador do Guia 1.
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

- **`guia-edo-p2-segunda-ordem.html`** (**reescrito em 11/08/2026**) — **Guia completo da P2**, gerado a partir do material
  oficial (aulas 9–10 + Listas 3–4 + exercícios recomendados). Formato **plano de ataque pré-prova de ~10h** (um fim de
  semana), definido com o Enzo. 28 seções, 1 802 fórmulas pré-renderizadas em SVG, 0 erros de TeX. Conteúdo:
  **Bloco 0 — socorro de Cálculo** (as 7 integrais que caem em variação de parâmetros: `∫sec` com a dedução do truque,
  `∫tan`, `∫cot`, `∫te^{at}`, `∫e^{at}sen(bt)` por partes cíclica + fórmula pronta, identidade `sen²=1−cos²`,
  soma-produto `cosA−cosB`) · superposição (+ contraexemplo não-linear, L3 ex.6) · **Wronskiano** e LI/LD com a
  **fórmula de Abel** (`W=Ce^{−∫p}` → um ponto basta) · TEU de 2ª ordem e maior intervalo (L3 ex.5, 6 itens) ·
  coef. constantes 3 casos (L3 ex.9, 10, 1, 2, 3) · redução de ordem com dedução (L3 ex.16a,b,d,f) · **Euler-Cauchy**
  pela substituição `x=ln t` (L3 ex.14c, 4 itens) · **operador `L`** (linearidade, anulador, prova de `y=y_h+y_p`) ·
  coef. a determinar + **caso de falha** (L4 ex.1a,b,c,d,e,i e 2a,h) · **variação de parâmetros** com a dedução completa
  via sistema/Cramer (L4 ex.3b,d e 4a,b,c) · **combo redução+não-homogênea** (L4 ex.5a,c) · massa-mola: montagem,
  livre s/ amort. (`A sen(ωt+φ)`, período/frequência/amplitude/fase), livre c/ amort. (**Δ=γ²−4mk**), forçada
  (**ressonância**, L4 ex.14 = exemplo da aula) e **batimento** (envelope lento × oscilação rápida) · **RLC** com a
  analogia completa (L4 ex.16) · **PVC** (L3 ex.17: os 3 destinos — única/infinitas/nenhuma) · **fórmula de Euler**
  `e^{it}` (L3 ex.13, 6 passos). Fecha com **erros comuns**, **5 blocos Feynman** (operador L, batimento, RLC, PVC,
  escolha do método — com respostas salvas no localStorage), **quiz de 12 questões** com placar, **18 flashcards** e
  **cola de 1 página** imprimível. Math pré-renderizado em SVG (mathjax-full/Node, `fontCache:'global'` → cache de
  glifos de 68 KB compartilhado, arquivo 3,0 MB; sem CDN, 100% offline). Testado no navegador: 0 estouro horizontal e
  0 distorção de fórmula em 390/768/1280 px, 0 erro de console, quiz/flashcards/busca/Feynman OK.

> 🚨 **Situação em 22/08/2026: o Enzo ficou de REC.** P2 aplicada (data exata não registrada aqui).
> **NF = 3,0** (F, confirmado pelo Enzo em 22/08) → pela regra `(NF+REC)/2 ≥ 4,5`, precisa de **REC ≥ 6,0**;
> o plano mira **7,0** para ter margem. Conceito máximo por REC é **C**. **Escopo da REC: tudo (P1+P2)**,
> confirmado com o Enzo. Ele **não tem** as provas P1/P2 corrigidas — simulados saem das Listas 0–4 +
> exercícios inéditos no mesmo estilo. Se a prova aparecer, refazer os simulados calibrados por ela.

> ⚠️ **Data da P2 (confirmado com o Enzo em 11/08/2026):** a P2 **foi remarcada** e ainda não foi aplicada — o mapa do
> quadrimestre listava 07/08, mas o material oficial só saiu em 11/08. **A data nova ainda não é conhecida**: o guia traz
> a pill "P2: remarcada — data a confirmar" no topo. Assim que o Enzo confirmar no Moodle, atualizar (a) esta ficha,
> (b) o `_dashboard/index.html` e (c) a pill do guia.

> 🐞 **Erros novos achados em 22/08/2026 (conferidos no sympy, sinalizados dentro do Guia 2 da REC):**
> 6. **Aula 1, exemplo 1:** enuncia `y' + y² = 1` com `φ(x)=tg x` como solução. Não é — `sec²x + tg²x = 1+2tg²x`.
>    O enunciado correto é **`y' − y² = 1`**; a cadeia de igualdades impressa no slide também não fecha.
>    (Para `y' + y² = 1` a solução seria `tgh x`.)
> 7. **Aula 2, exemplo 4:** a solução implícita `(y−1)² = x³+2x²+2x+4` e o intervalo `(−2,∞)` estão certos,
>    mas a explícita sai como `y = 1 + √(...)`, que dá `y(0)=3` e **viola a condição inicial `y(0)=−1`** do
>    próprio exemplo. O correto é **`y = 1 − √(...)`** (o ramo negativo).

> 🐞 **Erros encontrados nas fontes oficiais (11/08/2026, todos conferidos no sympy e sinalizados no topo do guia):**
> 1. **Aula 9, ex. 1** (`y''−5y'+6y=e^x`): resposta do slide traz `+2e^{2x}+3e^{3x}` redundantes (já estão em c₁,c₂).
> 2. **Aula 10, exemplo subamortecido**: slide diz `x(0)=0, x'(0)=0` (daria `x≡0`); o correto é `x(0)=1, x'(0)=0`.
>    No exemplo criticamente amortecido, "x(t)<0 para todo t>0" deveria ser "x(t)>0".
> 3. **Aula 10, ex.14** (batimento): o slide escreve `sen((ω−1)t/2)`; mantendo `6/(1−ω²)` na frente, o correto é
>    `sen((1−ω)t/2)` (diferem por um sinal global). A fórmula geral do batimento no slide 22 está correta.
> 4. **Lista 4, ex. 5a** (`t²y''−2y=3t²−1`): gabarito dá constante `+1/3`; o correto é **`+1/2`** (de `−2A=−1`).
> 5. **Lista 4, ex. 7**: gabarito escreve `x(0)=−0,8` mas usa `−0,2` na resposta (a resposta é que está certa).

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
- **Lista 3** (2ª ordem homogêneas): 5, 6, 8 (verificar y1/y2 soluções) · 4, 7a,b, 8 · 1, 2, 3, 9b,c,f,h,i,j,l, 10a,b,e, 14c, 16a,b,d,f, 17b (encontrar solução geral e usar as duas condições p/ C1,C2) — _11/08/2026_
- **Lista 4** (2ª ordem não-homogêneas + aplicações): 1a,b,c,d,e,i, 2a,h, 3b,d, 4a,b,c, 5a,c, 7, 8, 12, 13 — _11/08/2026_

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
- [x] Material oficial da P2 indexado — `material/aula9.pdf` (não-homogêneas: operador L, coef. indeterminados, variação
  de parâmetros) e `material/aula10.pdf` (aplicações: massa-mola, ressonância, batimento, circuitos RLC); **Lista 3**
  (homogêneas + PVC) e **Lista 4** (não-homogêneas + aplicações) recebidas e exercícios recomendados preenchidos (11/08/2026)
- [x] **Guia da P2 completo** — `guias/guia-edo-p2-segunda-ordem.html` **reescrito do zero em 11/08/2026** a partir das
  aulas 9–10 e Listas 3–4: bloco 0 de Cálculo, superposição/Wronskiano+Abel, TEU 2ª ordem, redução de ordem, coef.
  constantes, Euler-Cauchy, operador `L`/anulador, coef. a determinar + caso de falha, variação de parâmetros (com
  dedução), combo redução+não-homogênea, vibrações (livre/amortecida via `Δ=γ²−4mk`/forçada+ressonância+batimento),
  circuitos RLC, PVC e fórmula de Euler. Formato plano de 10h; Feynman + quiz + flashcards + cola. Todas as contas
  conferidas no sympy (5 erros dos gabaritos oficiais documentados acima); layout testado no navegador.
- [x] **Plano de revisão da REC** — `guias/plano-rec-iedo.html` (22/08/2026): 13 guias curtos + cronograma
  de 5 semanas + 2 simulados, agendado no Google Calendar
- [x] **REC · Guia 1** — `guias/rec-guia-01-calculo-base.html` (22/08/2026): base de Cálculo, 565 fórmulas
- [x] **REC · Guia 2** — `guias/rec-guia-02-linguagem-separaveis.html` (22/08/2026): linguagem + separáveis, 531 fórmulas
- [ ] **Gerar os 11 guias restantes da REC**, um por vez, no formato teoria → exemplos → exercícios:
  ~~1. Base de Cálculo~~ · ~~2. Linguagem das EDOs + separáveis~~ · 3. Fator integrante ·
  4. Substituições · 5. Qual método usar (reconhecimento) · 6. Modelagem · 7. Autônomas/reta de fase ·
  8. TEU · 9. 2ª ordem homogênea coef. constantes · 10. Wronskiano/redução/Euler-Cauchy ·
  11. Coef. a determinar · 12. Variação de parâmetros · 13. Massa-mola e RLC
- [ ] **Simulado 1** (1ª ordem, 2h cronometradas) para 12/09 e **Simulado 2** (completo) para 21/09
- [ ] **Confirmar no Moodle: horário da REC e a NF exata** (a NF muda a nota-alvo)
- [ ] ~~Confirmar a nova data da P2 no Moodle~~ (obsoleto — P2 já aplicada) e propagar para: ficha acima, `_dashboard/index.html`, pill do guia e
  eventos do Google Calendar (criar revisões espaçadas 1/3/7 dias a partir do fim de semana de estudo)
- [ ] (opcional) Resoluções passo a passo completas das **Listas 3 e 4** em `listas/`, no padrão das Listas 0/1/2 —
  o guia já resolve os principais recomendados, mas faltam L3 ex.11/12/15 e L4 ex.6/9/10/11/15/17/18
