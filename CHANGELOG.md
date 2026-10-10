# Changelog

## 2.1 (2026-10-10)

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
