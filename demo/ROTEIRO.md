# Demo LiliAI: roteiro de 20 minutos

Uma demonstração de ponta a ponta com um cenário fictício: Rafa Moura, especialista sênior de dados, na terceira sessão de mentoria. A plateia vê o ciclo completo: a entrevista, o registro de uma sessão, uma evidência de visibilidade, a revisão semanal, o painel pessoal, o painel para compartilhar e a checagem de privacidade.

**Tudo na pasta `demo/` é fictício.** Pessoas, empresas, clientes, valores e e-mails foram inventados.

## Arquivos da demo

| Arquivo | Para quê |
|---|---|
| `abertura.html` | Deck de 18 slides, cerca de 10 minutos: o problema, a jornada completa do Rafa no agente, o painel e a chamada para ação. Fala de cada slide na tecla N |
| `timelapse.html` | Timelapse da instalação do zero: 14 cenas, cerca de 80 segundos, com relógio acelerado e a fala de cada passo. Toca sozinho; espaço pausa, setas navegam, N mostra a fala |
| `persona.md` | Quem é o Rafa e as respostas da entrevista |
| `instrucao-demo.md` | Instrução do projeto pronta para colar |
| `diario-inicio.json` | Diário com as duas primeiras sessões e uma ação atrasada |
| `notas-sessao-3.txt` | Notas brutas da terceira sessão, com nome, valor, e-mail e termo bloqueado de propósito |
| `evidencia.txt` | Uma evidência avulsa para registrar |
| `post-linkedin.txt` | Um post com dados sensíveis para a checagem de privacidade |
| `painel-inicio.html` | Painel antes da sessão 3 |
| `painel-final.html` | Painel esperado depois da demo, versão pessoal (plano B) |
| `painel-final-compartilhar.html` | Painel esperado, versão anonimizada (plano B) |

## Como mostrar a instalação

Antes ou depois do deck, toque o `timelapse.html` em tela cheia (tecla F). Ele mostra a instalação do zero em cerca de 80 segundos, do download no GitHub até o painel, com um relógio que chega a 12m30s. Para narrar no seu ritmo, pause com espaço e avance com as setas; a tecla N mostra a fala de cada cena.

## Dois formatos

| Formato | Duração | Quando usar |
|---|---|---|
| **Só o deck** | 10 min | Pouco tempo, internet instável ou plateia grande. O deck mostra a jornada inteira do Rafa em telas simuladas e termina no painel e no QR code |
| **Deck e ao vivo** | 25 min | Grupo pequeno e curioso. Use os slides 1 a 8 como abertura, faça os atos 1 a 7 ao vivo e volte ao deck para os slides 17 e 18 (antes e depois, chamada para ação) |

Para o formato "só o deck", a preparação abaixo é dispensável: basta abrir `abertura.html`.

## Preparação para o formato ao vivo (na véspera, 15 minutos)

1. **Instale as 5 skills** de `skills/dist/` na conta que vai apresentar. Teste digitando `/liliai`.
2. **Crie um Projeto** chamado "Demo · Mentoria do Rafa".
3. **Envie ao conhecimento do Projeto:**
   - `onboarding/questionario.md`
   - `modelos/painel.html`
   - `demo/diario-inicio.json`, **renomeado para `diario.json`**
4. **Cole a instrução** de `demo/instrucao-demo.md` em Configurações do projeto › Instruções.
5. **Ensaie uma vez** os atos 3 a 7, numa conversa que você apaga depois. Depois do ensaio, volte o `diario.json` para a versão do `diario-inicio.json`.
6. **Deixe abertos no navegador:** `demo/abertura.html`, `demo/painel-inicio.html`, `demo/painel-final.html`, `demo/painel-final-compartilhar.html` e a página do kit (`index.html`).
7. **Datas:** o cenário funciona até 22/10/2026. Depois disso, os prazos de 23/10 e 28/10 aparecem como atrasados. Para apresentar mais tarde, troque as datas em `notas-sessao-3.txt` ("dia 23", "dia 28", "dia 30") por datas futuras.

