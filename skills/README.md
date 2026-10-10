# Skills: o LiliAI por comando `/`

Cinco comandos cobrem o ciclo inteiro. Digite `/` na conversa, escolha o comando e cole o que ele pedir.

| Comando | Quando usar | O que entrega |
|---|---|---|
| `/liliai-entrevista` | Uma vez, no começo | Instrução do projeto, contexto e `diario.json` inicial |
| `/liliai-sessao` | Depois de cada sessão, com as notas. Ou `evidência: ...` a qualquer momento | `diario.json` atualizado e métricas |
| `/liliai-semana` | Toda semana | O que vence e atrasou, evidências da semana, pauta da próxima sessão |
| `/liliai-painel` | Quando quiser ver tudo, ou mostrar para alguém | Painel HTML pessoal ou anonimizado para compartilhar |
| `/liliai-privacidade` | Antes de compartilhar qualquer texto | Texto checado e anonimizado |

## Instalar

1. Baixe os arquivos `.zip` da pasta `skills/dist/`, um por comando.
2. No Claude, abra **Configurações** e a área de **Skills** (em Capabilities na maioria dos planos). Envie cada zip.
3. Ative as skills. Numa conversa dentro do seu Projeto, digite `/liliai` para ver os comandos.

Os nomes dos menus podem variar conforme o plano. Sem Skills no plano, use os prompts da pasta `prompts/`: são gerados destas skills e dão o mesmo resultado.

## Onde ficam os dados

As skills não guardam nada. O diário é o `diario.json` no conhecimento do seu Projeto. Use os comandos dentro do Projeto para o Claude encontrar o diário e a instrução.

## Editar

Cada pasta tem um `SKILL.md`, que é a fonte única. Depois de editar, rode `python3 scripts/build.py`: ele atualiza os prompts, os anexos e os zips, e confere se a documentação cita todos os comandos. Mantenha o `name` no topo do arquivo igual ao nome da pasta.
