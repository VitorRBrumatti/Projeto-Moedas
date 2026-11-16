# Fontes, Licenças e Rastreabilidade de Assets — Coin Commando

Este documento registra a origem, licença verificada e elegibilidade técnica de todos os pacotes inspecionados na pasta pai (`../`).

> **Regra de conformidade (`AGENTS.md`):** Nunca introduzir assets com licença incompatível ou desconhecida em produção sem validar a licença original na fonte de download.

---

## 1. Tabela de Pacotes Inspecionados

| Arquivo Compactado (`../`) | Conteúdo Principal | Arquivo de Licença no Pacote | Licença Identificada | Situação Legal | Recomendação |
|---|---|---|---|---|---|
| `pvfx-foundry-thirteen-spritesheets.zip` | Spritesheets de VFX pixel art (`lit` e `strict`, `grid` e `packed`, com `manifest.json`) | `LICENSE.txt`, `PROVENANCE.json` | **CC0 1.0 Universal** (Domínio Público) | **Liberado** (uso comercial e pessoal sem atribuição obrigatória) | **Usar diretamente** (priorizar pasta `strict/grid` para pixel art). |
| `kenney_crosshair-pack.zip` | 200 miras de mouse (`Dark`, `Outline`, `White`) | `License.txt` | **CC0 1.0 Universal** (Kenney.nl) | **Liberado** | **Usar diretamente** (`Outline` ou `Dark` escalado para ~`0.45–0.5`). |
| `vista-ten-1.0.0.zip` | 10 cenários parallax de 4 camadas (`384×216` e `@3x`) + paletas `.gpl` | `LICENCE.txt` | **CC0 1.0 Universal** | **Liberado** (proibido apenas revender como asset pack) | **Reserva técnica** (útil se quiser parallax real multi-camada). |
| `kenney_tanksPack.zip` | Tanques, barris, caixotes e minas vetoriais | `License.txt` | **CC0 1.0 Universal** (Kenney.nl) | **Liberado** | **Não usar** (estilo vetorial flat incompatível com pixel art). |
| `vacaroxa--generic-run-n-gun-pack--v.1.0.zip` | Inimigos (`ARMob`, `RPGmob`, `SniperMob`), jogador, tilesets urbanos/industriais, explosão | **Nenhum arquivo de licença dentro do `.zip`** | Não informada no arquivo | **Atenção:** confirmar licença na página do autor (`vacaroxa` no Itch.io) antes de publicar/entregar | **Adaptar** inimigos, caixote e tiles industriais após confirmar licença. |
| `helicopter.zip` | Helicóptero pixel art 8 quadros (`96×32`) + partes destruídas | **Nenhum arquivo de licença dentro do `.zip`** | Não informada no arquivo | **Atenção:** confirmar origem e licença antes de distribuir | **Opcional** para extração/cutscene após confirmar licença. |
| `AssortedPixelArt.rar` | `IndustrialRuins_32x32.png`, `MyCaveTileset_32x32.png`, `monster_64x64.png`, `TopDownModernExterior_16x16.png` | **Nenhum arquivo de licença dentro do `.rar`** | Não informada no arquivo | **Atenção:** confirmar origem e licença antes de distribuir | **Adaptar** apenas `IndustrialRuins_32x32.png` se licença for compatível. |
| `Pixel Art - City Landscape V2.zip` | Camadas de fundo de cidade pixel art (`512px` largura) | **Nenhum arquivo de licença** (apenas `SpriteList.txt`) | Não informada no arquivo | **Atenção:** confirmar origem e licença | **Não necessário** (sem fase urbana no jogo atual). |
| `Sprites.zip` | `Army Soldier Sprites` (`250×250`) e `Terrorist Sprites` (`246×297`) | **Nenhum arquivo de licença** (`README.html` -> `yoogameart.com`) | Não informada no arquivo | **Não recomendado** (licença não anexada + estilo incompatível) | **Descartar** (estilo cartoon pintado e escala incompatível). |

