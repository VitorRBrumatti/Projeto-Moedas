# Organização do repositório — 11/11/2026

## Escopo
Limpeza estrutural, sem alterar jogabilidade, balanceamento, arte ou requisitos.
Git estava limpo no início. Sem commit ou push nesta etapa.

## Resultado
- Ativos em `assets/sprites/`, `assets/ui/`, `assets/audio/` e `assets/licenses/`.
- Registro único: `assets/sprites/sprites.json`, sem caminhos entre versões.
- Proveniência/hash dos54 arquivos ativos: `assets/sources.json`.
- Fontes, versões antigas e manifestos originais preservados em `assets/archive/v5`–`v8`.
  Não foram apagados ou recriados os sprites/sons. Mapa antes/depois em ASSET_RELOCATION.json.
- `sprites_v6.py` virou `sprite_assets.py`; todos os imports ativos atualizados.
- Dois protótipos sem callers (`beam`, `bullet`) saíram do preload; PNGs e fontes
  continuam no arquivo histórico. Laser/projéteis reais usam suas folhas atuais.
- `tools/capture.py` substitui os cinco capturadores versionados; snapshots originais
  como texto em `docs/history/tool-snapshots/`. `tools/generate_audio.py` continua
  disponível para regeneração explícita, sem ter sido executado na limpeza.
- Relatórios V5–V8 e setup antigo do Hermes em `docs/history/`.
- Evidências antigas ficaram nos mesmos caminhos, para preservar links já usados.
  `docs/asset_gallery.html` organiza o acesso; capturas novas em `evidence/current/`.
- README reescrito com estado atual, sem instruções antigas contraditórias.
- Testes renomeados por função: `test_assets.py`, `test_game_rules.py`,
  `test_views_and_combat.py` e `test_projectiles.py`, mantendo a cobertura.
- Removidos somente imports comprovadamente sem uso; módulos do jogo continuam
  na raiz para evitar refatoração desnecessária da arquitetura.

## Preservado
Nenhuma alteração nas regras de campaign.py, modelos/models.py, layouts de fases,
requisitos obrigatórios, gravidade, colisões, economia ou ranking.db.
`assets/player.png` original continua intacto e usado para a hitbox de referência.
`.venv`, backups e `_audit_workspace` continuam locais/ignorados, sem remoção.
Licenças originais preservadas e disponíveis ao lado dos ativos.

## Validação executada
- PASS:54 arquivos ativos comparados byte a byte por SHA-256 durante a migração.
- PASS:86 testes em contexto gráfico nativo Windows (4 avisos draw_text).
- PASS:py_compile dos módulos, ferramentas e testes; pip check; git diff --check.
- PASS:cópia isolada só com código e assets atuais, **sem assets/archive**, abriu
  menu e gameplay e decodificou os sons de marcha/Glock/AK/Minigun; não abriu o banco real.
- PASS:capturador atual executado, incluindo ida/volta de tela cheia e coordenadas
  do mouse; capturas atuais revisadas em `evidence/current/gallery.html`.
- BLOCKED:pytest headless Windows continua sem EGL; log separado em evidence/current.

Logs nativos em `evidence/current/tests-native.txt`.
Esta limpeza não reduz por remoção a história dos assets; ela separa o que o jogo
carrega do que foi preservado como fonte/versão anterior. Não há promessa de redução
mensurada de tamanho ou FPS. Sem partida humana completa ou teste mobile.

## Preparação do commit autorizada pelo usuário
Fontes/versões em assets/archive/ e snapshots em docs/history/tool-snapshots/
ficam locais e ignorados, pois não são necessários para rodar o jogo. Seus arquivos
originais continuam recuperáveis no commit anterior 1d121ce. Assets ativos, licenças,
testes e documentação atual permanecem versionados.

pytest.ini restringe a coleta à pasta tests/, evitando interpretar logs TXT de
evidências como doctests (erro reproduzido durante a preparação do commit).
