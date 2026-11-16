# Auditoria Completa de Assets — Coin Commando

Este documento consolida o inventário técnico dos pacotes de assets locais disponíveis na pasta pai (`../`) e o cruzamento completo com todos os elementos visuais utilizados atualmente pelo **Coin Commando** (tanto arquivos em `assets/` quanto elementos desenhados proceduralmente em código).

> **Direção artística e restrições preservadas:**
> - Estética alvo: **2D pixel art militar run-and-gun clássica** (inspiração Metal Slug, sem cópia de assets protegidos).
> - Coerência de perspectiva (**side-view 2D**) e escala visual (sem misturar cartoon vetorial ou top-down).
> - Requisitos obrigatórios de POO preservados (`docs/REQUISITOS_OBRIGATORIOS.md`), em especial a spritesheet do protagonista em **quadros `96×128`** carregada via `arcade.load_spritesheet()` e `get_texture_grid()` (`idle=0`, `salto=1`, `caminhada=2..9`).

---

## Etapa 1 — Inventário dos Pacotes Locais (`../`)

Todos os 9 pacotes encontrados em `../` foram extraídos exclusivamente para a pasta temporária de auditoria `_audit_workspace/`, preservando integralmente os originais.

| Pacote | Formato | Licença encontrada | Estilo / Perspectiva | Compatibilidade Geral |
|---|---|---|---|---|
| `vacaroxa--generic-run-n-gun-pack--v.1.0.zip` | `.zip` | Não inclusa no `.zip` (verificar página Itch.io) | Pixel art 2D side-view militar/industrial | **Alta** (inimigos, tiles industriais, caixas, explosão) |
| `pvfx-foundry-thirteen-spritesheets.zip` | `.zip` | **CC0 1.0 Universal** (`LICENSE.txt`) | Pixel art VFX (`strict` = paleta limitada/alpha binário; `lit` = glow) | **Muito Alta** (explosões, impactos, poeira, fogo, pickups) |
| `kenney_crosshair-pack.zip` | `.zip` | **CC0 1.0 Universal** (`License.txt`) | Ícones 2D limpos (Dark / Outline / White) | **Alta** (miras de mouse em escala reduzida) |
| `vista-ten-1.0.0.zip` | `.zip` | **CC0 1.0 Universal** (`LICENCE.txt`) | Pixel art parallax 4 camadas (384×216 e `@3x` 1152×648) | **Média/Alta** (reserva para parallax multi-camada) |
| `helicopter.zip` | `.zip` | Não inclusa no `.zip` | Pixel art 2D side-view (96×32 por quadro, 8 quadros) | **Média** (veículo de extração/cutscene ou chefe aéreo) |
| `AssortedPixelArt.rar` | `.rar` | Não inclusa no `.rar` | Misto: tileset industrial 32×32, caverna 32×32, monstros fantasia, top-down 16×16 | **Parcial** (`IndustrialRuins_32x32.png` aproveitável; restante incompatível) |
| `Pixel Art - City Landscape V2.zip` | `.zip` | Não inclusa no `.zip` (`SpriteList.txt` apenas) | Pixel art parallax cidade noturna/entardecer (512px largura) | **Baixa** (sem fase urbana na campanha atual) |
| `kenney_tanksPack.zip` | `.zip` | **CC0 1.0 Universal** (`License.txt`) | Vetorial flat/cartoon liso | **Incompatível** (quebra a estética pixel art) |
| `Sprites.zip` | `.zip` | Não inclusa (`README.html` -> `yoogameart.com`) | Cartoon/chibi vetorizado pintado (250×250 / 246×297) | **Incompatível** (escala e estilo incompatíveis) |

### Detalhamento por pacote relevante