## Roteiro

| Ato | Tempo | O que você faz | O que a plateia vê |
|---|---|---|---|
| 0 | 2 min | Deck `abertura.html` | O problema, a solução e a agenda |
| 1 | 4 min | `/liliai-entrevista` em modo rápido | Botões, consentimento e checagem de política |
| 2 | 1 min | Mostra o painel do início | Onde o Rafa está depois de duas sessões |
| 3 | 5 min | `/liliai-sessao` com as notas da sessão 3 | Privacidade, lições, ações, evidência detectada |
| 4 | 1 min | Evidência avulsa | Registro em uma linha |
| 5 | 3 min | `/liliai-semana` | Atraso, botões de status, pauta da próxima sessão |
| 6 | 3 min | `/liliai-painel` pessoal e para compartilhar | O mesmo diário, com e sem nomes |
| 7 | 1 min | `/liliai-privacidade` com o post | Texto reescrito sem dados sensíveis |
| 8 | 1 min | Fecha com o caminho para adotar | Link do repositório |

### Ato 0. Abertura (2 min)

Abra `demo/abertura.html` no navegador e aperte **F** para tela cheia. Avance com as setas ou com um clique. Aperte **N** para ver a fala de cada slide. O último slide apresenta o Rafa e a agenda da demo.

Se preferir abrir sem slides, use esta fala:

**Fale:** "Toda sessão de mentoria termina com três palavras no caderno. Duas semanas depois, a gente lembra de 'algo sobre visibilidade'. O LiliAI é um kit de comandos para o Claude que transforma cada sessão em lições, ações com prazo e evidências de que o trabalho chegou em quem decide. Sem código, e privado por padrão."

### Ato 1. Entrevista em modo rápido (4 min)

1. Abra uma **conversa nova dentro do Projeto** e digite `/liliai-entrevista`.
2. Na **P1**, clique em **Sim, modo Contexto**.
   **Fale:** "A primeira pergunta é sobre privacidade, com sim ou não explícito. O padrão é anônimo. Eu escolho Contexto para mostrar depois como os nomes ficam aqui dentro e somem quando eu compartilho."
3. Escolha **Rápido** e responda pelos botões, usando a tabela de `persona.md`.
4. No **H3**, escolha "Permitido com ferramentas aprovadas". O Claude pergunta se ele é uma ferramenta aprovada. Responda **Sim**.
   **Fale:** "Se a política da empresa contradisser o modo, ele volta para anônimo sozinho."
5. No **I1**, responda **Nenhum**. O Claude propõe um padrão (documentos internos, credenciais, dados de terceiros). Aceite.
6. Mostre o que sai: contexto, instrução, termos bloqueados, `diario.json` inicial, o primeiro painel já aberto e o bloco **Próximos passos**.
   **Fale:** "Em cinco minutos, o Claude conhece a pessoa, a meta, a política da empresa e o que nunca pode ser registrado."
7. **Não salve nada deste ato.** O Projeto já tem a instrução e o diário prontos para o resto da demo.

### Ato 2. Avançar o filme (1 min)

Abra `demo/painel-inicio.html`.

**Fale:** "Vamos avançar duas sessões. O Rafa já tem duas sessões registradas, uma evidência, porque a gestora leu o resumo dele, e uma ação atrasada: a conversa com o time de risco."

### Ato 3. Registrar a sessão 3 (5 min)

1. Abra uma **conversa nova no Projeto**.
2. Cole o conteúdo inteiro de `demo/notas-sessao-3.txt`. Ele já começa com `/liliai-sessao`.
3. Mostre, na resposta:
   - **Tabela de privacidade:** nomes mantidos (modo Contexto), o e-mail substituído (está em "nunca registrar") e o alerta do termo bloqueado "Banco Lumen".
   - **Lições e ações** com ids, e prazos de 23/10 e 28/10 tirados das notas.
   - **Ação antiga:** a conversa com o time de risco continua aberta e atrasada.
   - **Evidência detectada:** "Marcos pediu a apresentação no comitê" vira `Pedido da liderança`.
   **Fale:** "As ações medem o esforço. As evidências medem o que mudou em quem decide. É isso que conta numa promoção."
