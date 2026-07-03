# Publicação no GitHub Pages (dashboard dinâmico)

O painel `index.html` (na raiz) é servido pelo **GitHub Pages** e lista guias, listas e
materiais lendo um arquivo **`manifest.json`** (índice gerado automaticamente). Não precisa
rebuild nem editar o painel: deu `push` num arquivo dentro de
`Disciplinas/<matéria>/{guias,listas,material}/`, ele aparece no painel.

- **Repositório:** https://github.com/enzovarellap/ufabc-content (público)
- **URL do painel:** https://enzovarellap.github.io/ufabc-content/

## Como funciona (arquitetura)
1. `index.html` faz **uma** leitura de `manifest.json` e monta os cards.
   (Se o manifest faltar, cai para a API do GitHub como plano B.)
2. `scripts/gen_manifest.py` gera o `manifest.json` a partir de `git ls-files`
   (lista tudo que está versionado, em `Disciplinas/*/{guias,listas,material}`).
3. O workflow `.github/workflows/build-manifest.yml` roda esse script **a cada push na main**
   e recommita o `manifest.json` se a lista mudou (com `paths-ignore: manifest.json` para
   não entrar em laço). Isso mantém o `manifest.json` versionado no repo atualizado — útil
   pra quem abre o `index.html` localmente (`file://`), sem precisar do deploy.
4. O workflow `.github/workflows/pages.yml` (deploy em si) **gera seu próprio
   `manifest.json` na hora do build**, direto no artefato publicado — não depende do commit
   do passo 3. Por isso o site publicado nunca fica preso a um manifest desatualizado, mesmo
   que o commit automático do passo 3 ainda não tenha rodado.

> Por que não chamar a API do GitHub direto do navegador? Ela tem limite de **60 req/h** sem
> login e falha no primeiro carregamento — foi o que deixou as disciplinas vazias. O manifest
> resolve com **uma** leitura, sem limite.

## Ligar o Pages (uma vez só) — ⚠️ AÇÃO NECESSÁRIA
**03/07/2026 — mudou o modo de deploy.** O modo antigo (**Deploy from a branch**) fazia o
GitHub disparar um deployment automático a cada push na `main` — inclusive o commit
automático de `manifest.json` (ver abaixo), que chegava segundos depois do push original.
Os dois deployments corriam em paralelo e um cancelava o outro no meio, o que a API do
Pages às vezes reportava como **"Deployment failed, try again later"** (foi o que deixou
o painel desatualizado em 03/07/2026 às 17h).

Troquei para deploy via **workflow do GitHub Actions**
(`.github/workflows/pages.yml`): ele gera o `manifest.json` na hora do build (sem precisar
de commit automático) e enfileira os deployments em vez de cancelar um pelo outro.

**Passo manual (uma vez só):** Settings → **Pages** → **Build and deployment** → **Source**
→ trocar de "Deploy from a branch" para **"GitHub Actions"** → Save.
O arquivo `.nojekyll` na raiz não é mais necessário para esse modo, mas foi deixado por
segurança (não atrapalha).

## ⚠️ Permissão do GitHub Actions (uma vez só)
Para o workflow `pages.yml` poder publicar no Pages:
Settings → **Actions** → **General** → **Workflow permissions** →
confirme que está marcado **"Read and write permissions"** (mesma permissão já usada
pelo `build-manifest.yml` para recommitar o `manifest.json`).

## Fluxo ao criar um guia novo
1. Salve o arquivo em `Disciplinas/<matéria>/guias/` (ou `listas/`).
2. `commit` + `push` para `main`.
3. A Action regenera o `manifest.json`; o painel mostra o arquivo novo (clique em ↻ se precisar).

## Regenerar o manifest manualmente (opcional)
```
python scripts/gen_manifest.py
```

## Privacidade
Repositório e Pages são **públicos**: qualquer pessoa com o link vê os arquivos. Para fechar,
torne o repo privado (o Pages grátis deixa de funcionar — volta à publicação privada via
Cloudflare descrita em `COMO-PUBLICAR.md`).