1. **`vacaroxa--generic-run-n-gun-pack--v.1.0`**
   - **Personagens/Inimigos:**
     - `Enemies/ARMob.png`: `768×38` (células `32×38` / `48×38`, ~20 poses úteis: idle, tiro horizontal, tiro vertical, corrida, morte, projétil).
     - `Enemies/RPGmob.png`: `440×44` (10 quadros `44×44`: idle, tiro bazuca, morte, foguete).
     - `Enemies/SniperMob.png`: `616×44` (14 quadros `44×44`: idle agachado, tiro sniper, morte, projétil).
     - `Player/SpriteSheet_player.png` (`360×315`) e `SpriteSheet_player_sliced.png` (`360×360`, 8×8 de `45×45`): animações de jogador run-and-gun, porém em escala menor e menos detalhado que o `assets/player.png` atual.
   - **Tilesets e Objetos:**
     - `Assets_area_1/Tileset/Subway_tiles.png` (`400×400`): plataformas metálicas, canos, placas verdes de sinalização, armários/painéis, grades, tijolos escuros.
     - `Assets_area_2/tileset/tiles_out.png` (`208×400`): **caixote de madeira**, **vigas com faixas amarelas/pretas**, **placa de perigo**, **cone**, plataformas de concreto com vegetação, cerca/água, poste.
   - **Efeitos:** `Enemies/Explosion_Particle.png` (`288×32`, 9 quadros `32×32`).
   - **Fundos:** `subway_BG.png` (`496×272`), `wall_subway.png` (`560×696`), `nuvens_1/2/3.png` (`496×272`).

2. **`pvfx-foundry-thirteen-spritesheets` (v1.0.0 + legacy 0.10.0)**
   - Cada efeito possui versão `lit` (com brilho/transparência suave) e `strict` (paleta limitada, alpha binário — ideal para pixel art), nos formatos `grid` (célula fixa + `manifest.json`) e `packed`.
   - **Destaques para o Coin Commando:**
     - Explosões: `explosions/big-explosion` (`18` quadros `128×128`, sheet `1024×384`), `explosions/small-explosion` (`14` quadros `64×64`, sheet `512×128`), `explosions/fire-nova` (`19` quadros `96×64`).
     - Impactos: `impacts/hit-spark` (`8` quadros `64×64`, sheet `512×64`), `impacts/blood-splat` (`16` quadros `128×120`), `impacts/rock-shatter` (`18` quadros `64×56`), `impacts/shockwave-ring` (`16` quadros `120×52`).
     - Poeira/Fumaça: `smoke/dash-dust` (`13` quadros `68×32`), `smoke/dust-puff` (`14` quadros `72×40`), `smoke/steam-vent` (`30` quadros `48×72`, loop).
     - Fogo (Fase 3 Fundição): `fire/flamethrower` (`16` quadros `128×48`, loop), `fire/ground-flames` (`16` quadros `64×40`, loop), `fire/lava-burst` (`23` quadros `64×72`).
     - UI / Pickups: `ui/coin-pickup` (`10` quadros `32×32`), `ui/heart-pickup` (`10` quadros `32×40`), `ui/treasure-glint` (`16` quadros `48×48`, loop).

3. **`kenney_crosshair-pack`**
   - `200` arquivos em `PNG/Dark/` (`64×64`), `PNG/Outline/` (`74×74`) e `PNG/White/` (`64×64`), além de spritesheets e vetores.

4. **`helicopter`**
   - `helicopter.png` (`768×32`, 8 quadros `96×32` com rotor animado), `separated_frames/helicopter_1..8.png`, e partes destruídas (`cabine.png` `64×32`, `helicopter_back.png` `32×32`, `door_16x16.png` `224×16`).

5. **`AssortedPixelArt`**
   - `IndustrialRuins_32x32.png` (`512×320`): tiles 32×32 de metal enferrujado, placas de aviso, grades de arame, tijolos escuros, lixeira/detritos.
   - `MyCaveTileset_32x32.png` (`512×512`), `monster_64x64.png` (`192×64`), `TopDownModernExterior_16x16.png` (`256×368`).

6. **`vista-ten-1.0.0`**
   - 10 cenários em 4 camadas (`0_sky`, `1_far`, `2_mid`, `3_near`) em `384×216` e `1152×648` (`@3x`): `cairn` (neve/montanha), `canopy` (floresta), `downs` (colinas), `flue` (chaminés industriais), `hollow` (cidade noturna), `kiln` (vulcânico/fornalha), `leeward` (costa), `mesa` (deserto/cânion), `sodium` (neblina), `tundra` (gelo/neve).

