---
name: liliai-privacidade
description: Checa e anonimiza um texto antes de compartilhar, procurando nomes, e-mails, valores, documentos internos e termos bloqueados do LiliAI. Use com /liliai-privacidade junto com o texto.
---

# LiliAI: checagem de privacidade

Se o usuário não colar um texto, pergunte qual texto checar. Se ele disser "o último", use a última saída desta conversa.

## Leitura

Esta checagem vale nos dois modos de privacidade. Mesmo no modo Contexto, o texto que sai do Projeto sai anonimizado.

Leia o texto como um estranho. Procure:
- nomes de pessoas, empresas e clientes
- e-mails e telefones
- valores em moeda
- números de documento e de contrato
- documentos ou projetos internos
- qualquer termo da lista de termos bloqueados e do "o que nunca registrar" da instrução do projeto

## Saída

1. Tabela `trecho | tipo | motivo`. Se não achar nada, diga isso.
2. O texto reescrito com funções no lugar de nomes e sem valores.
3. Lista do que não deu para anonimizar com segurança.
4. Última linha, sempre: "Esta é uma segunda leitura, não uma garantia. Releia antes de enviar e confirme a política da sua empresa e o combinado do seu grupo de mentoria."
