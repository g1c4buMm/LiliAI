# Onboarding

A entrevista tem 37 perguntas em 11 blocos (0 e A a J), em dois modos:

| Modo | Perguntas | Tempo |
|---|---|---|
| **Rápido** (recomendado) | P1, A1, A2, B1, B2, C1, C3, D1, H3, I1 | cerca de 5 minutos |
| **Completo** | Todas | 20 a 30 minutos |

A P1 é o consentimento de privacidade: sim ou não. Veja `docs/04-privacidade.md`.

## Como fazer

1. Tenha `onboarding/questionario.md` no conhecimento do Projeto.
2. Digite `/liliai-entrevista` numa conversa do Projeto (ou cole `prompts/00-entrevista.md`).
3. Clique nos botões ou escreva no campo livre.

## Controles na conversa

| Você escreve | O Claude faz |
|---|---|
| `A3 ?` | Mostra o exemplo e o motivo da pergunta |
| `pular` | Pula uma pergunta opcional |
| `pausar` | Resume o que já foi respondido para você retomar depois |
| `refazer` | Recomeça |

## Travas

- I1 vazio ganha um padrão proposto: documentos internos, credenciais, dados pessoais de terceiros, números de contrato.
- Modo Contexto com política contraditória no H3 volta para Anônimo.

## Saídas

1. `contexto.md`, com as respostas e o consentimento.
2. Instrução do projeto.
3. Termos bloqueados.
4. `diario.json` inicial, com o perfil preenchido.

## Adaptando as perguntas

Edite `onboarding/questionario.md` e rode `python3 scripts/build.py` para atualizar a cópia dentro da skill. Mantenha os ids estáveis: a entrevista usa P1, A1, A2, A4, B1, B2, C1, C2, C3, D1, G2, G3, G4, H3, I1 e I2.
