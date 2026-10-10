# Fluxo

| Momento | Comando | Saída |
|---|---|---|
| Uma vez | `/liliai-entrevista` | Instrução, contexto, `diario.json` inicial |
| Logo depois da sessão | `/liliai-sessao` + notas | `diario.json` atualizado |
| Quando algo acontecer com quem decide | `/liliai-sessao evidência: ...` | Evidência registrada |
| Toda semana | `/liliai-semana` | Atrasos, evidências da semana, pauta |
| Quando quiser ver ou mostrar | `/liliai-painel` | Painel HTML pessoal ou para compartilhar |
| Antes de compartilhar qualquer texto | `/liliai-privacidade` | Texto anonimizado |

## Regras de extração

- Uma lição por item. Toda ação tem responsável, prazo (ou vazio) e status.
- Inferência marcada como inferência. Prazo inferido fica marcado no painel.
- Ids nunca mudam depois de criados.

## Regras de contagem (calculadas pelo painel)

- Sessão: tem pelo menos uma lição ou ação.
- Atrasada: prazo passado e status diferente de Feito.
- Evidência: `Texto lido`, `Reunião com liderança` ou `Pedido da liderança`.
- Pilar: conta em quantas sessões aparecem as lições ligadas a ele.
