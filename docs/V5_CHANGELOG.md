# Changelog — Sprint V5-A (10/11/2026)

## Entrega efetiva
- `actors.py`: novo protagonista próprio; 10 quadros 96×128, estados e 100 ms
  preservados, cache dos frames; hitbox anterior explicitamente preservada.
- `game.py / TelaJogo`: pivô da arma +9 px lateral espelhado e +3 px vertical,
  compartilhado com mira e muzzle. Nenhuma alteração em dano, cadência, economia,
  gravidade, plataformas, colisão ou progressão.
- `weapon_art.py`: centro da textura corrigido em 1 px; escala de apresentação e
  mãos proporcionais para retrato do menu. Arsenal continua AK, SMG, escopeta e rifle.
- `game.py / TelaMenu` e `arcade_style.py`: composição nova com ruínas, commando,
  aço/oliva/areia, botões com foco, atalhos visíveis e ranking clicável. Setas,
  Enter, mouse e feedback sonoro mantidos; movimento de fundo respeita F9.
- `game.py / TelaSobre`: reparo pontual de regressão já presente no workspace:
  construtor com avatar havia substituído o método de desenho. `on_draw` restaurado
  sem remover o avatar preexistente. Redesign dessa tela permanece para V5-B.
- Testes de contrato, proveniência/hashes, hitbox, cache, navegação, bounds,
  labels, redução de efeitos, muzzle/rotação e autoria.

## Baseline e preservação
Git inicial: game.py e tests/test_arcade_v3.py modificados; AGENTS.md, SETUP.md,
_audit_workspace/, docs/, prompts/ e skills/ não rastreados. Ver initial-status.txt e
preexisting.patch em evidence/v5-a. Nada foi revertido, commitado ou enviado.
Baseline nativo: **59 PASS / 1 FAIL** (teste anterior usava Button.rect inexistente).
O teste foi ajustado para a API real Button.box, com bounds e interseções reais.
Nenhum arquivo original da pasta pai ou assets/player.png foi sobrescrito.
Nenhuma chamada de inicialização/escrita no ranking real foi executada; teste ORM
usa banco temporário. O capturador não chama main()/inicializar_banco().

## Fontes consultadas
Prompt master integral; AGENTS.md; README.md; skill coin-commando-dev;
REQUISITOS_OBRIGATORIOS.md; GAPS_AUDITORIA_INICIAL.md; ASSET_AUDIT.md;
ASSET_SOURCES.md; MISSING_ASSETS.md; módulos e testes afetados, models.py, main.py,
SETUP.md; licenças locais Kenney Crosshair/Tanks, PVFX, vista-ten.
Não encontrados PDFs/DOCX originais na raiz/pasta pai inspecionada.

## Assets integrados
Apenas **commando personalizado**, PNG avulso (sem ZIP/RAR):
`../commando_unarmed_10f_960x128.png` → staging `assets/_staging_v5/commando.png`
→ `assets/v5/commando.png`. Deslocamento Y +6, sem escala. Usuário confirmou
ser o autor e autorizou uso, modificação e redistribuição pública nesta sessão.
Hashes e autorização em assets/v5/sources.json / ASSET_SOURCES.md.
Fundo ruins.png e armas locais reaproveitados. Nenhum asset dos ZIPs/RARs foi
promovido nesta sprint; pacotes sem licença continuam em quarentena.
Drone 384×128 e boss 1152×320 inspecionados: aparência de 4×2 células,
respectivamente 96×64 e 288×160; grade horizontal presumida corta os personagens.
Não integrados; ordem temporal e estados ainda não comprovados.

## Verificação final
| Estado | Verificação | Resultado |
| --- | --- | --- |
| PASS | Suíte completa com Arcade nativo Windows | **67 passed**, 4 PerformanceWarnings de draw_text, sem falhas |
| PASS | Lógica/assets sem EGL | **11 passed** |
| PASS | python -m py_compile dos arquivos afetados e compileall dos módulos/testes | Sem erros |
| PASS | python -m pip check | No broken requirements found |
| PASS | git diff --check | Sem erros |
| PASS | Capturas OpenGL nativas com janela visible=True | Menu, Sobre, jogo, quatro armas; 960×640 |
| BLOCKED | python -m pytest -q headless Windows | 3 erros de coleta: Library EGL not found; não contado como PASS |
| FAIL (baseline, corrigido) | Button.rect no teste anterior | 1 falha antes; agora usa box e verifica não sobreposição |
| FAIL (regressão demonstrada, corrigida) | Sobre sem autoria renderizada | Teste falhou antes do reparo e passa na suíte final |