---

## 2. Mapa de Origem -> Destino Recomendado (Somente Pacotes Liberados ou Elegíveis)

| Recurso de Origem (`_audit_workspace/...`) | Alvo no Coin Commando | Ação Necessária |
|---|---|---|
| `pvfx-foundry-thirteen-spritesheets/effects/explosions/big-explosion/strict/grid/sprite-sheet.png` | Explosões de `Grenade`, `Barrel`, `Impact("explosion")` | Carregar grid `128×128`, 18 quadros |
| `pvfx-foundry-thirteen-spritesheets/effects/explosions/small-explosion/strict/grid/sprite-sheet.png` | Morte de `Drone` / explosões menores | Carregar grid `64×64`, 14 quadros |
| `pvfx-foundry-thirteen-spritesheets/effects/impacts/hit-spark/strict/grid/sprite-sheet.png` | Impacto de projéteis (`Impact("bullet")`) | Carregar grid `64×64`, 8 quadros |
| `pvfx-foundry-thirteen-spritesheets/effects/smoke/dash-dust/strict/grid/sprite-sheet.png` | Poeira de `Dash` e `Charger` | Carregar grid `68×32`, 13 quadros |
| `pvfx-foundry-thirteen-spritesheets/effects/smoke/dust-puff/strict/grid/sprite-sheet.png` | Poeira de pouso (`land`) | Carregar grid `72×40`, 14 quadros |
| `pvfx-foundry-thirteen-spritesheets/effects/fire/ground-flames/strict/grid/sprite-sheet.png` e `lava-burst` | Chamas/lava da Fase 3 (Fundição) | Carregar grid `64×40` / `64×72` em loop |
| `pvfx-foundry-thirteen-spritesheets/effects/ui/coin-pickup/strict/grid/sprite-sheet.png` | Efeito visual ao coletar moeda | Carregar grid `32×32`, 10 quadros |
| `pvfx-foundry-thirteen-spritesheets/effects/ui/treasure-glint/strict/grid/sprite-sheet.png` | Brilho contínuo sobre `MoedaEspecial` | Carregar grid `48×48`, 16 quadros (loop) |
| `kenney_crosshair-pack/PNG/Outline/crosshair-*.png` | Mira do mouse em `TelaJogo` | Carregar 1 textura escolhida com `scale=0.45` |
| `vacaroxa--generic-run-n-gun-pack--v.1.0/Enemies/SniperMob.png` e `ARMob.png` | Variantes visuais de `Shooter` e `Charger` | **Após confirmar licença:** fatiar e aplicar upscale nearest-neighbor ~2× |
| `vacaroxa--generic-run-n-gun-pack--v.1.0/Assets_area_2/tileset/tiles_out.png` | Caixote (`Cover`), `bridge.png` e plataformas industriais | **Após confirmar licença:** recortar regiões para `36×48` / `48×24` / `48×48` |
| `vacaroxa--generic-run-n-gun-pack--v.1.0/Assets_area_1/Tileset/Subway_tiles.png` | Tiles da Fase 3 (Fundição) | **Após confirmar licença:** recortar blocos `48×48` |

---

## 3. Assets Atuais Mantidos em `assets/`

- `player.png` (`960×128`, 10 quadros `96×128`) — **MANTER** (requisito POO obrigatório).
- `guard.png` (`96×128`), `boss.png` (`240×144`), `drone.png` (`78×66`) — **MANTER**.
- `ruins.png`, `desert.png`, `foundry.png`, `snow.png`, `arcade-menu.png` — **MANTER**.
- `stone.png` (`48×48`), `wall.png` (`48×48`) — **MANTER** (para Fase 1 Selva/Ruínas).
- `bridge.png` (`48×24`), `coin.png` (`27×27`) — **SUBSTITUIR** (por versão adaptada e sprite animado novo, respectivamente).
