# Publicação no GitHub Pages (dashboard dinâmico)

O painel `index.html` (na raiz) é servido pelo **GitHub Pages** e lista guias, listas e
materiais **lendo o repositório ao vivo** pela API do GitHub. Não precisa rebuild nem editar
o painel: deu `push` num arquivo dentro de `Disciplinas/<matéria>/{guias,listas,material}/`,
ele aparece no painel.

- **Repositório:** https://github.com/enzovarellap/ufabc-content (público)
- **URL do painel:** https://enzovarellap.github.io/ufabc-content/

## Como ligar o Pages (uma vez só)
1. No GitHub, abra o repositório → **Settings** → **Pages**.
2. Em **Build and deployment → Source**, escolha **Deploy from a branch**.
3. Em **Branch**, selecione **`main`** e a pasta **`/ (root)`**. Clique **Save**.
4. Aguarde ~1 min. O Pages publica em `https://enzovarellap.github.io/ufabc-content/`.

> O arquivo `.nojekyll` (na raiz) garante que o Pages sirva TODOS os arquivos como estão
> (inclusive pastas que começam com `_`, como `_dashboard/`), sem processamento Jekyll.

## Como funciona o "dinâmico"
- O painel chama `https://api.github.com/repos/enzovarellap/ufabc-content/contents/<pasta>`
  para cada disciplina e monta os links automaticamente.
- Os arquivos abrem pela própria URL do Pages (HTML renderiza com MathJax; PDF abre no navegador).
- Há cache de 10 min no navegador + botão **↻ Atualizar arquivos** para forçar releitura.
- A API sem login permite ~60 chamadas/hora — suficiente para uso pessoal. Como o repo é
  **público**, não precisa de token.

## Fluxo ao criar um guia novo
1. Salve o arquivo em `Disciplinas/<matéria>/guias/` (ou `listas/`).
2. `git add` + `commit` + `push` para `main`.
3. Pronto — o painel mostra o novo arquivo sozinho (clique em ↻ se o cache ainda não expirou).

## Privacidade
O repositório e o Pages são **públicos**: qualquer pessoa com o link vê os arquivos,
incluindo os PDFs de material. Se algum dia quiser fechar, dá para tornar o repo privado
(o Pages grátis deixa de funcionar — aí volta a publicação privada via Cloudflare descrita
em `COMO-PUBLICAR.md`).
