# Privacidade

## Onde ficam seus dados

No seu Projeto no Claude. Este repositório tem só o kit.

## Dois modos, escolhidos por você

A primeira pergunta da entrevista (P1) pede um sim ou não explícito.

| | Anônimo (padrão, P1 = não) | Contexto (P1 = sim) |
|---|---|---|
| O que fica no diário | Só funções, sem nomes nem valores | Dados reais do seu contexto |
| Precisão do Claude | Boa | Maior, porque ele conhece pessoas e casos pelo nome |
| Texto para compartilhar | Anonimizado | Anonimizado, sempre |
| O que está no I1 | Nunca registrado | Nunca registrado |
| Este repositório | Nunca recebe dado seu | Nunca recebe dado seu |

Regras do consentimento:

- Só vale "sim" explícito, com a frase de confirmação de que a política da empresa permite. Na dúvida, o modo é Anônimo.
- Se a resposta do H3 (política da empresa) contradizer o "sim", o Claude aponta o conflito e volta para Anônimo.
- O modo e a data ficam escritos na instrução do projeto e no resumo de contexto.
- Para voltar atrás, diga "mudar para anônimo". O Claude anonimiza o diário e devolve a versão nova.

## O que nunca deve aparecer nos seus textos compartilhados

- nomes de pessoas e clientes
- endereços de e-mail
- valores em moeda
- números de documento
- documentos internos da empresa
- cada termo da sua lista de termos bloqueados

## Como o LiliAI protege

1. A instrução do projeto manda anonimizar e usar funções no lugar de nomes.
2. Os termos bloqueados ficam na instrução do projeto. O Claude avisa quando algum aparece.
3. O `/liliai-privacidade` faz uma segunda leitura antes de qualquer compartilhamento, e o `/liliai-painel` tem uma versão "para compartilhar" já anonimizada, sem as notas.

## O limite

A checagem por prompt é uma leitura feita por um modelo. Ela pega muito, mas não é determinística. Releia você mesmo o que vai compartilhar.

## Antes de compartilhar qualquer coisa

1. Rode o `/liliai-privacidade` e corrija o que ele mostrar.
2. Releia como um estranho.
3. Confirme a política da sua empresa para ferramentas de IA e para compartilhar conteúdo de mentoria.
4. Confirme o que o seu grupo de mentoria combinou sobre confidencialidade.
5. Compartilhe só o que é seu e já está anonimizado.
