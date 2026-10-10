# Prompt 01. Registrar uma sessão

Equivale ao comando `/liliai-sessao`. Registra uma sessão de mentoria no diario.json do LiliAI. Limpa as notas, extrai lições, ações e evidências, atualiza status, conta métricas e devolve o diário. Também registra evidência avulsa. Use com /liliai-sessao.

Copie o bloco abaixo e cole numa conversa dentro do seu Projeto. Onde o texto disser "esta skill", leia "este prompt".

````text
# LiliAI: registrar uma sessão

## Dois usos

- **Sessão completa**: `/liliai-sessao` com data, tema e as notas brutas ou a transcrição.
- **Evidência avulsa**: `/liliai-sessao evidência: <o que aconteceu>`. Pule para "Evidência avulsa" no fim.

Se não vierem notas nem evidência, peça e pare.

## Entradas

- Notas brutas da sessão. Data e tema: se faltarem, pergunte numa linha. Sem tema, use "Sessão geral".
- O `diario.json` do conhecimento do Projeto. Se não existir, comece do modelo vazio (`modelos/diario.json` ou o `diario.json` desta skill) e avise. Se o usuário ainda tiver um `diario.md` antigo, converta para JSON e avise.
- O "Modo de privacidade" da instrução do projeto. Se não houver, use Anônimo e avise numa linha.

## Passo 0. Privacidade da entrada

Procure nas notas: nomes de pessoas e clientes, e-mails, valores em moeda, números de documento, termos bloqueados e o que estiver em "o que nunca registrar".

- **Anônimo**: mostre uma tabela `trecho | tipo | substituição` e siga com as substituições. Não repita os termos originais fora desta tabela.
- **Contexto**: mostre uma tabela `trecho | tipo | tratamento`. Dados reais ficam com o tratamento "mantido (modo Contexto)". O que estiver em "o que nunca registrar" é sempre substituído.

## Passo 1. Notas

Limpe o texto mantendo todas as falas. Corrija os rótulos de quem fala, remova vícios de linguagem e repetições, agrupe por tema com títulos curtos. Não resuma e não acrescente nada. Marque trechos incompreensíveis com [incompreensível]. Esse texto vai para o campo `notas` da sessão.

## Passo 2. Lições, ações, perguntas e evidências

- **Lições**: uma por item, só o que está nas notas. Id: `S<data>-L1`, `-L2`...
- **Ações**: descrição, responsável, prazo (`AAAA-MM-DD` ou `""`), `prazo_inferido` e status (`Feito`, `Aberto`, `A confirmar`). Id: `S<data>-A1`... Sem prazo nas notas, use `""` e não invente.
- **Perguntas em aberto**: o que as notas não respondem.
- **Atualizações de ações antigas**: se as notas disserem que uma ação anterior foi feita ou mudou, atualize o `status` dela pelo id. Nunca mude ids existentes.
- **Evidências de visibilidade**: se as notas mostrarem que quem decide leu um texto, deu agenda ou pediu algo, proponha uma evidência com `tipo` = `Texto lido`, `Reunião com liderança` ou `Pedido da liderança`.
- Marque inferências com "(inferência)". No modo Anônimo, use funções, nunca nomes. Sinalize o que não tiver evidência nas notas.

## Passo 3. Métricas

- Sessão: tem pelo menos uma lição ou ação.
- Ações por status, atrasadas (prazo passado e status diferente de Feito), evidências totais.

Mostre uma tabela curta com os totais e confirme se a soma das ações por status bate com o total.

## Saída

1. Em tabelas curtas: privacidade, lições novas, ações novas, status alterados, evidências propostas, métricas.
2. Peça confirmação: "Confirma? Responda ok ou corrija." Use botões se a ferramenta existir.
3. Após a confirmação, devolva o **`diario.json` completo**, num bloco `json`, com a sessão nova no fim de `sessoes`. Recalcule `prioridade` e `proximos_30_dias` a partir das ações abertas, atrasadas e com prazo mais próximo. Valide o JSON: aspas duplas, sem vírgula sobrando, ids únicos.
4. Diga: "Substitua o diario.json no conhecimento do Projeto por esta versão." Se o diário estiver num documento vivo ou artefato que você consiga editar, atualize lá e diga que não há passo manual.

## Evidência avulsa

1. Leia a descrição depois de "evidência:". Classifique o `tipo`. Se não der para classificar, pergunte com botões.
2. Aplique o modo de privacidade à descrição.
3. Monte `{"id": "E<próximo número>", "data": "<hoje>", "tipo": "...", "descricao": "...", "quem": "<função ou nome, conforme o modo>", "sessao": "<id da sessão mais recente ou vazio>"}`.
4. Mostre a evidência, peça confirmação e devolva o `diario.json` completo.
````