4. Responda **ok**. O Claude devolve o `diario.json` completo.
5. **Substitua o `diario.json`** no conhecimento do Projeto. Faça isso ao vivo: leva dez segundos.
   **Fale:** "É o único passo manual do ciclo."

### Ato 4. Evidência avulsa (1 min)

Na mesma conversa, cole `demo/evidencia.txt`. Confirme e substitua o diário de novo.

**Fale:** "Aconteceu algo no corredor? Uma linha e está registrado."

### Ato 5. Revisão semanal (3 min)

1. Conversa nova no Projeto: `/liliai-semana`.
2. Mostre a tabela: a conversa com o time de risco aparece **atrasada**.
3. Nos botões, marque essa ação como **Ainda aberto** e responda "Nenhuma" para evidências da semana.
4. Mostre a **pauta da próxima sessão**: três entregas, três perguntas e uma decisão.
   **Fale:** "Dez minutos na sexta, e eu chego na próxima sessão com pauta."

### Ato 6. Painel pessoal e para compartilhar (3 min)

1. `/liliai-painel` e escolha **Para mim**. Abra o painel gerado.
   **Mostre:** os números no topo, o bloco **Visibilidade com quem decide**, os compromissos com o filtro **Atrasadas**, os pilares e o histórico com as notas.
2. `/liliai-painel` de novo e escolha **Para compartilhar**.
   **Mostre lado a lado:** "Júlia" virou "Gestora direta", "Banco Lumen" virou "Cliente A", as notas sumiram e a tabela de checagem apareceu.
   **Fale:** "O mesmo diário. Para mim, com nomes. Para a mentora ou o gestor, anonimizado."

### Ato 7. Checagem de privacidade (1 min)

Cole `demo/post-linkedin.txt`. Mostre a tabela com nome, empresa, cliente, valor e e-mail, e o post reescrito.

**Fale:** "Antes de qualquer coisa sair daqui, uma segunda leitura. Não é garantia; eu sempre releio."

### Ato 8. Como adotar (1 min)

Abra a página do kit.

**Fale:** "São 30 minutos para montar: instalar 5 skills, criar um Projeto, fazer a entrevista. Depois, dez minutos por sessão. O kit é aberto, e os dados ficam no Projeto de cada um, nunca no repositório."

## Plano B

| Se acontecer | Faça |
|---|---|
| `/liliai` não aparece | Use os prompts da pasta `prompts/`: copie o bloco e cole na conversa |
| O Claude demora ou erra o JSON | Mostre `demo/painel-final.html` e diga "é isto que sai" |
| O painel não abre como página | Abra `demo/painel-final.html` e `demo/painel-final-compartilhar.html` no navegador |
| A entrevista se alonga | Pare depois da P1 e da checagem do H3; o resto é igual |
| Internet cai | Os três painéis em HTML funcionam offline (só a fonte muda) |

## Perguntas que costumam aparecer

| Pergunta | Resposta curta |
|---|---|
| Meus dados vão para o GitHub? | Não. O repositório só tem o kit. `diario.json` está no `.gitignore` |
| Preciso saber programar? | Não. São comandos e prompts |
| E se meu plano não tiver Skills? | Os prompts da pasta `prompts/` dão o mesmo resultado |
| Posso usar sem nomes reais? | Sim. É o padrão: modo Anônimo |
| A checagem de privacidade é garantida? | Não. É uma segunda leitura feita por um modelo. Releia sempre |
| Funciona no celular? | Sim, em qualquer lugar onde o Claude funcione |

## Depois da demo

Apague o Projeto "Demo · Mentoria do Rafa", ou volte o `diario.json` para o `diario-inicio.json` para a próxima apresentação.
