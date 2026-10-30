# Changelog

## 2.3 (2026-10-30)

- **Plano que aprende**: o `diario.json` (versão 2) ganha o bloco `plano`, com objetivos para a meta, indicador, status (Não iniciado, No rumo, Em risco, Concluído), ações e evidências ligadas, e o histórico de cada mudança com origem e motivo.
- **Revisão do plano a cada registro**: o `/liliai-sessao` liga ações e evidências aos objetivos, muda status com o motivo, cria objetivo novo quando a fonte traz uma expectativa nova e aponta conflitos entre gestão e mentoria.
- **Outras fontes**: `/liliai-sessao 1:1`, `/liliai-sessao feedback` e `/liliai-sessao fonte` registram 1:1 com a gestão, avaliações, feedbacks e documentos de expectativa, por texto ou arquivo. Salário, bônus e assuntos pessoais nunca são registrados.
- **Plano inicial na entrevista**: de dois a três objetivos a partir da meta, do que a mentoria deve mudar e de quem decide.
- **Painel**: seção "Plano para a meta" com o status de cada objetivo e "Como o plano mudou"; selo de origem nos compromissos e no histórico.
- **`/liliai-semana`** mostra os objetivos em risco e pergunta se houve 1:1 ou feedback. **`/liliai-painel`** para compartilhar deixa 1:1 e feedbacks de fora por padrão.
- Diários da versão 1 continuam funcionando: o plano nasce no próximo `/liliai-sessao`.
- Demo: novo ato 3b com `demo/notas-1a1.txt`.

## 2.2 (2026-10-10)

- **Primeiro painel no fim da entrevista**: o `/liliai-entrevista` gera o painel na hora, a partir do `diario.json` inicial, mesmo com poucas respostas.
- **Bloco "Próximos passos"** no fim da entrevista: o que salvar no Projeto, onde colar a instrução e o comando de cada momento (sessão, semana, painel). Deixa claro que salvar arquivos no Projeto é um passo da pessoa.
- **Painel depois de cada sessão**: o `/liliai-sessao` oferece "Ver agora" e gera o painel com o diário novo, sem esperar a troca no Projeto.
- Vídeos com áudio em 48 kHz.
- Pitch do hackathon em `demo/hackathon/`: deck de 3 slides com cronômetro, roteiro em pop-up e `apresentar.command`.

## 2.1 (2026-10-10)

- **Timelapse da instalação** (`demo/timelapse.html`): 14 cenas da instalação do zero até o painel, com relógio acelerado e fala de cada passo.
- **Modo da entrevista como escolha do usuário**: nova pergunta P2, com botões "Rápido" e "Completo". O questionário passa a ter 38 perguntas.
- **Completar depois**: no fim do modo rápido, o Claude oferece responder as 27 restantes agora ou depois. "completar entrevista" retoma só as pendentes.

## 2.0 (2026-10-10)

- **Cinco comandos** no lugar de oito: `/liliai-preparar` entrou no `/liliai-semana`; `/liliai-pilares` e `/liliai-dossie` entraram no `/liliai-painel` (versão "para compartilhar").
- **`diario.json`** como fonte única, com ids estáveis para sessões, lições e ações. O `diario.md` antigo é convertido pelo `/liliai-sessao`.
- **Evidências de visibilidade**: texto lido, reunião com liderança, pedido da liderança. Registro avulso com `/liliai-sessao evidência: ...` e bloco próprio no painel.
- **Entrevista em modo rápido** (10 perguntas). I1 vazio ganha um padrão proposto. A entrevista entrega o `diario.json` inicial.
- **Pilares por id**, não por texto.
- **`scripts/build.py`**: gera prompts a partir das skills, anexos, zips e painéis de exemplo; valida diários; confere a documentação. CI com `--check`.
- **Exemplos** (`exemplos/`): diário vazio, normal e com atrasos, com painéis renderizados.
- **Demo** (`demo/`): cenário fictício e roteiro de 20 minutos.
- **`.gitignore`** bloqueia `diario.json`, `contexto.md` e painéis gerados.
- Telas novas dos passos 4, 7 e 11.

## 1.0

- Primeira versão: oito comandos, diário em Markdown, painel HTML, privacidade com consentimento.
