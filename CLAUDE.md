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
| 15/06 (seg) | Modelagem e Controle | Prova 1 |
| 29/06 (seg) | Matemática Discreta II | Prova 1 (Sem. 1–4) |
| 30/06 (ter) | EDO | Prova 1 |
| 03/08 (seg) | Modelagem e Controle | Prova 2 |
| 07/08 (sex) | EDO | Prova 2 |
| 10/08 (seg) | Matemática Discreta II | Prova 2 (Sem. 5–11) |
| 11/08 (ter) | Métodos Experimentais (NB2-SA) | Prova individual |
| 14/08 (sex) | Práticas de Ensino de Química I | Prova escrita individual |

Substitutivas/REC: EDO SUB 11/08, REC 18/08 · Discreta SUB 12/08, REC 19/08 ·
Modelagem SUB 10/08 · Métodos SUB 13/08, REC 19/08 · Química REC 19–21/08.
ESMA001 (projeto): entregas por aula (Relatório Final ≈13/08) — **datas exatas a confirmar**.

> ⚠️ **Práticas de Química** proíbe uso de IA em atividades avaliadas — guias só para estudo, nunca para produzir entregas.
> **Professores:** EDO=Edson A. Arrázola · Discreta II=Renzo G. Gómez Diaz · Modelagem=Victor A. F. de Campos · Métodos(NB2)=Daniel Z. de Flório · ESMA001=Humberto de Paiva Jr. · Química=Rafaela Valero.

## Disciplinas (6)
| Sigla | Nome | Pasta |
|---|---|---|
| BCN0405-15 | Introdução às Equações Diferenciais Ordinárias | `Disciplinas/BCN0405 - EDO` |
| ESTO017-17 | Métodos Experimentais em Engenharia | `Disciplinas/ESTO017 - Metodos Experimentais` |
| ESMA001-23 | Soluções para Desafios em Engenharia | `Disciplinas/ESMA001 - Solucoes Desafios Eng` |
| NHLQ002-22 | Práticas de Ensino de Química I | `Disciplinas/NHLQ002 - Praticas Ensino Quimica I` |
| MCCC010-23 | Matemática Discreta II | `Disciplinas/MCCC010 - Matematica Discreta II` |
| ESTA020-17 | Modelagem e Controle | `Disciplinas/ESTA020 - Modelagem e Controle` |

## Grade de horários (noturno, Santo André)
| Dia | 19:00–21:00 | 21:00–23:00 |
|---|---|---|
| Segunda | Matemática Discreta II | Modelagem e Controle |
| Terça | Métodos Experimentais | EDO |
| Quarta | Práticas Ens. Química I *(quinzenal I)* | Matemática Discreta II |
| Quinta | Soluções p/ Desafios em Eng. | Métodos Experimentais |
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
- Passo a passo completo em `COMO-PUBLICAR.md`. (Futuro opcional: automatizar com `wrangler`.)

## Perfil de estudo do Enzo (contexto que guia tudo)
- **Tempo:** ~5h/semana, concentradas nos **fins de semana**.
- **Aulas:** em sua maioria **não serão aproveitadas por inteiro** → os guias são a
  **fonte principal de aprendizado** (ensinam do zero, não pressupõem a aula).
- **Meta:** **passar com tranquilidade** (não mira A) → calibrar ao essencial/cobrado.
- **Como aprende:** lendo resumo + fazendo exercícios + **ensinando (Feynman)**.
- **Prioridades:** **Matemática Discreta II** e **EDO** (as mais difíceis).
- **Foco do material:** resumos teóricos enxutos + listas resolvidas passo a passo + simulados.
- **Provas antigas:** não tem → buscar exemplos similares na web para montar simulados.
- **Apoio extra:** projeto da **ESMA001** e **relatórios de prática** de Métodos Experimentais.

## Ferramentas conectadas
- **Google Calendar** — aulas recorrentes, provas, prazos e **revisões espaçadas**.
  É também o único lugar de "tarefas" (Enzo não usa app de tarefas separado).
- **Notion** — segundo cérebro: resumos/anotações pesquisáveis.
- **Skills:** `university-study-guide` (guias HTML), `calculus-problem-set-solver`
  (listas EDO/Discreta), `pdf`/`pdf-viewer` (extrair planos/listas),
  `data:create-viz` (gráficos/regressão p/ Métodos Exp.), `theme-factory`,
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
7. **Projeto/relatórios:** apoiar ESMA001 (cronograma + entregas) e relatórios de
   Métodos Experimentais (`doc-coauthoring` + `data:create-viz`).

> **Regra permanente:** sempre transcrever neste CLAUDE.md o contexto novo que surgir
> nas conversas (decisões, preferências, mudanças de escopo), para servir de steering file.
