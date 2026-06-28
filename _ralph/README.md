# _ralph — loop de preenchimento de lacunas

Investigação de 27/06/2026 sobre **EDO** e **Matemática Discreta II**: o que ainda
falta de guia/resolução, formatado para rodar no padrão **Ralph loop** (uma tarefa por
iteração até zerar o backlog).

## Arquivos
- **`PROMPT.md`** — instruções permanentes do agente (procedimento, padrão de guia, **regras de fórmulas MathJax**, verificação).
- **`BACKLOG.md`** — lacunas priorizadas (T1…T5). Marque `[x]` ao concluir cada uma.
- **`loop.sh`** — runner: reinvoca `claude -p` lendo o `PROMPT.md` até o backlog zerar.

## Como rodar (Claude Code CLI)
```bash
cd "UFABC 2026.2"
bash _ralph/loop.sh            # roda até acabar (máx. 12 iterações)
MAX_ITERS=2 bash _ralph/loop.sh  # só 2 tarefas
```

## Backlog (resumo)
| # | Matéria | Lacuna | Prova |
|---|---|---|---|
| T1 | EDO | Resolução da **Lista 2** (modelagem, autônomas, TEU) | P1 30/06 |
| T2 | EDO | Completar **Guia 3** (modelagem + TEU, além de isóclinas/equilíbrio) | P1 30/06 |
| T3 | Discreta | Guia **grafos avançados** (euler/hamilton, matching, coloração) | P2 10/08 |
| T4 | Discreta | Guia **probabilidade / método probabilístico** | P2 10/08 |
| T5 | EDO | Guia **2ª ordem** (Wronskiano, coef. const., Euler-Cauchy, variação de parâmetros, vibrações) | P2 07/08 |

> Discreta II só tem a Lista 1 (já resolvida) — sem Lista 2 nesta rodada.
> Nesta sessão os agentes já foram disparados em paralelo para T1–T5; o loop serve para
> reexecutar/retomar qualquer item que falte ou para rodadas futuras.
