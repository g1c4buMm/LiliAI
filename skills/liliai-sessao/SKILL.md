---
name: liliai-sessao
description: Registra no diario.json do LiliAI uma sessão de mentoria ou outra fonte (1:1 com a gestão, feedback formal ou informal), extrai lições, ações e evidências, revisa o plano para a meta com base no que chegou, devolve o diário e mostra o painel atualizado. Também registra evidência avulsa. Use com /liliai-sessao.
---

# LiliAI: registrar uma sessão ou outra fonte

## Usos

- **Sessão de mentoria**: `/liliai-sessao` com data, tema e as notas brutas ou a transcrição.
- **Outra fonte**: `/liliai-sessao 1:1`, `/liliai-sessao feedback` ou `/liliai-sessao fonte`, com as notas, o texto ou um arquivo anexado (avaliação em PDF, print, transcrição, e-mail).
- **Evidência avulsa**: `/liliai-sessao evidência: <o que aconteceu>`. Pule para "Evidência avulsa" no fim.

Se não vierem notas, arquivo nem evidência, peça e pare.

## Entradas

- Notas, texto ou arquivo. Data e tema: se faltarem, pergunte numa linha. Sem tema, use "Sessão geral".
- O `diario.json` do conhecimento do Projeto. Se não existir, comece do modelo vazio (`modelos/diario.json` ou o `diario.json` desta skill) e avise. Se o usuário ainda tiver um `diario.md` antigo, converta para JSON e avise. Se o diário estiver na versão 1 (sem `plano`), crie `"plano": {"atualizado_em": "", "objetivos": [], "historico": []}`, mude `versao` para 2 e avise numa linha.
- O "Modo de privacidade" da instrução do projeto. Se não houver, use Anônimo e avise numa linha.

## Passo 0. Tipo do registro

Defina o `tipo` pelo comando ou pelo conteúdo. Se não der para saber, pergunte com botões: "O que você está registrando?"

| tipo | Quando | O que procurar além do padrão |
|---|---|---|
| `Mentoria` (padrão) | sessão com a mentora ou mentor | lições, ações, perguntas |
| `1:1 com gestão` | conversa com gestor, gestora ou skip-level | expectativas para a meta, critérios de prontidão, acordos e pedidos da gestão, prazos de ciclo e calibração |
| `Feedback formal` | avaliação, ciclo de performance, 360 consolidado | pontos fortes, pontos a desenvolver, exemplos citados, expectativas para o próximo ciclo |
| `Feedback informal` | comentário de par, cliente interno ou liderança | o padrão por trás do comentário, quem deu (função) |
| `Outra fonte` | documento de expectativas do cargo, descrição de nível, conversa com RH | critérios que mudam a meta ou o prazo |

Registre também `com`: quem participou ou deu o feedback (função no modo Anônimo, nome no modo Contexto). Na Mentoria, `com` é opcional.

## Passo 1. Privacidade da entrada

Procure nas notas: nomes de pessoas e clientes, e-mails, valores em moeda, números de documento, termos bloqueados e o que estiver em "o que nunca registrar".

- **Anônimo**: mostre uma tabela `trecho | tipo | substituição` e siga com as substituições. Não repita os termos originais fora desta tabela.
- **Contexto**: mostre uma tabela `trecho | tipo | tratamento`. Dados reais ficam com o tratamento "mantido (modo Contexto)". O que estiver em "o que nunca registrar" é sempre substituído.
- **Em qualquer modo, nunca registre**: salário, bônus, remuneração e valores de reajuste; notas ou posições de ranking de outras pessoas; saúde, licenças e assuntos pessoais de qualquer pessoa. Substitua por "[assunto omitido]" e mostre na tabela. A nota ou o conceito da própria avaliação do usuário só entra se ele confirmar, com botões: "Registrar o conceito da avaliação?" (Sim / Não).

## Passo 2. Notas

Limpe o texto mantendo todas as falas. Corrija os rótulos de quem fala, remova vícios de linguagem e repetições, agrupe por tema com títulos curtos. Não resuma e não acrescente nada. Marque trechos incompreensíveis com [incompreensível]. Esse texto vai para o campo `notas` do registro. Para arquivo de avaliação, guarde só os trechos que viraram lição ou ação.

## Passo 3. Lições, ações, perguntas e evidências

- **Id do registro**: `S<data>`. Se já existir um registro com essa data, use `S<data>b`, depois `c`.
- **Lições**: uma por item, só o que está na fonte. Id: `S<data>-L1`, `-L2`... Em feedback, ponto forte e ponto a desenvolver viram lições escritas como fato: "Ponto forte reconhecido: ..." e "A desenvolver: ...".
- **Ações**: descrição, responsável, prazo (`AAAA-MM-DD` ou `""`), `prazo_inferido` e status (`Feito`, `Aberto`, `A confirmar`). Id: `S<data>-A1`... Sem prazo na fonte, use `""` e não invente. Acordos em que a gestão é responsável também viram ação, com ela como responsável.
- **Perguntas em aberto**: o que a fonte não responde.
- **Atualizações de ações antigas**: se a fonte disser que uma ação anterior foi feita ou mudou, atualize o `status` dela pelo id. Nunca mude ids existentes.
- **Evidências de visibilidade**: se a fonte mostrar que quem decide leu um texto, deu agenda ou pediu algo, proponha uma evidência com `tipo` = `Texto lido`, `Reunião com liderança` ou `Pedido da liderança`. Um 1:1 em que a gestão pede algo ligado à meta é `Pedido da liderança`.
- Marque inferências com "(inferência)". No modo Anônimo, use funções, nunca nomes. Sinalize o que não tiver evidência na fonte.

