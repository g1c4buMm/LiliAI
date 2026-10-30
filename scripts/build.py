#!/usr/bin/env python3
"""Build do kit LiliAI. Só para quem mantém o repositório; quem usa o kit não precisa rodar.

    python3 scripts/build.py           gera tudo
    python3 scripts/build.py --check   confere se o que está no repositório bate com a fonte (CI)

Fonte única:
- skills/<nome>/SKILL.md        instruções de cada comando
- onboarding/questionario.md    perguntas da entrevista
- modelos/painel.html           visual do painel
- modelos/diario.json           diário vazio
- exemplos/diario-*.json        diários fictícios

Gerado a partir da fonte:
- prompts/NN-*.md               versão "colar à mão" de cada skill
- skills/<nome>/<anexos>        cópias dos modelos que cada skill usa
- skills/dist/<nome>.zip        pacotes para instalar
- modelos/painel.html (dados)   exemplo embutido no modelo
- exemplos/painel-*.html        painéis renderizados dos diários de exemplo
"""
import io, json, re, sys, zipfile, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = '--check' in sys.argv
HOJE_EXEMPLO = '2026-10-10'

SKILLS = [  # ordem do fluxo; número do prompt equivalente
    ('liliai-entrevista', '00-entrevista', 'Entrevista'),
    ('liliai-sessao', '01-sessao', 'Registrar uma sessão'),
    ('liliai-semana', '02-semana', 'Revisão semanal e pauta'),
    ('liliai-painel', '03-painel', 'Painel da mentoria'),
    ('liliai-privacidade', '04-privacidade', 'Checagem de privacidade'),
]
ANEXOS = {
    'liliai-entrevista': [('onboarding/questionario.md', 'questionario.md'), ('modelos/diario.json', 'diario.json'), ('modelos/painel.html', 'painel.html')],
    'liliai-sessao': [('modelos/diario.json', 'diario.json'), ('modelos/painel.html', 'painel.html')],
    'liliai-painel': [('modelos/painel.html', 'painel.html')],
}
REMOVIDOS = ['liliai-preparar', 'liliai-pilares', 'liliai-dossie']
DOCS_COM_COMANDOS = ['README.md', 'index.html', 'skills/README.md']
STATUS = {'Feito', 'Aberto', 'A confirmar'}
TIPOS = {'Texto lido', 'Reunião com liderança', 'Pedido da liderança'}
FONTES = {'Mentoria', '1:1 com gestão', 'Feedback formal', 'Feedback informal', 'Outra fonte'}
STATUS_OBJ = {'Não iniciado', 'No rumo', 'Em risco', 'Concluído'}

problemas, mudou = [], []


def escrever(rel, conteudo):
    p = ROOT / rel
    dados = conteudo if isinstance(conteudo, bytes) else conteudo.encode('utf-8')
    atual = p.read_bytes() if p.exists() else None
    if atual == dados:
        return
    mudou.append(rel)
    if not CHECK:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(dados)