---

## Etapa 2 — Cruzamento e Classificação dos Elementos do Jogo

Critérios de classificação:
- **PRONTO**: pode ser integrado diretamente (no máximo ajuste de `scale` no carregamento).
- **ADAPTAR**: existe recurso adequado nos pacotes, mas requer recorte, redimensionamento nearest-neighbor, recoloração ou reorganização de spritesheet.
- **CRIAR**: nenhum recurso adequado foi encontrado nos pacotes (ou os existentes quebram a estética/escala).
- **MANTER**: o asset atual (ou solução visual atual) já é suficientemente bom e coerente.

### 2.1 Personagens e Inimigos

| Elemento no Jogo | Implementação Atual | Dimensão / Quadros Atuais | Candidato nos Pacotes | Status | Justificativa Técnica |
|---|---|---|---|---|---|
| **Protagonista (`Jogador`)** | `assets/player.png` (`actors.py`) | `960×128` (10 quadros `96×128`, scale `0.55`) | `vacaroxa/Player/SpriteSheet_player.png` (`45×45`) | **MANTER** | O sprite atual é mais detalhado, segue estética arcade clássica e cumpre literalmente o requisito POO (`96×128`, 10 quadros). |
| **Inimigo Guard (Padrão)** | `assets/guard.png` (`game.py`) | `96×128` (1 quadro estático, scale `0.55`) | `vacaroxa/Enemies/ARMob.png` (`32×38` animado) | **MANTER** (ou **ADAPTAR** para animar) | `guard.png` tem ótimo acabamento visual e combina perfeitamente com `player.png`, mas só tem 1 quadro. Recomenda-se manter `guard.png` para o guarda base ou criar seus quadros de caminhada/tiro; `ARMob` pode entrar como variante de tropa. |
| **Inimigo Shooter (Atirador)** | `assets/guard.png` com tint azul + mochila/antena via código (`polish.py`) | `96×128` (1 quadro) | `vacaroxa/Enemies/SniperMob.png` (`616×44`, 14 quadros) / `ARMob.png` | **ADAPTAR** | `SniperMob.png` dá identidade visual própria ao atirador (com animação de tiro e morte); precisa upscale nearest-neighbor ~2× e fatiamento em grid uniforme. |
| **Inimigo Charger (Investida)** | `assets/guard.png` com tint vermelho + cachecol via código (`polish.py`) | `96×128` (1 quadro) | `vacaroxa/Enemies/ARMob.png` (`768×38`) / `RPGmob.png` | **ADAPTAR** | `ARMob.png` (com recoloração/paleta vermelha) ou `RPGmob.png` oferece quadros de corrida e morte após upscale nearest-neighbor ~2×. |
| **Inimigo Drone** | `assets/drone.png` (`game.py`) | `78×66` (1 quadro, oscilação seno) | `helicopter/helicopter.png` (`96×32`, 8 quadros) | **MANTER** | `drone.png` tem design mech militar idêntico ao `boss.png`. O helicóptero é veículo tripulado grande demais em conceito para um drone pequeno; pode ser aproveitado como **ADAPTAR** para cutscene/extração. |
| **Chefão (`Boss` / Guardião Glacial)** | `assets/boss.png` (`game.py`) | `240×144` (1 quadro estático) | `kenney_tanksPack` (vetorial) | **MANTER** | `boss.png` é um tanque mech pixel art muito superior ao `kenney_tanksPack` (que é vetor flat incompatível). Faltam apenas quadros de dano/destruição se desejado evoluir no futuro. |

### 2.2 Cenários, Tilesets e Terreno