## Passo 4. Revisão do plano (todo registro, sem exceção)

O `plano` do diário é o caminho até a meta: `objetivos` com status e o `historico` do que mudou. Cada registro novo revisa o plano. É isso que faz o LiliAI aprender com o tempo.

Objetivo: `{"id": "O1", "texto": "...", "indicador": "como saber que avançou", "status": "Não iniciado|No rumo|Em risco|Concluído", "acoes": ["ids"], "evidencias": ["ids"]}`.

1. **Se o plano estiver vazio**, proponha de dois a quatro objetivos a partir da meta do `perfil`, das lições e do que a fonte disse. Status inicial: "Não iniciado", ou "No rumo" se já houver ação feita.
2. **Ligue** cada ação e evidência nova ao objetivo a que ela serve. Uma ação pode ficar sem objetivo; diga quais ficaram.
3. **Status de cada objetivo**, com o motivo em uma frase:
   - "No rumo": ações andando no prazo, ou evidência nova.
   - "Em risco": ação ligada atrasada, sinal contrário da gestão ou de feedback, ou prazo da meta apertado.
   - "Concluído": o indicador foi atingido, com fato na fonte.
4. **Objetivo novo** quando a fonte trouxer uma expectativa que nenhum objetivo cobre (comum em 1:1 e feedback). No máximo cinco objetivos que não estejam concluídos; acima disso, proponha juntar ou concluir.
5. **Conflito**: se a gestão ou um feedback disser o contrário do que a mentoria orientou, ou do que o plano assume, não escolha um lado. Aponte o conflito e acrescente uma pergunta para a próxima sessão de mentoria.
6. **Recalcule** `prioridade` e `proximos_30_dias` a partir do plano: primeiro o que está em risco, depois as ações com prazo mais próximo.
7. **Histórico**: acrescente `{"data": "<data do registro>", "origem": "<id do registro>", "mudancas": [...]}`. Cada mudança começa pelo id do objetivo ("O2: passou de No rumo para Em risco: <motivo>"), ou por "Prioridade:" ou "Próximos 30 dias:". Sem mudanças, registre "Plano confirmado: <motivo em uma frase>". Atualize `plano.atualizado_em`.

Mostre a revisão numa tabela `objetivo | antes | depois | por quê | fonte`, seguida dos objetivos novos, das ligações e dos conflitos.

## Passo 5. Métricas

- Sessão: registro do tipo Mentoria com pelo menos uma lição ou ação. Os outros tipos contam como "outras fontes".
- Ações por status, atrasadas (prazo passado e status diferente de Feito), evidências totais, objetivos por status.

Mostre uma tabela curta com os totais e confirme se a soma das ações por status bate com o total.

## Saída

1. Em tabelas curtas: privacidade, lições novas, ações novas, status alterados, evidências propostas, **revisão do plano**, métricas.
2. Peça confirmação: "Confirma? Responda ok ou corrija." Use botões se a ferramenta existir. Correções no plano entram antes de devolver o diário.
3. Após a confirmação, devolva o **`diario.json` completo**, num bloco `json`, com o registro novo no fim de `sessoes` (com `tipo` e `com`) e o `plano` revisado. Valide o JSON: aspas duplas, sem vírgula sobrando, ids únicos, todo id citado no plano existe.
4. Diga: "Substitua o diario.json no conhecimento do Projeto por esta versão. Eu não consigo gravar no seu Projeto: esse passo é seu." Se o diário estiver num documento vivo ou artefato que você consiga editar, atualize lá e diga que não há passo manual.
5. **Painel atualizado.** Pergunte, com botões se a ferramenta existir: "Quer ver o painel com este registro?" Opções: "Ver agora" (recomendado) e "Depois".
   - **Ver agora:** gere o painel pessoal com o `diario.json` que você acabou de devolver, sem esperar a troca no Projeto. Use `modelos/painel.html` do Projeto ou o `painel.html` desta skill, copie o modelo inteiro e troque só o bloco `<script type="application/json" id="dados">` por `{"exibicao": {"hoje": "AAAA-MM-DD", "audiencia": "pessoal", "exemplo": false}, "diario": {...}}`. Publique como página ou artefato, se puder; senão, entregue o HTML completo num bloco de código.
   - **Depois:** diga "Quando quiser ver o painel, rode /liliai-painel."
6. Feche com uma linha: "Próximo passo: substituir o diario.json no Projeto. Teve 1:1 ou feedback? /liliai-sessao 1:1 ou /liliai-sessao feedback. Na revisão da semana, /liliai-semana."

## Evidência avulsa

1. Leia a descrição depois de "evidência:". Classifique o `tipo`. Se não der para classificar, pergunte com botões.
2. Aplique o modo de privacidade à descrição.
3. Monte `{"id": "E<próximo número>", "data": "<hoje>", "tipo": "...", "descricao": "...", "quem": "<função ou nome, conforme o modo>", "sessao": "<id do registro mais recente ou vazio>"}`.
4. Ligue a evidência ao objetivo do plano a que ela serve. Se ela mudar o status de um objetivo, acrescente ao histórico `{"data": "<hoje>", "origem": "<id da evidência>", "mudancas": ["O1: ..."]}`.
5. Mostre a evidência e a mudança no plano, peça confirmação e devolva o `diario.json` completo.
