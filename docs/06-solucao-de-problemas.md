# Solução de problemas

| Sintoma | Causa provável | Solução |
|---|---|---|
| `/liliai` não aparece | Skills não enviadas ou não ativadas | Envie os zips de `skills/dist/` e ative. Sem Skills, use `prompts/` |
| O Claude responde de forma genérica | Conversa aberta fora do Projeto | Abra a conversa dentro do Projeto |
| O Claude ignora meus termos bloqueados | A instrução não foi colada | Cole a instrução em Configurações do projeto |
| O comando não acha o diário | `diario.json` não está no conhecimento | Envie o arquivo com esse nome exato |
| O painel mostra dados antigos | O `diario.json` não foi substituído | Substitua pelo último que o Claude devolveu |
| O painel abre em branco | JSON inválido | Peça "valide o diario.json e corrija" |
| Tenho um `diario.md` antigo | Versão anterior do kit | Rode `/liliai-sessao` com ele no Projeto: a skill converte para JSON |
| A entrevista foi interrompida | Fechei a conversa | Cole o resumo do `pausar` e diga "continue de onde parou" |
| O Claude inventou uma lição | Notas pouco claras | Peça "marque o que não tem evidência nas notas" |
| A entrevista veio sem botões | Versão do Claude sem perguntas com opções | Responda pelo número das opções |
