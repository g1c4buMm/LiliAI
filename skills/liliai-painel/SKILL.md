---
name: liliai-painel
description: Gera o painel visual em HTML da mentoria LiliAI a partir do diario.json, com histórico, visibilidade, compromissos, pilares e métricas. Tem versão pessoal e versão anonimizada para compartilhar. Use com /liliai-painel.
---

# LiliAI: painel da mentoria

Gera uma página HTML única com o histórico completo da mentoria: números do ciclo, o plano para a meta com o status de cada objetivo e o histórico das mudanças, evidências de visibilidade, ações por status, lições por registro, prioridade, próximos 30 dias, compromissos com filtro e atraso, pilares e a linha do tempo de sessões, 1:1 e feedbacks.

## Entradas

- O `diario.json` do conhecimento do Projeto. Sem diário, diga isso, sugira /liliai-sessao e pare.
- O modo de privacidade da instrução do projeto. Se não houver, use Anônimo.
- Diário sem `plano` (versão 1): o painel mostra o plano vazio. Diga numa linha que o plano nasce no próximo /liliai-sessao.

## 1. Para quem é o painel

Pergunte, com botões se a ferramenta existir: "Este painel é para você ou para compartilhar?"
- **Para mim** (padrão): usa o diário como está.
- **Para compartilhar** (mentora, gestor, grupo): trabalhe numa cópia do diário e
  - troque nomes por funções, remova valores, e-mails e termos bloqueados
  - apague o campo `notas` de todas as sessões
  - pergunte com botões: "Incluir 1:1 com a gestão e feedbacks?" Opções: "Não, só a mentoria" (padrão) e "Sim, anonimizados". Com "Não", remova da cópia os registros com `tipo` diferente de Mentoria, as ações e lições deles, as evidências que apontam para eles, as ligações a esses ids nos objetivos do plano e as entradas do `plano.historico` com essa origem
  - releia o texto dos objetivos e do histórico do plano: nada de expectativas atribuídas a uma pessoa, valores ou termos bloqueados
  - rode a checagem do /liliai-privacidade sobre a cópia e mostre a tabela

## 2. Pilares

Se o diário tiver três sessões ou mais e `pilares` estiver vazio, ou se houver lições de sessões novas fora de qualquer pilar, agrupe as lições em até cinco pilares: `{"nome": "...", "licoes": ["ids das lições"], "o_que_muda": "uma frase"}`. Use ids, nunca textos. Com menos de três sessões, deixe `pilares` vazio.

## 3. Montar a página

Use `modelos/painel.html` do conhecimento do Projeto. Se não estiver lá, use `painel.html` que acompanha esta skill. Se nenhum dos dois estiver disponível, peça o arquivo e pare. Não improvise outro layout.

**Copie o modelo inteiro, sem mudar HTML, CSS ou script. Troque somente o conteúdo do bloco `<script type="application/json" id="dados">` por:**

```json
{"exibicao": {"hoje": "AAAA-MM-DD", "audiencia": "pessoal ou compartilhar", "exemplo": false},
 "diario": { ...o diario.json inteiro, ou a cópia anonimizada... }}
```

O modelo calcula sozinho contagens, atrasos, gráficos, pilares e filtros. Valide o JSON antes de entregar.

## 4. Entrega

1. Se você puder publicar páginas ou artefatos, publique o HTML. Se não puder, entregue o arquivo `painel-AAAA-MM-DD.html` completo num bloco de código, para salvar e abrir no navegador.
2. Em até três linhas: objetivos em risco, atrasadas, próximo prazo, evidências nos últimos 30 dias e o pilar mais forte.
3. Se os pilares mudaram, devolva também o `diario.json` atualizado para substituir no Projeto (só na versão pessoal; a cópia anonimizada nunca substitui o diário).
4. Na versão pessoal, lembre: "Para compartilhar, rode /liliai-painel de novo e escolha Para compartilhar."
