# Montar o Projeto

## 1. Pegue o kit

No GitHub, **Code > Download ZIP** e descompacte.

## 2. Instale as skills (recomendado)

Envie os cinco zips de `skills/dist/` em Configurações, na área de Skills. Teste digitando `/liliai`. Detalhes em `skills/README.md`. Sem Skills no plano, use os prompts de `prompts/`.

## 3. Crie o Projeto

No Claude, **Projetos > Novo projeto**. Nome sugerido: o da sua meta.

## 4. Envie os arquivos de apoio

Em **Conhecimento do projeto**, adicione:

- `onboarding/questionario.md`
- `modelos/painel.html`
- os arquivos de `prompts/`, só se você não instalou as skills

## 5. Faça a entrevista

Numa conversa dentro do Projeto, digite `/liliai-entrevista`. A primeira pergunta é a privacidade (sim ou não). Depois você escolhe o modo na P2: rápido (11 perguntas, cerca de 5 minutos) ou completo (38). Quem começa pelo rápido pode completar depois com "completar entrevista".

## 6. Salve o que a entrevista entrega

| Bloco | Onde vai |
|---|---|
| Resumo do contexto | Conhecimento do Projeto, como `contexto.md` |
| Instrução do projeto | Configurações do projeto > Instruções |
| Termos bloqueados | Já estão na instrução |
| `diario.json` inicial | Conhecimento do Projeto, como `diario.json` |

## Onde guardar o diário

| Forma | Como | Passo manual |
|---|---|---|
| **Arquivo no conhecimento do Projeto** | Cada comando devolve o `diario.json` completo; você substitui o arquivo | Sim, dez segundos por sessão |
| **Documento vivo ou artefato** | Se o seu Claude edita documentos ou artefatos, peça para manter o `diario.json` lá | Não |

## Memória

Se a memória do Claude estiver ligada, ela guarda fatos estáveis sobre você entre conversas. Não use a memória no lugar do diário: ela não é um registro auditável.
