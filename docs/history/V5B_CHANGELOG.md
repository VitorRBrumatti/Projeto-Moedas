# Menus, HUD e sprites dos packs — V5-B

## Pedido implementado
Unificar os menus e a faixa superior de gameplay com a tela inicial militar.
Priorizar assets locais adequados no lugar de redesenhar ícones por código.

## Mudanças reais
- `arcade_style.py`: painéis compartilhados, botões pixelados da mesma família,
  paleta oliva/areia/ferrugem, ícones reais e glifo %; ajuste da moldura para oliva.
- `ui_fx.py`: todos os botões secundários usam esse renderer, sem deslocamento de
  hover que separava o card do seu conteúdo. Áreas de clique/ações preservadas.
- `game.py`: Loja, Opções, Instruções, Sobre, Ranking, Game Over e Pausa usam o
  mesmo tratamento de painéis/títulos/botões da tela inicial. Avatar de Sobre
  passou a usar o frame individual do protagonista novo, com cache existente.
- HUD dividido em pontos/créditos, vida/dash/facas, arma/munição/recarga e missão.
  Valores continuam ligados à campanha real; moeda/meta/tempo/combo/boss mantidos.
- Placa de suprimentos e loja usam ícone de munição; proteção e reparo usam os
  PNGs selecionados. Mira procedural substituída por sprite com alpha recortado.
- Quatro texturas carregadas em GameWindow.__init__, nunca em on_draw.
- Sem alteração de física, câmera, dano, preço, compras, meta ou progressão.

## Assets integrados (CC0 verificada no License.txt de cada pack)
| ZIP | Caminho interno | Runtime |
| --- | --- | --- |
| kenney_tanksPack.zip | PNG/Default size/tanks_crateAmmo.png | assets/v5/ammo.png |
| kenney_tanksPack.zip | PNG/Default size/tanks_crateArmor.png | assets/v5/armor.png |
| kenney_tanksPack.zip | PNG/Default size/tanks_crateRepair.png | assets/v5/repair.png |
| kenney_crosshair-pack.zip | PNG/Outline/crosshair-002.png | assets/v5/crosshair.png |

Autor Kenney, https://kenney.nl. Licenças copiadas para assets/v5/.
Fontes, hashes SHA-256 (fonte/adaptado), permissão e alterações em sources.json.
Crosshair: conversão RGBA e recorte (27,27,47,47), 74×74 → 20×20, sem redesenho.
Demais PNGs copiados sem alteração. Staging preservado em assets/_staging_v5/.
As caixas são ícones de interface/sinalização, não tanques top-down no cenário.
Arquivos originais/ZIPs/RARs e ranking.db preservados. Packs não foram reextraídos.
Não há armas laterais licenciadas adequadas comprovadas nos packs inspecionados;
as quatro armas atuais foram mantidas. Sprites/Terrorist/vacaroxa continuam sem
licença local comprovada; drone/boss próprios precisam validar grade/estados antes
 de integrar. Não foram substituídos inimigos, cenários ou boss nesta tarefa.

## Verificação
- PASS: 70 testes, contexto OpenGL nativo Windows; 4 avisos PerformanceWarning draw_text.
- PASS: py_compile dos módulos/testes/capturador afetados; pip check; git diff --check.
- PASS: capturas reais nativas de 10 telas/estados e revisão visual das imagens.
- BLOCKED: pytest padrão headless, 3 erros de coleta por Library EGL not found.
- Regressão demonstrada antes: UI não tinha texturas pré-carregadas; teste falhou
  e passou após implementação. Testes protegem economia sem render-time loads,
  recorte alpha da mira e separação do rótulo PTS/score.
- Capturador `tools/capture_v5b.py` usa banco temporário e prepara recarga para QA.
  Ranking da evidência está vazio de propósito; Game Over não salva no banco real.
- Galeria em `docs/evidence/v5-b/gallery.html`; logs no mesmo diretório.

## Executar
```bash
source .venv/Scripts/activate
python main.py
```
Fechar a janela antiga e reabrir para carregar o código novo.
Capturas: `python tools/capture_v5b.py`.
Testes Windows nativos: `python -c "import arcade,pytest; raise SystemExit(pytest.main(['-q']))"`.

## Limites e próximos passos
Sem partida humana completa, escuta ou benchmark de FPS. Revisão feita em capturas
960×640 e suíte automatizada. Aprovação estética final continua com o usuário.
Não alterada a decisão pendente de 70% versus 100% das moedas. Sem commit ou push.
Próxima etapa: validar/adaptar grades dos drones/boss próprios e selecionar VFX
compatíveis com licença, sem mudar IA nem regras durante trabalho só visual.
