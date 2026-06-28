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
   não entrar em laço). Resultado: o índice se mantém sozinho.

> Por que não chamar a API do GitHub direto do navegador? Ela tem limite de **60 req/h** sem
> login e falha no primeiro carregamento — foi o que deixou as disciplinas vazias. O manifest
> resolve com **uma** leitura, sem limite.

## Ligar o Pages (uma vez só) — já feito
Settings → Pages → Source **Deploy from a branch** → Branch **main** / **/(root)** → Save.
O arquivo `.nojekyll` na raiz garante que tudo (inclusive pastas com `_`) seja servido como está.

## ⚠️ Permissão do GitHub Actions (uma vez só)
Para o workflow conseguir recommitar o `manifest.json`:
Settings → **Actions** → **General** → **Workflow permissions** →
marcar **“Read and write permissions”** → Save.
(Se não marcar, o painel ainda funciona com o `manifest.json` versionado; só não se
atualiza sozinho nos próximos pushes.)

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
