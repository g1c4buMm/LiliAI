# O diário em JSON

O `diario.json` é a fonte única da sua mentoria. Os comandos leem e devolvem este arquivo, e o painel é só uma forma de vê-lo. Você nunca precisa editar o JSON à mão: peça ao Claude.

## Estrutura

```json
{
  "versao": 2,
  "perfil": {
    "titulo": "Minha mentoria de carreira",
    "pessoa": "cargo, da pergunta A1",
    "meta": "meta, da B1",
    "prazo_meta": "prazo, da B2",
    "mentoria": "formato, da C1 e C2",
    "modo_privacidade": "Anônimo ou Contexto",
    "revisao_semanal": "dia e horário, da G2"
  },
  "plano": {
    "atualizado_em": "2026-10-09",
    "objetivos": [
      {"id": "O1", "texto": "Tornar o trabalho visível para quem decide",
       "indicador": "Resumo quinzenal chegando ao gestor", "status": "No rumo",
       "acoes": ["S2026-10-09-A1"], "evidencias": ["E1"]}
    ],
    "historico": [
      {"data": "2026-10-09", "origem": "S2026-10-09",
       "mudancas": ["O1: passou de Não iniciado para No rumo: resumo de uma página definido"]}
    ]
  },
  "sessoes": [
    {
      "id": "S2026-10-09",
      "data": "2026-10-09",
      "tipo": "Mentoria",
      "com": "",
      "tema": "Visibilidade com a liderança",
      "notas": "texto limpo da sessão",
      "licoes": [
        {"id": "S2026-10-09-L1", "texto": "Entregar sem comunicar não gera visibilidade."}
      ],
      "acoes": [
        {"id": "S2026-10-09-A1", "descricao": "Escrever o primeiro resumo", "responsavel": "Eu",
         "prazo": "2026-10-23", "prazo_inferido": true, "status": "Aberto"}
      ],
      "perguntas": ["Qual caso levar ao diretor regional?"]
    }
  ],
  "evidencias": [
    {"id": "E1", "data": "2026-10-20", "tipo": "Texto lido", "descricao": "Resumo quinzenal lido e comentado",
     "quem": "Gestor direto", "sessao": "S2026-10-09"}
  ],
  "pilares": [
    {"nome": "Visibilidade com quem decide", "licoes": ["S2026-10-09-L1"], "o_que_muda": "Resumo quinzenal ao gestor."}
  ],
  "prioridade": "uma frase",
  "proximos_30_dias": ["até cinco itens"]
}
```

## Regras

| Campo | Regra |
|---|---|
| `id` de registro | `S` + data. Dois registros no mesmo dia: `S2026-10-09b` |
| `tipo` de registro | `Mentoria` (padrão, também quando o campo falta), `1:1 com gestão`, `Feedback formal`, `Feedback informal` ou `Outra fonte` |
| `com` | Quem participou ou deu o feedback: função no Anônimo, nome no Contexto |
| `id` de lição e ação | id da sessão + `-L1`, `-L2`, `-A1`... Nunca muda depois de criado |
| `status` | `Feito`, `Aberto` ou `A confirmar`. É a única fonte do status: não há tabela separada de compromissos |
| `prazo` | `AAAA-MM-DD` ou `""`. `prazo_inferido: true` quando veio de interpretação |
| `tipo` de evidência | `Texto lido`, `Reunião com liderança` ou `Pedido da liderança` |
| `pilares[].licoes` | Lista de ids de lições, não de textos |
| `plano.objetivos[].id` | `O1`, `O2`... Nunca muda depois de criado |
| `plano.objetivos[].status` | `Não iniciado`, `No rumo`, `Em risco` ou `Concluído` |
| `plano.objetivos[].acoes` e `evidencias` | Ids que existem no diário |
| `plano.historico[].origem` | Id do registro, id da evidência, `entrevista` ou `semana` |
| `plano.historico[].mudancas` | Cada linha começa pelo id do objetivo (`O2: ...`), ou por `Prioridade:` ou `Próximos 30 dias:` |

## Plano que aprende

O plano é o caminho até a meta. Ele nasce na entrevista e é revisto a cada `/liliai-sessao`, seja uma sessão de mentoria, um 1:1 com a gestão ou um feedback:

1. Ações e evidências novas são ligadas ao objetivo a que servem.
2. Cada objetivo muda de status só com motivo escrito: "Em risco" quando uma ação ligada atrasa ou a gestão sinaliza o contrário.
3. Uma expectativa nova da gestão vira objetivo novo.
4. Quando a gestão e a mentoria dizem coisas diferentes, o Claude não escolhe: aponta o conflito e leva a pergunta para a próxima sessão.
5. Tudo fica no `historico`, que o painel mostra em "Como o plano mudou".

Diários da versão 1 (sem `plano`) continuam funcionando: o próximo `/liliai-sessao` cria o plano e muda a versão para 2.

## Evidências de visibilidade

As ações medem o que você fez. As evidências medem o que mudou em quem decide:

- **Texto lido**: um texto seu foi lido, comentado ou repassado por quem decide.
- **Reunião com liderança**: você conseguiu tempo de agenda com quem decide.
- **Pedido da liderança**: alguém da liderança pediu sua opinião, um material ou sua presença.

Registre a qualquer momento com `/liliai-sessao evidência: o diretor pediu o resumo para levar ao comitê`. O `/liliai-semana` também pergunta se houve evidência nova.

## Privacidade

Salário, bônus, remuneração e assuntos pessoais de qualquer pessoa nunca entram no diário, em nenhum modo. No modo Contexto, o diário pode ter nomes reais. Ele nunca entra no repositório: `diario.json` está no `.gitignore`. Para compartilhar, use `/liliai-painel` e escolha "Para compartilhar": a versão gerada é anonimizada, não leva as notas e, por padrão, deixa de fora 1:1 e feedbacks.
