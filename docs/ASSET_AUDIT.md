# Coin Commando — auditoria de assets locais

> Histórico de produção preservado. Estrutura atual: `assets/README.md` e
> `docs/README.md`. Arquivos V5–V8 ficam em `assets/archive/`; relatórios, em `docs/history/`.

**Data da auditoria:** 10/11/2026  
**Escopo:** arquivos compactados encontrados em `../`, material extraído em
`_audit_workspace/` e recursos atualmente usados pelo jogo. Nenhum arquivo
original foi movido, sobrescrito ou removido. A auditoria não altera o jogo.

## Conclusão executiva

| Sistema visual | Decisão | Evidência principal |
| --- | --- | --- |
| Protagonista | **MANTER** | `assets/player.png` é exatamente `960x128`: 10 células `96x128`, requisito obrigatório da atividade. Os candidatos usam células `250x250`, `340x250` ou uma folha `360x315`. |
| Guard/shooter/charger | **ADAPTAR** | `Sprites` fornece soldado com idle, run, jump, fall, climb, crawl e death; `Terrorist` fornece idle/run. Nenhum usa o contrato `96x128` nem a mesma escala visual. |
| Drone | **CRIAR** | Não há drone voador militar equivalente. O helicóptero é um veículo horizontal, não substitui o inimigo e não tem o mesmo enquadramento. |
| Boss | **CRIAR** | Não há criatura/chefe grande coerente com o guardião atual. Tanques são veículos top-down e não substituem o boss humanoide. |
| Fundos | **ADAPTAR** | `vista-ten` e `Pixel Art - City Landscape V2` têm fundos em camadas, mas exigem composição, recorte e ajuste de escala para `960x640`. Os quatro fundos atuais já são coerentes entre si. |
| Tiles/plataformas | **ADAPTAR** | `vacaroxa` oferece tilesets `400x400`/`208x400` e `AssortedPixelArt` oferece tilesets `32x32`, mas não há equivalência 1:1 para os blocos atuais de `48x48`/`48x24`. |
| Crosshair | **PRONTO** | O Kenney Crosshair Pack possui PNGs individuais, animações e licença CC0; pode substituir o desenho procedural sem mudar colisão ou input. |
| Explosões/impactos | **ADAPTAR** | PVFX Foundry oferece 101 efeitos, 1.826 frames por tier e manifestos JSON; precisa de um adaptador para os tempos/pivôs do sistema `Impact`. |
| Minas/barris/props | **ADAPTAR** | Kenney Tanks possui minas `36x14`, barris/caixas e explosões, mas é visualmente top-down e exige ajuste de escala/colisão. |
| Helicóptero | **ADAPTAR** | Há folha `768x32` e oito frames separados `96x32`; útil como decoração/veículo novo, não como substituição de entidade existente. |
| Moeda | **MANTER** | Nenhum pacote oferece uma moeda militar/pixel-art melhor compatível; `assets/coin.png` é pequeno, legível e já integrado. |
| Armas | **MANTER** | As quatro armas são desenhadas proceduralmente em `weapon_art.py`, com geometria alinhada ao muzzle e ao balanceamento. Não há pacote de armas laterais coerente. |
| HUD/UI | **MANTER** | Os elementos são desenhados pela interface e o menu usa a composição atual. Crosshair é a única troca claramente segura. |

## Inventário dos pacotes

| Pacote original | Conteúdo identificado |
| --- | --- |
| `AssortedPixelArt.rar` | 4 PNGs: ruínas industriais `416x256`, monstro `192x64`, tileset de caverna `512x512` e exterior top-down `256x256`. |
| `helicopter.zip` | 1 folha `768x32`, 8 frames `96x32`, peças quebradas `64x32`, `32x32` e `224x16`. |
| `kenney_crosshair-pack.zip` | 2.013 arquivos; PNGs Dark/Light/Color, folhas de tiles e vetores. Animações de mira com quadros individuais. |
| `kenney_tanksPack.zip` | 186 arquivos; tanques, torres, tracks, projéteis, minas, barris, caixas e explosão de 12 quadros; versões Default/Retina, spritesheets e vetores. |
| `Pixel Art - City Landscape V2.zip` | 10 PNGs em camadas de céu, nuvens, prédios e sombras; imagens entre `512x54` e `512x405`. |
| `pvfx-foundry-thirteen-spritesheets.zip` | 101 efeitos, dois tiers (`lit`/`strict`), folhas grid/packed, manifestos com frame count, duração, pivô e bounds; 404 PNGs de folhas mais legado. |
| `Sprites.zip` | Soldado do exército e terrorista, folhas e PNGs por frame. Exército: idle, run, jump, fall, climb, crawl e death. Terrorista: 13 idle e 21 run. |
| `vacaroxa--generic-run-n-gun-pack--v.1.0.zip` | Player, três inimigos, explosão, dois tilesets e fundos de metrô/nuvens. As folhas de personagem são strips compactos. |
| `vista-ten-1.0.0.zip` | 10 conjuntos de paisagens em camadas; 50 PNGs `384x216` e cópias `1152x648`, com paletas `.gpl`; licença CC0-1.0. |

