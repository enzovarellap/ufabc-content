# BACKLOG — lacunas de EDO e Matemática Discreta II (gerado 27/06/2026)

Ordem = prioridade. Faça de cima para baixo. Marque `[x]` ao concluir (Verificação obrigatória feita).
Prazos: **P1 Discreta 29/06 (seg)**, **P1 EDO 30/06 (ter)**, **P2 EDO 07/08**, **P2 Discreta 10/08**.

---

## [x] T1 — EDO · Resolução da Lista 2 (P1 — URGENTE)
- **Skill:** `calculus-problem-set-solver`.
- **Entrada:** `Disciplinas/BCN0405 - EDO/listas/lista2 (1).pdf` (6 págs). Apoio: `material/aula5.pdf` (Aplicações/Modelagem), guias P1 já existentes em `guias/`.
- **Saída:** `Disciplinas/BCN0405 - EDO/listas/resolucao-lista2.html`.
- **Conteúdo coberto pela lista:** crescimento/decaimento (bactérias, Césio-137 meia-vida), curva de aprendizado \(dP/dt=k(M-P)\), resfriamento de Newton, misturas (tanque com vazões diferentes), modelo de adoção/publicidade (logístico), Gompertz, circuito RC. Ou seja: **modelagem com EDO de 1ª ordem, equações autônomas/análise qualitativa e TEU**.
- **Critérios:** cada exercício com montagem da EDO → método → solução → interpretação. Respostas conferidas no `sympy`. Seguir Regras de fórmulas (MathJax).
- **Ao concluir:** atualizar `BCN0405 - EDO/CLAUDE.md` (marcar resolução da Lista 2).

## [x] T2 — EDO · Revisar e completar o Guia 3 (P1)
- **Skill:** `university-study-guide`.
- **Arquivo:** `Disciplinas/BCN0405 - EDO/guias/guia-edo-p1-modelagem-autonomas-teu.html` (já existe, mas hoje só tem isóclinas + pontos de equilíbrio).
- **Tarefa:** auditar o que já existe e **completar** para cobrir, com exemplos resolvidos: (a) **modelagem** de 1ª ordem (decaimento/crescimento, resfriamento, misturas, logístico/Gompertz — base `material/aula5.pdf` e Lista 2); (b) **equações autônomas** (linha de fase, estabilidade de equilíbrios, classificação atrator/repulsor/semiestável); (c) **Teorema de Existência e Unicidade** (enunciado, hipóteses de continuidade de \(f\) e \(\partial f/\partial y\), exemplos de aplicação e de falha de unicidade).
- **Critérios:** não regredir o conteúdo existente; manter MathJax; quiz/Feynman/cola presentes. Conferir contas no sympy.
- **Ao concluir:** atualizar `CLAUDE.md` (marcar Guia 3 concluído).

## [x] T3 — Discreta II · Guia P2-a: grafos avançados
- **Skill:** `university-study-guide`.
- **Entrada:** `Disciplinas/MCCC010 - Matematica Discreta II/material/aula6e7.pdf` (+ `plano-ensino-md2.pdf` para escopo). Complementar com referência padrão (Bondy & Murty / Diestel) quando o slide for esparso.
- **Saída:** `Disciplinas/MCCC010 - Matematica Discreta II/guias/guia-grafos-avancados-p2.html`.
- **Tópicos (Semanas 5–~9):** grafos **eulerianos** (Teorema de Euler, algoritmo de Fleury) e **hamiltonianos** (Dirac, Ore); **emparelhamentos** (Teorema de Berge dos caminhos aumentantes, Hall e König em bipartidos, fator/emparelhamento perfeito); **coloração de arestas** (índice cromático, Teorema de Vizing) e **de vértices** (número cromático, Teorema de Brooks).
- **Critérios:** definições + teoremas com ideia de prova + exemplos pequenos com diagramas (SVG ou descrição). MathJax para toda notação. Quiz/Feynman/cola.
- **Ao concluir:** atualizar `CLAUDE.md`.

## [ ] T4 — Discreta II · Guia P2-b: probabilidade discreta / método probabilístico
- **Skill:** `university-study-guide`.
- **Entrada:** ementa em `plano-ensino-md2.pdf` (sem slides ainda → ensinar do zero a partir de referência padrão: Alon & Spencer / Mitzenmacher-Upfal).
- **Saída:** `Disciplinas/MCCC010 - Matematica Discreta II/guias/guia-probabilidade-p2.html`.
- **Tópicos (Semanas ~9–11):** espaço de probabilidade discreto, **variáveis aleatórias** e **esperança** (linearidade), indicadores; desigualdades de **Jensen**, **Markov** e **Chebyshev**; modelo **Erdős-Rényi** \(G(n,p)\); **método do primeiro momento** (existência por \(E[X]<1\Rightarrow P(X=0)>0\)) e **segundo momento** (Var/Chebyshev), **método da alteração** e ideia de **concentração**. Aplicação clássica: cota inferior para \(R(k,k)\) e existência de grafos com cintura e número cromático grandes.
- **Critérios:** muita intuição + exemplos numéricos pequenos conferidos no sympy. MathJax. Quiz/Feynman/cola.
- **Ao concluir:** atualizar `CLAUDE.md`.

## [ ] T5 — EDO · Guia P2: EDO lineares de 2ª ordem
- **Skill:** `university-study-guide`.
- **Entrada:** ementa em `material/plano de ensino.pdf` (sem slides de 2ª ordem ainda → ensinar do zero a partir de Zill / Boyce-DiPrima).
- **Saída:** `Disciplinas/BCN0405 - EDO/guias/guia-edo-p2-segunda-ordem.html`.
- **Tópicos:** EDO linear de 2ª ordem (homogênea/não-homogênea), independência linear e **Wronskiano**, **redução de ordem**; **coeficientes constantes** (equação característica: raízes reais distintas, repetidas, complexas); **Euler-Cauchy**; **coeficientes a determinar** e **variação de parâmetros**; **vibrações mecânicas** massa-mola (livre/amortecida/forçada, ressonância).
- **Critérios:** cada método com receita + exemplo resolvido conferido no sympy. MathJax. Quiz/Feynman/cola.
- **Ao concluir:** atualizar `CLAUDE.md`.

---

### Notas
- Discreta II tem **só a Lista 1** (já resolvida) — não há Lista 2 para resolver nesta rodada.
- EDO Lista 0 e Lista 1 já estão resolvidas (`listas/resolucao-lista0.html`, `resolucao-lista1.html`).
- Depois de T1–T2 (P1) rodar a publicação: `python build-site.py` (ver `COMO-PUBLICAR.md`).