def ler(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def corpo_skill(nome):
    texto = ler(f'skills/{nome}/SKILL.md')
    m = re.match(r'^---\n(.*?)\n---\n', texto, re.S)
    if not m:
        problemas.append(f'skills/{nome}/SKILL.md sem frontmatter')
        return '', ''
    fm, corpo = m.group(1), texto[m.end():]
    if not re.search(rf'^name: {re.escape(nome)}$', fm, re.M):
        problemas.append(f'skills/{nome}/SKILL.md: name diferente da pasta')
    desc = re.search(r'^description: (.*)$', fm, re.M)
    return (desc.group(1) if desc else ''), corpo.strip()


def data_ok(s):
    try:
        datetime.date.fromisoformat(s)
        return True
    except Exception:
        return False


def validar_diario(rel, d):
    pre = f'{rel}:'
    for k in ('versao', 'perfil', 'sessoes', 'evidencias', 'pilares'):
        if k not in d:
            problemas.append(f'{pre} falta "{k}"')
    ids, licoes, sess_ids = set(), set(), set()
    for s in d.get('sessoes', []):
        sid = s.get('id', '')
        if not re.fullmatch(r'S\d{4}-\d{2}-\d{2}[a-z]?', sid) or not data_ok(s.get('data', '')):
            problemas.append(f'{pre} sessão com id ou data inválidos: {sid}')
        if sid in sess_ids:
            problemas.append(f'{pre} id de sessão repetido: {sid}')
        sess_ids.add(sid)
        for l in s.get('licoes', []):
            if not l.get('id', '').startswith(sid + '-L') or l['id'] in ids:
                problemas.append(f'{pre} id de lição inválido ou repetido: {l.get("id")}')
            ids.add(l.get('id')); licoes.add(l.get('id'))
        for a in s.get('acoes', []):
            if not a.get('id', '').startswith(sid + '-A') or a['id'] in ids:
                problemas.append(f'{pre} id de ação inválido ou repetido: {a.get("id")}')
            ids.add(a.get('id'))
            if a.get('status') not in STATUS:
                problemas.append(f'{pre} status inválido em {a.get("id")}: {a.get("status")}')
            if a.get('prazo') and not data_ok(a['prazo']):
                problemas.append(f'{pre} prazo inválido em {a.get("id")}')
    for e in d.get('evidencias', []):
        if e.get('tipo') not in TIPOS or not data_ok(e.get('data', '')):
            problemas.append(f'{pre} evidência inválida: {e.get("id")}')
        if e.get('sessao') and e['sessao'] not in sess_ids:
            problemas.append(f'{pre} evidência {e.get("id")} aponta para sessão inexistente')
    for p in d.get('pilares', []):
        for lid in p.get('licoes', []):
            if lid not in licoes:
                problemas.append(f'{pre} pilar "{p.get("nome")}" aponta para lição inexistente {lid}')
    acoes_ids = {a.get('id') for s in d.get('sessoes', []) for a in s.get('acoes', [])}
    ev_ids = {e.get('id') for e in d.get('evidencias', [])}
    for s in d.get('sessoes', []):
        if s.get('tipo', 'Mentoria') not in FONTES:
            problemas.append(f'{pre} tipo de registro inválido em {s.get("id")}: {s.get("tipo")}')
    plano = d.get('plano')
    if plano is None:
        if d.get('versao', 1) >= 2:
            problemas.append(f'{pre} falta "plano" (versao 2)')
        return
    if plano.get('atualizado_em') and not data_ok(plano['atualizado_em']):
        problemas.append(f'{pre} plano.atualizado_em inválido')
    oids = set()
    for o in plano.get('objetivos', []):
        oid = o.get('id', '')
        if not re.fullmatch(r'O\d+', oid) or oid in oids:
            problemas.append(f'{pre} id de objetivo inválido ou repetido: {oid}')
        oids.add(oid)
        if o.get('status') not in STATUS_OBJ:
            problemas.append(f'{pre} status inválido no objetivo {oid}: {o.get("status")}')
        for aid in o.get('acoes', []):
            if aid not in acoes_ids:
                problemas.append(f'{pre} objetivo {oid} aponta para ação inexistente {aid}')
        for eid in o.get('evidencias', []):
            if eid not in ev_ids:
                problemas.append(f'{pre} objetivo {oid} aponta para evidência inexistente {eid}')
    for h in plano.get('historico', []):
        if not data_ok(h.get('data', '')) or not h.get('mudancas'):
            problemas.append(f'{pre} entrada de histórico do plano inválida: {h}')
        o = h.get('origem', '')
        if o not in sess_ids and o not in ('entrevista', 'semana') and not o.startswith('E'):
            problemas.append(f'{pre} histórico do plano com origem desconhecida: {o}')


def injetar(modelo, diario, audiencia='pessoal', exemplo=True):
    dados = {'exibicao': {'hoje': HOJE_EXEMPLO, 'audiencia': audiencia, 'exemplo': exemplo}, 'diario': diario}
    bloco = json.dumps(dados, ensure_ascii=False, indent=2).replace('</', '<\\/')
    return re.sub(r'(<script type="application/json" id="dados">\n).*?(\n</script>)',
                  lambda m: m.group(1) + bloco + m.group(2), modelo, count=1, flags=re.S)


def zip_skill(nome):
    buf = io.BytesIO()
    pasta = ROOT / 'skills' / nome
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(pasta.rglob('*')):
            if f.is_file():
                info = zipfile.ZipInfo(f'{nome}/{f.relative_to(pasta).as_posix()}', (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, f.read_bytes())
    return buf.getvalue()


def main():
    # 1. exemplos: validar e renderizar
    modelo = ler('modelos/painel.html')
    exemplos = sorted((ROOT / 'exemplos').glob('diario-*.json'))
    for f in exemplos:
        d = json.loads(f.read_text(encoding='utf-8'))
        validar_diario(f'exemplos/{f.name}', d)
        nome = f.stem.replace('diario-', '')
        escrever(f'exemplos/painel-{nome}.html', injetar(modelo, d))
    for f in sorted((ROOT / 'demo').glob('diario-*.json')):
        d = json.loads(f.read_text(encoding='utf-8'))
        validar_diario(f'demo/{f.name}', d)
        nome = f.stem.replace('diario-', '')
        aud = 'compartilhar' if nome.endswith('compartilhar') else 'pessoal'
        escrever(f'demo/painel-{nome}.html', injetar(modelo, d, audiencia=aud))
    validar_diario('modelos/diario.json', json.loads(ler('modelos/diario.json')))
    normal = json.loads(ler('exemplos/diario-normal.json'))
    modelo = injetar(modelo, normal)
    escrever('modelos/painel.html', modelo)

    # 2. anexos das skills
    for nome, arquivos in ANEXOS.items():
        for origem, destino in arquivos:
            escrever(f'skills/{nome}/{destino}', (ROOT / origem).read_bytes() if origem != 'modelos/painel.html' else modelo.encode('utf-8'))

    # 3. prompts gerados a partir das skills
    indice = ['# Prompts', '',
              'Gerados a partir de `skills/*/SKILL.md` pelo `scripts/build.py`. Não edite aqui: edite a skill.', '',
              'Use quando o seu plano não tiver Skills. Abra o arquivo, copie o bloco de código e cole numa conversa dentro do seu Projeto.', '',
              '| Arquivo | Equivale a |', '|---|---|']
    esperados = set()
    for nome, arq, titulo in SKILLS:
        desc, corpo = corpo_skill(nome)
        texto = (f'# Prompt {arq[:2]}. {titulo}\n\n'
                 f'Equivale ao comando `/{nome}`. {desc}\n\n'
                 'Copie o bloco abaixo e cole numa conversa dentro do seu Projeto. Onde o texto disser "esta skill", leia "este prompt".\n\n'
                 '````text\n' + corpo + '\n````\n')
        escrever(f'prompts/{arq}.md', texto)
        esperados.add(f'{arq}.md')
        indice.append(f'| `{arq}.md` | `/{nome}` |')
    escrever('prompts/README.md', '\n'.join(indice) + '\n')
    for f in (ROOT / 'prompts').glob('*.md'):
        if f.name != 'README.md' and f.name not in esperados:
            problemas.append(f'prompts/{f.name} não corresponde a nenhuma skill (apague)') if CHECK else f.unlink()

    # 4. zips
    pastas = sorted(p.name for p in (ROOT / 'skills').iterdir() if p.is_dir() and p.name.startswith('liliai-'))
    if pastas != sorted(n for n, _, _ in SKILLS):
        problemas.append(f'pastas de skills {pastas} diferem da lista SKILLS do build')
    for nome, _, _ in SKILLS:
        escrever(f'skills/dist/{nome}.zip', zip_skill(nome))
    for f in (ROOT / 'skills' / 'dist').glob('*.zip'):
        if f.stem not in pastas:
            problemas.append(f'skills/dist/{f.name} é de uma skill que não existe') if CHECK else f.unlink()

    # 5. documentação cita todos os comandos e nenhum removido
    for doc in DOCS_COM_COMANDOS:
        t = ler(doc)
        for nome, _, _ in SKILLS:
            if f'/{nome}' not in t:
                problemas.append(f'{doc} não menciona /{nome}')
    for f in ROOT.rglob('*'):
        if f.is_file() and f.suffix in {'.md', '.html'} and 'CHANGELOG' not in f.name:
            t = f.read_text(encoding='utf-8', errors='ignore')
            for r in REMOVIDOS:
                if r in t:
                    problemas.append(f'{f.relative_to(ROOT)} ainda cita {r}')

    if mudou:
        print(('Desatualizado: ' if CHECK else 'Gerado: ') + ', '.join(mudou))
    for p in problemas:
        print('ERRO:', p)
    if problemas or (CHECK and mudou):
        sys.exit(1)
    print('OK')


if __name__ == '__main__':
    main()