## Comparação com o jogo

O jogo usa atualmente:

- `player.png`, `guard.png`, `drone.png`, `boss.png`, `coin.png`;
- `ruins.png`, `desert.png`, `foundry.png`, `snow.png`;
- `stone.png`, `wall.png`, `bridge.png`;
- armas, projéteis, granadas, minas, lasers, espinhos, barris, partículas,
  impactos e mira desenhados por código;
- spritesheet do protagonista carregada por `load_spritesheet()` e
  `get_texture_grid()` com células `96x128`.

Os candidatos devem permanecer em `_audit_workspace/` até haver decisão de
integração, revisão de licença e teste visual. A galeria local está em
[asset_gallery.html](./asset_gallery.html).

## Ordem recomendada

1. Integrar o crosshair Kenney como teste de baixo risco.
2. Fazer um protótipo isolado dos soldados `Sprites`, preservando a folha
   `player.png` e medindo escala, silhueta e ancoragem.
3. Adaptar PVFX Foundry para `Impact`/explosões, usando os manifestos e
   filtragem nearest-neighbour.
4. Só então decidir se algum fundo/tileset substitui uma fase inteira; não
   misturar `vista-ten`, `Kenney` top-down e os fundos atuais na mesma cena.
5. Produzir manualmente apenas drone, boss e qualquer novo protagonista que
   mantenha o contrato `96x128`.

## Limitações e riscos

- `vacaroxa`, `Sprites`, `helicopter`, `AssortedPixelArt` e `Pixel Art - City
  Landscape V2` não trazem um arquivo de licença explícito no conteúdo
  extraído; não devem ser publicados antes de confirmar a licença na página de
  origem.
- A auditoria é estática e a galeria é local; não foi declarado teste visual
  do jogo.
- O banco `ranking.db` real não foi tocado.

## Atualização V5-A — 10/11/2026 (substitui decisões anteriores para o protagonista/UI)

- **Commando: INTEGRADO.** Folha RGBA 960×128, 10 células; autor usuário, autorização
  confirmada. Ajuste vertical +6 px e colisão anterior preservada. Não é só candidato.
- **Drone: QUARENTENA TÉCNICA.** 384×128 RGBA; cortes de 48×128 atravessam silhuetas.
  A imagem contém duas fileiras e quatro colunas aparentes (96×64), não oito colunas.
  Confirmar ordem e margem em V5-C; não alterar IA/granadas agora.
- **Iron Commander: QUARENTENA TÉCNICA.** 1152×320 RGBA; cortes de 144×320 atravessam
  silhuetas. Aparência de quatro colunas por duas linhas (288×160). Não comprova
  idle/hurt/death nem ordem temporal. V5-E deve validar ataque, chão e hitbox.
- Licenças locais Kenney Crosshair/Tanks, PVFX e vista-ten relidas. Nenhum arquivo
  desses packs foi integrado nesta sprint. PVFX tem escopo explícito por arquivos;
  vista-ten declara CC0 e também observação contra revenda do pack: conservar o texto.
- Pacotes sem licença explícita continuam bloqueados; tanques top-down continuam
  inadequados como substitutos laterais. Sem reextração nem varredura de crosshairs.
- Evidência: `evidence/v5-a/contact-sheet.png`, `assets.json`, `menu-after.png`,
  `weapons-after.png`. Revisão visual estática feita; não equivale a playtest humano.

## V5-B — integração de interface
Quatro sprites CC0 Kenney promovidos: munição/proteção/reparo como ícones e crosshair.
Perspectiva de veículos não reutilizada como personagem lateral. Demais candidatos
continuam com suas restrições anteriores. V5B_CHANGELOG.md documenta arquivos e QA.

## V6 — decisões atualizadas
Drone e Iron Commander saíram da quarentena técnica após validar grade4×2.
Protagonista escolar preservado. Bandidos, armas e props têm folhas geradas próprias.
PVFX explosão/impactos e caixa Kenney integrados; ver V6_CHANGELOG.md e sources.json.