| Elemento no Jogo | Implementação Atual | Dimensão / Detalhes | Candidato nos Pacotes | Status | Justificativa Técnica |
|---|---|---|---|---|---|
| **Fundo Menu Principal** | `assets/arcade-menu.png` (`arcade_style.py`) | `1672×941` | `Pixel Art - City Landscape V2` | **MANTER** | `arcade-menu.png` já é pixel art industrial noturno de alta qualidade feito sob medida para a cena do menu. |
| **Fundo Fase 1 (Selva/Ruínas)** | `assets/ruins.png` | `1536×1024` | `vista-ten/canopy` | **MANTER** | `ruins.png` tem ruínas, cachoeira e antena militar alinhadas ao tema; `vista-ten` fica como opção caso se implemente parallax 4 camadas. |
| **Fundo Fase 2 (Deserto)** | `assets/desert.png` | `2172×724` | `vista-ten/mesa` | **MANTER** | Fundo atual já atende perfeitamente ao tema deserto. |
| **Fundo Fase 3 (Fundição)** | `assets/foundry.png` | `1672×941` | `vista-ten/kiln` / `flue` | **MANTER** | `foundry.png` é extremamente detalhado (fornalhas, lava, correntes). |
| **Fundo Fase 4 (Glacial)** | `assets/snow.png` | `1672×941` | `vista-ten/tundra` / `cairn` | **MANTER** | Fundo atual já entrega estética glacial militar coerente. |
| **Chão/Plataforma Fase 1 (Selva)** | `assets/stone.png` + `assets/wall.png` | `48×48` | `vacaroxa/tiles_out.png` (bloco com folhagem) | **MANTER** | `stone.png` e `wall.png` são literalmente pedra de ruínas com musgo no tamanho exato `48×48`. |
| **Chão/Plataforma Fase 2 (Deserto)** | `stone.png` + tint `(240,184,131)` + cap areia via código | `48×48` | Nenhum específico de deserto nos pacotes | **CRIAR** | Hoje depende de tinting genérico; um tile `48×48` de arenito/bunker desértico dará identidade própria à Fase 2. |
| **Chão/Plataforma Fase 3 (Fundição)** | `stone.png` + tint azulado + rebites via código | `48×48` | `vacaroxa/Subway_tiles.png` e `AssortedPixelArt/IndustrialRuins_32x32.png` | **ADAPTAR** | Ambos os pacotes têm vigas metálicas, chapas com faixas amarelas/pretas e blocos industriais. Basta recortar e ajustar para `48×48`. |
| **Chão/Plataforma Fase 4 (Glacial)** | `stone.png` + tint azul claro + cap neve via código | `48×48` | Nenhum tile de gelo/neve nos pacotes | **CRIAR** | Nenhum pacote traz tileset `48×48` de gelo/bunker ártico. |
| **Plataforma Ponte (`bridge.png`)** | `assets/bridge.png` + postes/cordas por código | `48×24` | `vacaroxa/tiles_out.png` (plataforma metálica/passarela) | **ADAPTAR** | `bridge.png` atual é muito simples (3 tons lisos). Passarelas de `tiles_out.png` ou `IndustrialRuins_32x32.png` podem ser recortadas para `48×24`. |

### 2.3 Coletáveis, Objetos de Cena e Perigos (Atualmente Sprites Simples ou Código)

