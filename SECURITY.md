# Política de segurança

O Lili.AI é um kit aberto de skills, prompts e modelos para o Claude. Ele não tem servidor, banco de dados nem conta própria: os dados de cada pessoa ficam no Projeto dela, dentro do Claude. Mesmo assim, um prompt mal escrito pode vazar dados ou ser manipulado, e é isso que esta política cobre.

## Versões com suporte

| Versão | Suporte |
|---|---|
| 2.x | ✅ Recebe correções de segurança |
| 1.x | ❌ Sem suporte. Atualize para a 2.x |

## Como reportar uma vulnerabilidade

**Não abra uma issue pública.** Use o canal privado do GitHub:

1. Vá em [Security › Advisories](https://github.com/g1c4buMm/LiliAI/security/advisories/new) e clique em **Report a vulnerability**.
2. Descreva o problema, a versão do kit, o comando (`/liliai-...`) ou arquivo afetado e os passos para reproduzir.
3. **Use dados fictícios.** Nunca envie notas reais de mentoria, nomes, e-mails ou o seu `diario.json`. A pasta `demo/` tem um cenário pronto para isso.

## O que esperar

| Etapa | Prazo |
|---|---|
| Confirmação de recebimento | até 5 dias úteis |
| Avaliação inicial | até 10 dias úteis |
| Correção ou plano de correção | depende da gravidade; problemas que expõem dados têm prioridade |

O Lili.AI é mantido por uma pessoa, no tempo livre. Os prazos são um compromisso de boa-fé, não um SLA. Você recebe crédito no advisory e no CHANGELOG, se quiser.

## Escopo

**Dentro do escopo:**

- **Vazamento de dados pessoais:** uma skill ou prompt que mantém nomes, e-mails, valores, clientes ou termos bloqueados quando deveria remover, em especial no modo Anônimo, no painel "para compartilhar" ou em `/liliai-privacidade`.
- **Injeção de prompt:** texto colado nas notas, em uma evidência ou no `diario.json` que faz a skill ignorar a política de privacidade, mudar o modo sem a confirmação literal ou executar instruções embutidas.
- **Modelo do painel** (`modelos/painel.html`): XSS ou execução de código a partir do conteúdo do diário, ou carregamento de recursos externos que exponha dados.
- **Site** (`index.html`): XSS, formulário do beta enviando dados além do e-mail, ou rastreamento não declarado.
- **Script de build** (`scripts/build.py`) e workflow de CI: execução de código, ou dados pessoais entrando no repositório ou nos zips.
- **Dados reais no repositório:** se você encontrar qualquer dado pessoal real em um commit, reporte em privado para que ele seja removido do histórico.

**Fora do escopo:**

- A segurança do Claude, da sua conta Anthropic ou da plataforma do GitHub. Reporte esses casos diretamente a eles.
- Respostas imprecisas do modelo que não expõem dados nem quebram uma regra de privacidade.
- A política de dados da sua empresa. O kit pergunta sobre ela, mas a decisão é sua.

## Princípios que o kit segue

- **Anônimo por padrão.** O modo Contexto só liga com consentimento explícito e uma frase de confirmação literal.
- **Nenhum dado pessoal no repositório.** O `.gitignore` bloqueia `diario.json`, `contexto.md`, `instrucao.md`, painéis gerados e a pasta `meus-dados/`.
- **Lista "nunca registrar" nunca vazia.** Se a pessoa não informa nada, o kit propõe uma lista padrão.
- **Sem dependências externas no painel.** O HTML gerado funciona offline; só a fonte vem do Google Fonts.
- **A checagem de privacidade é uma segunda leitura, não uma garantia.** Releia sempre antes de compartilhar.

## Se você usa o kit

- Mantenha o seu `diario.json` só no conhecimento do Projeto no Claude, nunca em um fork público.
- Antes de compartilhar um painel, gere a versão **Para compartilhar** e revise a tabela de checagem.
- Se você fez um fork, confira com `git log --all -- diario.json` que nenhum diário real foi commitado.