Logs em docs/evidence/v5-a/: baseline-native.txt, native-pytest.txt,
logic-pytest.txt, headless-pytest.txt, pip-check.txt e about-regression-before.txt.
Python escolhido: .venv313/Scripts/python.exe, Python 3.13.14 / Arcade 3.3.3.
pytest não estava instalado; instalado somente no ambiente de desenvolvimento.

## Evidência e limites de aceite
Galeria: evidence/v5-a/gallery.html (também ligada em asset_gallery.html).
Capturas revisadas visualmente: menu sem truncamento ou interseção dos botões;
personagem sem pés encobertos; arma com mãos proporcionais no retrato;
quatro armas em 0, 0.8, pi e -1.2 rad com muzzle marcado; Sobre com autoria/avatar.
Gameplay antes contém fade de entrada, depois sem fade: não comparar luminância.
Não foi feita partida humana completa, escuta crítica, benchmark de FPS ou aprovação
estética pelo usuário. Corpo não possui rig de braços para todos os ângulos/frames;
a sobreposição usa mãos e pivô estáveis, com revisão humana em movimento pendente.

## Requisitos preservados / decisões pendentes
Views, Sprite/SpriteList, Bloco, PhysicsEnginePlatformer, can_jump, spritesheet,
prioridade das animações, ORM e Top 10 no construtor continuam presentes e cobertos
pelos testes existentes. Campanha de quatro fases, loja, armas, boss, moedas e
meta vigente de 70% não foram removidos. Conflito com 100% da Parte 1 e outros
itens da auditoria P1 permanecem sem decisão humana; não declarar conformidade
integral da atividade. Nenhum documento obrigatório foi alterado.

## V5-B — próxima sprint, não executada
1. Migrar Loja, Opções, Instruções, Sobre, Ranking, Pausa e Game Over para a
   família militar; manter estado, compras, input de nome e persistência.
2. Aplicar protagonista novo no avatar de Sobre e validar sprite/textos.
3. Reformular HUD/overlays/intro mantendo objetivos, moedas, munição, boss HP,
   feedback de recarga e área de combate visível.
4. Capturar cada tela em 960×640 e validar foco, atalhos, mouse, bounds e F9.
5. Partida manual para avaliar braços/armas durante caminhada/salto e mira extrema.
Drone/helicópteros/VFX ficam V5-C, cenários V5-D, boss/arena V5-E.

## Como executar no Windows
```powershell
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe tools/capture_v5.py --visible
.\.venv\Scripts\python.exe -c "import arcade,pytest; raise SystemExit(pytest.main(['-q']))"
```
O terceiro comando importa Arcade antes dos testes para usar WGL nativo em vez de
EGL headless. O comando padrão pytest continua bloqueado neste Windows; executar
sem essa adaptação no Linux/CI com EGL configurado para validar também o headless.
main.py usa o ranking normal; as capturas não inicializam nem escrevem nesse banco.
Aprovação humana pendente: visual/game feel e decisão acadêmica 70% versus 100%.
Sem commit, push ou publicação automática.

## Correção do ambiente após V5-A
A .venv anterior (Python 3.14, sem dependências) foi recriada com Python 3.13
e requirements.txt + pytest. A .venv313 duplicada foi movida para ../_venv313-backup-Projeto-Moedas após validar a nova; exclusão bloqueada pelo controle automático de segurança.
README atualizado com ativação Git Bash e ambiente único .venv.

## Continuação: menus/HUD e sprites
Implementação posterior solicitada pelo usuário em V5B_CHANGELOG.md; quatro assets
Kenney integrados e 70 testes nativos aprovados. Galeria evidence/v5-b/gallery.html.

## Continuação V6
Novo pedido executado: arsenal de3 armas, economia, sprites animados, menu e boss.
Ver V6_CHANGELOG.md e evidence/v6/gallery.html.