| Elemento no Jogo | Implementação Atual | Dimensão / Detalhes | Candidato nos Pacotes | Status | Justificativa Técnica |
|---|---|---|---|---|---|
| **Moeda Comum (`coin.png`)** | `assets/coin.png` | `27×27` (1 quadro, bob seno) | `pvfx/ui/coin-pickup` (efeito de coleta, não a moeda em si) | **CRIAR** | `coin.png` atual é estática (1 quadro). Falta spritesheet giratória de moeda militar/dourada (4–8 quadros `28×28` ou `32×32`) para dar vida ao coletável principal do jogo. |
| **Moeda Especial (`MoedaEspecial`)** | `assets/coin.png` em `scale=1.2` | ~`32×32` | `pvfx/ui/treasure-glint` (overlay de brilho) | **CRIAR** (sprite) + **PRONTO** (brilho PVFX) | Precisa de visual distinto da moeda comum (ex: estrela/medalha/moeda rubi ou platina giratória). |
| **Cobertura / Barricada (`Cover`)** | Retângulo + rebites por código (`combat.py`) | `36×48` | `vacaroxa/tiles_out.png` (caixote de madeira) | **ADAPTAR** | Há um caixote de madeira pixel art pronto dentro de `tiles_out.png`; basta recortar e ajustar para `36×48` (ou `48×48`). |
| **Barril Explosivo (`Barrel`)** | Retângulo vermelho + triângulo por código (`world_fx.py`) | `24×34` | `kenney_tanksPack` (vetorial - descartado) | **CRIAR** | Nenhum barril pixel art compatível foi encontrado nos pacotes (`kenney_tanksPack` é vetor flat). |
| **Caixa de Suprimentos / Loja (`draw_supply`)** | Retângulo verde + texto `[B] LOJA` (`game.py`) | `42×32` | `vacaroxa/tiles_out.png` / `Subway_tiles.png` | **ADAPTAR** | Pode usar caixote militar adaptado + ícone de munição/loja. |
| **Bandeira de Saída (`draw_exit`)** | Mastro + triângulo por código (`game.py`) | `~144px` altura | `helicopter/helicopter.png` (extração) ou sprite próprio | **CRIAR** (bandeira/portal) / **ADAPTAR** (heli) | Não há bandeira/heliponto animado nos pacotes; `helicopter.png` pode complementar a extração no fim da fase. |
| **Perigos: Mina, Espinhos, Emissor Laser** | `SpriteSolidColor` + formas geométricas (`world_fx.py`) | Mina `42×15`, Espinhos `42×15`, Laser `34×16` + feixe | Nenhum pixel art específico (apenas mina vetorial em `kenney_tanksPack`) | **CRIAR** | Criar sprites pixel art pequenos (mina com LED animado 2 quadros, espinhos metálicos, emissor de laser industrial). |

### 2.4 Armas, Projéteis e Efeitos Visuais (VFX)

| Elemento no Jogo | Implementação Atual | Detalhes | Candidato nos Pacotes | Status | Justificativa Técnica |
|---|---|---|---|---|---|
| **Armas na mão do jogador** | `weapon_art.py` (PIL `54–66×27`) | 4 armas (`AK-47`, `SMG`, `Shotgun`, `Rifle`) + mãos | Nenhum pacote traz armas isoladas compatíveis | **MANTER** | `weapon_art.py` já gera pixel art limpo, com cache e alinhado ao sistema de mira angular do jogador. |
| **Granada (`Grenade`)** | Formas geométricas (`18×18`, `combat.py`) | Corpo + pino + LED piscante | Nenhum nos pacotes | **CRIAR** | Sprite pequeno (`16×16` ou `20×20`, 2–4 quadros rotacionando) elevaria muito o acabamento em combate. |
| **Faca arremessada (`Knife`)** | Linhas + triângulo (`24×4`, `combat.py`) | Rotaciona em voo | Nenhum nos pacotes | **MANTER** (ou **CRIAR** opcional) | O desenho vetorial em `24×4` é rápido e legível em movimento, baixa prioridade para substituir. |
| **Projéteis / Traços de Bala** | 3 linhas sobrepostas (`combat.py`) | AK, SMG, Shotgun, Rifle, Hostil | `pvfx/projectiles` (fantasia/mágico) | **MANTER** | Traçantes procedurais funcionam melhor que sprites estáticos em qualquer ângulo de mira; os do PVFX são mágicos/flechas. |
| **Explosões (`Impact` / `Barrel` / `Grenade`)** | Círculos concêntricos + 7 quadrados (`combat.py`) | 0.5s | `pvfx/explosions/big-explosion` (`128×128`, 18q) e `small-explosion` (`64×64`, 14q) — variante `strict` | **PRONTO** | Substituição direta via `arcade.load_spritesheet()` usando a versão `strict` (pixel art). |
| **Faíscas de Impacto (`Impact("bullet")`)** | 6 linhas radiais amarelas (`combat.py`) | 0.2s | `pvfx/impacts/hit-spark` (`64×64`, 8q) e `rock-shatter` (`64×56`, 18q) | **PRONTO** | Substituição direta de altíssima qualidade visual. |
| **Poeira de Dash / Pouso / Corrida** | Quadrados/linhas simples (`effects.py`, `polish.py`) | `0.15s–0.4s` | `pvfx/smoke/dash-dust` (`68×32`, 13q) e `dust-puff` (`72×40`, 14q) | **PRONTO** | Encaixa perfeitamente no dash e no Charger. |
| **Efeito de Coleta de Moeda / Vida** | Partículas quadradas (`effects.py`) | `2–5px` | `pvfx/ui/coin-pickup` (`32×32`, 10q), `heart-pickup` (`32×40`, 10q), `treasure-glint` (`48×48`, 16q) | **PRONTO** | Dá feedback arcade instantâneo ao coletar moedas e curas. |
| **Chamas / Vapor na Fundição (Fase 3)** | Retângulo laranja pulsante no chão (`game.py`) | Glow simples | `pvfx/fire/ground-flames`, `lava-burst`, `smoke/steam-vent` | **PRONTO** | Substitui o retângulo simples de lava por animação pixel art real. |
| **Muzzle Flash (Clarão de Tiro)** | Polígono estrela 10 pontas (`combat.py`) | `0.025s–0.055s` | Nenhum específico nos pacotes | **MANTER** | O clarão procedural escala por arma e rotaciona com o cano perfeitamente. |

