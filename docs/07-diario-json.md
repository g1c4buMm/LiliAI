# O diário em JSON

O `diario.json` é a fonte única da sua mentoria. Os comandos leem e devolvem este arquivo, e o painel é só uma forma de vê-lo. Você nunca precisa editar o JSON à mão: peça ao Claude.

## Estrutura

```json
{
  "versao": 1,
  "perfil": {
    "titulo": "Minha mentoria de carreira",
    "pessoa": "cargo, da pergunta A1",
    "meta": "meta, da B1",
    "prazo_meta": "prazo, da B2",
    "mentoria": "formato, da C1 e C2",
    "modo_privacidade": "Anônimo ou Contexto",
    "revisao_semanal": "dia e horário, da G2"
  },
  "sessoes": [
    {
      "id": "S2026-10-09",
      "data": "2026-10-09",
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
| `id` de sessão | `S` + data. Duas sessões no mesmo dia: `S2026-10-09b` |
| `id` de lição e ação | id da sessão + `-L1`, `-L2`, `-A1`... Nunca muda depois de criado |
| `status` | `Feito`, `Aberto` ou `A confirmar`. É a única fonte do status: não há tabela separada de compromissos |
| `prazo` | `AAAA-MM-DD` ou `""`. `prazo_inferido: true` quando veio de interpretação |
| `tipo` de evidência | `Texto lido`, `Reunião com liderança` ou `Pedido da liderança` |
| `pilares[].licoes` | Lista de ids de lições, não de textos |

## Evidências de visibilidade

As ações medem o que você fez. As evidências medem o que mudou em quem decide:

- **Texto lido**: um texto seu foi lido, comentado ou repassado por quem decide.
- **Reunião com liderança**: você conseguiu tempo de agenda com quem decide.
- **Pedido da liderança**: alguém da liderança pediu sua opinião, um material ou sua presença.

Registre a qualquer momento com `/liliai-sessao evidência: o diretor pediu o resumo para levar ao comitê`. O `/liliai-semana` também pergunta se houve evidência nova.

## Privacidade

No modo Contexto, o diário pode ter nomes reais. Ele nunca entra no repositório: `diario.json` está no `.gitignore`. Para compartilhar, use `/liliai-painel` e escolha "Para compartilhar": a versão gerada é anonimizada e não leva as notas.
