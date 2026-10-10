---
name: liliai-semana
description: Revisão semanal do LiliAI em dez minutos a partir do diario.json. Mostra o que vence e o que atrasou, registra evidências novas, atualiza status e prepara a pauta da próxima sessão. Use com /liliai-semana.
---

# LiliAI: revisão semanal e pauta

Leia o `diario.json` do conhecimento do Projeto. Sem diário, diga isso, sugira /liliai-sessao e pare. Use a data de hoje como referência.

## 1. Situação

Tabela `Ação | Sessão | Prazo | Situação` com:
- ações que vencem nos próximos sete dias
- ações atrasadas (prazo passado e status diferente de Feito)
- ações "A confirmar" há mais de duas semanas

Se não houver nenhuma, diga isso numa linha.

## 2. Perguntas rápidas

Com botões se a ferramenta de perguntas com opções existir, até quatro de uma vez:
1. Para cada ação da tabela: "Feito", "Ainda aberto", "Mudar prazo", "Cortar".
2. "Teve alguma evidência de visibilidade esta semana?": "Texto lido", "Reunião com liderança", "Pedido da liderança", "Nenhuma". Para cada evidência, peça uma linha de descrição.

"Cortar" muda o status para `Feito` e acrescenta " (cortada)" à descrição, para não sumir do histórico.

## 3. Leitura da semana

Um parágrafo curto respondendo:
- O que aprendi que muda o meu jeito de trabalhar na segunda-feira?
- Qual é a coisa mais importante a fazer agora? Isso vira o campo `prioridade`.

## 4. Pauta da próxima sessão

Cada item em uma linha:
- três coisas para reportar como feitas, com evidência no diário
- três perguntas para a mentoria, ligadas às perguntas em aberto e às ações travadas
- uma decisão em que preciso de ajuda, com as opções em jogo

Se não houver itens suficientes para algum grupo, diga quantos achou em vez de inventar. A pauta é escrita para sair do Projeto: em qualquer modo, use funções no lugar de nomes e não cite valores.

## 5. Saída

Se algo mudou (status, prazos, evidências, prioridade), devolva o `diario.json` completo num bloco `json`, com `prioridade` e `proximos_30_dias` atualizados, e diga para substituir o arquivo no Projeto. Se nada mudou, diga que o diário continua igual.

Feche com: "Para ver tudo num painel, rode /liliai-painel."

Regras: fatos só do diário, inferência marcada, funções no lugar de nomes no modo Anônimo, escrita direta.
