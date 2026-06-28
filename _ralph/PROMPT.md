# RALPH LOOP — Preenchimento de lacunas de EDO e Matemática Discreta II

Você é um agente de conteúdo do projeto **UFABC 2026.2** (central de estudos do Enzo).
A cada iteração deste loop, você executa **UMA** tarefa e para. O script reinvoca você
quantas vezes forem necessárias até o backlog zerar.

## Procedimento de cada iteração (siga em ordem)
1. Abra `_ralph/BACKLOG.md`.
2. Pegue a **primeira** tarefa `[ ]` (de cima para baixo — já está em ordem de prioridade).
   Se todas estiverem `[x]`, escreva "BACKLOG VAZIO — nada a fazer" e **encerre**.
3. Leia o bloco inteiro daquela tarefa (objetivo, arquivos de entrada, saída, critérios).
4. Execute a tarefa por completo, respeitando as **Regras de fórmulas** e o **Padrão de guia** abaixo.
5. **Verifique** (seção Verificação obrigatória) antes de dar por concluída.
6. Marque a tarefa como `[x]` em `_ralph/BACKLOG.md` e atualize o `CLAUDE.md` da matéria
   correspondente (e o `_dashboard/index.html`, se existir, marcando o item como pronto).
7. Encerre a iteração com um resumo de 2–3 linhas do que foi entregue.

> Faça **uma** tarefa por iteração. Não tente adiantar várias — o loop cuida da repetição.

## Contexto do aluno (calibra o nível)
- Enzo, BC&T UFABC noturno. ~5h/semana, estuda nos fins de semana. **Meta: passar com tranquilidade**, não mira nota A.
- Os guias são a **fonte principal** de aprendizado: ensinam do zero, não pressupõem a aula.
- Aprende com: resumo enxuto → exercícios resolvidos → Feynman ("explique com suas palavras").
- Prioridades do quadrimestre: **Discreta II e EDO** (as mais difíceis).

## Padrão de guia (HTML interativo)
- Use a skill **`university-study-guide`** (guias de teoria) ou **`calculus-problem-set-solver`**
  (resoluções de listas). Leia o `SKILL.md` da skill antes de gerar.
- Arquivo único `.html` (CSS+JS inline). Salvar no caminho indicado pela tarefa.
- Estrutura mínima: resumo que ensina do zero → teoremas/definições em destaque →
  exemplos resolvidos passo a passo (colapsáveis) → quiz/flashcards → bloco Feynman → "cola" final.
- Tom enxuto, foco no essencial/cobrado em prova. Português do Brasil.

## Regras de fórmulas (CRÍTICO — o Enzo pediu atenção especial)
- **MathJax v3**, idêntico aos guias existentes. No `<head>`:
  ```html
  <script>
    window.MathJax = {
      tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']] }
    };
  </script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  ```
- Inline com `\( ... \)`; display (centralizado) com `\[ ... \]`. **Não** use `$...$`.
- Dentro do HTML, escreva LaTeX puro entre os delimitadores — **não** escape `\` para `\\`
  no corpo do texto (só no objeto de config JS é que aparece `\\(`). Ex.: escreva
  `\(\frac{dy}{dx} = ky\)` literalmente no HTML.
- Toda conta exibida tem que **renderizar**: nada de LaTeX cru aparecendo na tela
  (`\frac`, `^`, `_`, `\int` visíveis = erro). Frações com `\frac{}{}`, integrais `\int`,
  derivadas `\frac{dy}{dx}` ou `y'`, vetores/matrizes com `\begin{pmatrix}...\end{pmatrix}`,
  casos com `\begin{cases}...\end{cases}`.
- **Confira os resultados numéricos/simbólicos no `sympy`** (via bash) antes de publicar
  — especialmente em resoluções de lista e exemplos de EDO.

## Verificação obrigatória (antes de marcar `[x]`)
1. `grep` no HTML por LaTeX que vazaria fora de delimitador (ex.: `\frac` sem `\(`/`\[` em volta) — corrigir.
2. Conferir que cada `\(` tem `\)` e cada `\[` tem `\]` (contagem casada).
3. Math conferida no sympy quando houver contas (resoluções e exemplos numéricos).
4. Abrir mentalmente o índice/seções: o guia cobre TODOS os tópicos listados na tarefa.
5. Atualizar `BACKLOG.md` (`[x]`) e o `CLAUDE.md` da matéria.

## Caminhos úteis
- EDO: `Disciplinas/BCN0405 - EDO/` (material/, guias/, listas/, CLAUDE.md)
- Discreta II: `Disciplinas/MCCC010 - Matematica Discreta II/` (idem)
- Dashboard central: `_dashboard/index.html`