### 2.5 Interface (HUD, Mira e Menus)

| Elemento no Jogo | Implementação Atual | Detalhes | Candidato nos Pacotes | Status | Justificativa Técnica |
|---|---|---|---|---|---|
| **Mira do Mouse (`Crosshair`)** | Círculo + 4 linhas (`game.py`) | `~30×30` | `kenney_crosshair-pack/PNG/Outline/` (`74×74`) e `Dark/` (`64×64`) | **PRONTO** | Basta carregar um dos 200 arquivos com `scale=0.45`–`0.5`. |
| **Fonte Bitmap Pixel Art (`lettering`)** | Gerada via PIL (`arcade_style.py`) | `5×7` estilizada | Nenhum pacote de fonte | **MANTER** | Sistema próprio já entrega estilo arcade metálico/dourado com cache. |
| **Corações de Vida no HUD** | Polígono 8 pontas (`game.py`, `arcade_style.py`) | Cheio / Vazio | `pvfx/ui/heart-pickup` (apenas efeito) | **MANTER** (ou **CRIAR** ícone pixel art 16×16 se desejar) | Os corações atuais são bem legíveis; substituir por sprite pixel art 16×16 é melhoria opcional de baixa prioridade. |
| **Ícones das Armas na Loja/HUD** | `weapon_art.py` | 4 armas | Nenhum | **MANTER** | Já são pixel art gerados com detalhe (coronha, carregador, mira). |
| **Ícones dos Botões do Menu** | Formas geométricas (`arcade_style.py`) | Play, Loja, Opções, Sobre | Nenhum pacote de ícones UI | **MANTER** | Coerentes com a estética de gabinete arcade. |

---

## Resumo Quantitativo da Auditoria

- **MANTER:** 17 elementos (protagonista `96×128`, `guard.png`, `boss.png`, `drone.png`, 5 fundos de fase/menu, `stone.png`/`wall.png` da Fase 1, `weapon_art.py`, traçantes de bala, muzzle flash, fonte pixel art, UI/botões).
- **PRONTO (Integração Direta):** 7 famílias de recursos (`pvfx` explosões, impactos, poeira/fumaça, fogo/vapor da fundição, efeitos de pickup/brilho, e `kenney_crosshair-pack` para mira).
- **ADAPTAR (Ajuste/Recorte/Escala):** 6 elementos (inimigos `Shooter`/`Charger` via `vacaroxa`, tiles industriais da Fase 3 via `Subway_tiles`/`IndustrialRuins`, ponte `bridge.png`, cobertura `Cover`, caixa de suprimentos, helicóptero de extração opcional).
- **CRIAR (Produção Manual Necessária):** 7 itens específicos (moeda comum animada, moeda especial animada, tileset `48×48` Deserto, tileset `48×48` Glacial, barril explosivo, perigos — mina/espinhos/emissor laser —, granada arremessável e bandeira de saída).

> **Conclusão:** Cerca de **75% das lacunas visuais** (principalmente VFX de combate, mira, inimigos variantes, caixotes e tiles industriais) já podem ser resolvidas com os pacotes gratuitos locais, reduzindo a produção manual ao mínimo essencial listado em [`docs/MISSING_ASSETS.md`](MISSING_ASSETS.md).
