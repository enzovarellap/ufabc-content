# Como publicar a Central de Estudos (privado, só você) — Cloudflare

Sua pasta `publish/` já é um **site pronto**: o painel (`index.html`) na raiz,
os 4 guias, as listas, os PDFs das aulas e o suporte a "instalar no celular" (PWA).
Falta só colocar no ar — de graça e protegido por login.

**Resultado final:** uma URL tipo `estudos-ufabc.pages.dev` que abre o seu painel,
pede seu e-mail + um código, e só **você** entra. Funciona no navegador e no celular.

> Tempo: ~10 minutos, uma vez só. Depois, atualizar leva 1 minuto.

---

## Parte 1 — Colocar o site no ar (Cloudflare Pages)

1. Crie uma conta grátis em **https://dash.cloudflare.com/sign-up** (e confirme o e-mail).
2. No painel da Cloudflare, vá em **Workers & Pages** → **Create application** →
   aba **Pages** → **Upload assets** (também aparece como *"Drag and drop"*).
3. Dê um nome ao projeto, ex: **`estudos-ufabc`** (vira o endereço `estudos-ufabc.pages.dev`).
4. **Arraste** para a janela de upload a **pasta `publish` inteira**
   (em `Documentos\Claude\Projects\UFABC 2026.2\publish`). Dragar a pasta é o método mais
   confiável. *(O `publish.zip` é só um atalho opcional — se for usá-lo, garanta que é a
   versão mais recente; gere de novo com `python build-site.py` quando em dúvida.)*
5. Clique **Save and Deploy**. Em ~30s o site está no ar em `https://estudos-ufabc.pages.dev`.

✅ Teste a URL: o painel deve abrir e os guias devem funcionar.
   *(Neste ponto o link ainda é público — a Parte 2 fecha o acesso.)*

---

## Parte 2 — Trancar para só você entrar (Cloudflare Access — login por código)

Isso usa o **Cloudflare Access** (plano grátis, até 50 usuários). Você digita seu
e-mail no site, recebe um **código de uso único** no Gmail e entra. Ninguém sem
o seu e-mail passa.

1. No menu da Cloudflare, abra **Zero Trust** (pode aparecer como *Cloudflare One*).
   Na primeira vez ele pede pra escolher um nome de time e o **plano Free** — escolha Free.
2. Vá em **Settings → Authentication → Login methods** e confirme que
   **One-time PIN** está **ativado** (vem ativado por padrão).
3. Vá em **Access → Applications → Add an application → Self-hosted**.
4. Configure:
   - **Application name:** `Estudos UFABC`
   - **Session duration:** `1 month` (pra não pedir código toda hora no celular)
   - **Application domain / subdomain:** `estudos-ufabc.pages.dev`
     *(coloque exatamente o domínio do seu projeto Pages, sem caminho)*
   - Avance (**Next**).
5. Crie a **política (policy)**:
   - **Policy name:** `Só o Enzo`
   - **Action:** `Allow`
   - **Include → Emails →** `enzovpastore@gmail.com`
   - Salve (**Next → Add application**).

✅ Pronto. Agora, ao abrir `estudos-ufabc.pages.dev`, aparece a tela da Cloudflare
pedindo o e-mail; com seu e-mail você recebe o código e entra. Com o e-mail "1 mês"
de sessão, no celular você praticamente não digita código de novo.

> **Atalho:** o próprio projeto em **Pages → Settings** tem uma opção de
> **Access Policy** que faz o mesmo. Se ela estiver disponível pra produção, dá pra
> ativar por ali em vez de criar a aplicação manualmente.

---

## Parte 3 — Instalar no celular (vira "app" na tela inicial)

Depois de logar uma vez no celular:

- **iPhone (Safari):** botão **Compartilhar** → **Adicionar à Tela de Início**.
- **Android (Chrome):** menu **⋮** → **Adicionar à tela inicial / Instalar app**.

Abre em tela cheia, com ícone próprio, como um aplicativo. Os guias que você já
abriu ficam disponíveis **mesmo offline** (bom pra estudar no fim de semana sem depender da rede).

---

## Parte 4 — Atualizar quando eu gerar guias novos

O site é uma "foto" da pasta. Quando surgir guia novo, é só **regerar e reenviar**:

1. **Regerar:** rodar `python build-site.py` (eu faço isso pra você na nossa conversa,
   ou você roda na pasta do projeto). Isso atualiza `publish/` e o `publish.zip`.
2. **Reenviar:** na Cloudflare, abra o projeto **estudos-ufabc** → **Create deployment**
   (ou **Upload**) → arraste o `publish.zip` novo → **Deploy**.

O login e a proteção continuam valendo — você só troca o conteúdo.

> **Mais pra frente (opcional):** dá pra automatizar isso com o utilitário
> `wrangler` (1 comando publica tudo), eliminando o arrastar-e-soltar. Quando quiser,
> me peça que eu deixo configurado.

---

### Por que essa solução (e não Notion)
Os guias usam HTML interativo + MathJax (fórmulas), quizzes e tema próprio.
No Notion isso vira texto "achatado" e você perde a interatividade — exatamente o que
te incomodava. Publicando como site, **mantém 100%** dos guias e ganha acesso fácil no
celular. O Notion continua ótimo como **segundo cérebro** (anotações pesquisáveis),
em paralelo, não como visualizador dos guias.
