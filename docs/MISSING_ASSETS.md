# Assets Faltantes para Produção Manual — Coin Commando

Este documento lista **exclusivamente** os sprites que ainda precisam de criação original (classificação **CRIAR** em [`ASSET_AUDIT.md`](ASSET_AUDIT.md)), após aproveitar ao máximo os pacotes gratuitos locais.

Todos os itens abaixo devem seguir a estética **2D pixel art militar run-and-gun** (contorno escuro, sombreamento nítido, perspectiva *side-view* e escala compatível com o protagonista `96×128` exibido em `scale=0.55`).

---

## 1. Moeda Comum Animada (`coin.png`)
- **Função no jogo:** Coletável principal das fases (requisito obrigatório P1: mínimo 25 moedas por fase, +1 ponto e moeda da loja). Substitui o sprite estático atual (`27×27`, 1 quadro).
- **Dimensões recomendadas:** `32×32` por quadro (spritesheet horizontal `192×32` ou `256×32`).
- **Quadros necessários:** 6 a 8 quadros.
- **Animações necessárias:** Rotação contínua em eixo vertical (360° em loop suave) com brilho dourado especular.
- **Prioridade:** **Alta** (elemento central do título e da mecânica do jogo).
- **Possibilidade de adaptar algum sprite existente:** Não há moeda pixel art nos pacotes baixados. O efeito de coleta `pvfx/ui/coin-pickup` (`32×32`, 10 quadros) complementará a moeda quando ela for pega.

## 2. Moeda Especial Animada (`coin_special.png`)
- **Função no jogo:** `MoedaEspecial` móvel que rebate nas bordas (+5 pontos, requisito P1). Atualmente reutiliza `coin.png` ampliada (`scale=1.2`).
- **Dimensões recomendadas:** `36×36` ou `32×32` por quadro (spritesheet `192×32` ou `216×36`).
- **Quadros necessários:** 6 quadros.
- **Animações necessárias:** Rotação em loop com cor/silhueta distinta da moeda comum (ex.: medalhão militar platina/rubi ou moeda com estrela central).
- **Prioridade:** **Média** (funciona com `coin.png` escalada, mas visual próprio evita confusão na tela).
- **Possibilidade de adaptar algum sprite existente:** Sim, **parcialmente** — pode ser derivada por recoloração e adição de detalhe (estrela/borda) sobre a nova `coin.png` criada, somada ao brilho em loop `pvfx/ui/treasure-glint`.

## 3. Tileset Deserto (`desert_stone.png` / `desert_wall.png`)
- **Função no jogo:** Chão, paredes de sustentação e plataformas da **Fase 2 (Deserto)**, substituindo o reaproveitamento atual de `stone.png` com tinting marrom.
- **Dimensões recomendadas:** `48×48` por tile (bloco de piso + bloco de preenchimento inferior).
- **Quadros necessários:** 1 quadro por tile (2 a 3 variações estáticas opcionais: topo com areia, bloco trincado, parede interna).
- **Animações necessárias:** Nenhuma (estático).
- **Prioridade:** **Alta** (eleva drasticamente a identidade visual da Fase 2).
- **Possibilidade de adaptar algum sprite existente:** Baixa — nenhum pacote local possui tileset `48×48` de arenito/bunker desértico. No máximo, `stone.png` atual serve de referência de proporção e encaixe.

## 4. Tileset Glacial (`snow_stone.png` / `snow_wall.png`)
- **Função no jogo:** Chão, paredes e plataformas da **Fase 4 (Glacial)**, substituindo `stone.png` com tinting azul claro + retângulo de neve por código.
- **Dimensões recomendadas:** `48×48` por tile (bloco de piso com camada de neve/gelo + bloco de preenchimento rocha/gelo).
- **Quadros necessários:** 1 quadro por tile (2 variações opcionais).
- **Animações necessárias:** Nenhuma (estático).
- **Prioridade:** **Alta** (a Fase 4 é a fase do Chefão Final).
- **Possibilidade de adaptar algum sprite existente:** Baixa — não há tiles de neve/gelo nos pacotes baixados.

## 5. Barril Explosivo (`barrel.png`)
- **Função no jogo:** Objeto destrutível de cenário (`Barrel` em `world_fx.py`) que explode ao receber dano e causa dano em área. Atualmente desenhado com retângulos e triângulo por código.
- **Dimensões recomendadas:** `24×34` ou `32×40` por quadro (spritesheet `96×40` se tiver estado danificado).
- **Quadros necessários:** 1 quadro base (opcional: +2 quadros de estado amassado/piscando antes de explodir).
- **Animações necessárias:** Estático (ou alerta piscante pré-detonação); a explosão em si já está coberta por `pvfx/explosions/big-explosion`.
- **Prioridade:** **Média-Alta** (muito visível no gameplay).
- **Possibilidade de adaptar algum sprite existente:** Não recomendado adaptar dos pacotes atuais: o único barril presente está em `kenney_tanksPack`, que é estilo vetorial liso incompatível com pixel art.

## 6. Conjunto de Perigos (`mine.png`, `spikes.png`, `laser_emitter.png`)
- **Função no jogo:** Obstáculos e armadilhas de fase (`Hazard` em `world_fx.py`), atualmente desenhados com `SpriteSolidColor` e triângulos/linhas.
- **Dimensões recomendadas:**
  - `mine.png`: `42×16` (ou `36×16`) por quadro.
  - `spikes.png`: `48×16` (tileável com blocos `48×48`).
  - `laser_emitter.png`: `36×18` por quadro (o feixe do laser pode continuar procedural/glow).
- **Quadros necessários:**
  - Mina: 2 quadros (LED apagado / LED vermelho aceso).
  - Espinhos: 1 quadro estático (opcional: +1 quadro com sangue/brilho metálico).
  - Emissor Laser: 2 quadros (standby / carregando-ativo).
- **Animações necessárias:** Piscar do LED da mina e estado ativo do emissor laser.
- **Prioridade:** **Média** (melhora leitura de perigo e acabamento visual).
- **Possibilidade de adaptar algum sprite existente:** Baixa — apenas `kenney_tanksPack` tem mina (vetorial incompatível) e `AssortedPixelArt/MyCaveTileset_32x32.png` tem estalactites de pedra orgânica (não são espinhos metálicos militares).

## 7. Granada Arremessável (`grenade.png`)
- **Função no jogo:** Projétil parabólico do jogador (`Grenade` em `combat.py`), atualmente desenhado com retângulo verde e círculo de brilho por código.
- **Dimensões recomendadas:** `18×18` ou `20×20` por quadro.
- **Quadros necessários:** 4 quadros (rotação de 90° por quadro) + opcional LED vermelho piscando.
- **Animações necessárias:** Giro no ar em loop enquanto quica/cai; ao detonar, usa `pvfx/explosions/big-explosion`.
- **Prioridade:** **Média**.
- **Possibilidade de adaptar algum sprite existente:** Nenhuma nos pacotes locais.

## 8. Bandeira / Portal de Saída (`exit_flag.png`)
- **Função no jogo:** Marcador de conclusão do setor (`draw_exit` em `game.py`), atualmente um retângulo cinza com triângulo.
- **Dimensões recomendadas:** `48×144` por quadro (spritesheet `192×144` ou `240×144`).
- **Quadros necessários:** 4 quadros por estado (bandeira abaixada/travada vs bandeira hasteada tremulando ao liberar os 70% de moedas).
- **Animações necessárias:** Tremular contínuo da bandeira ao vento + transição/luz verde quando desbloqueada.
- **Prioridade:** **Baixa-Média** (o jogador vê em todas as fases, mas o marcador atual já é funcional).
- **Possibilidade de adaptar algum sprite existente:** Alternativamente, pode-se **ADAPTAR** `helicopter/helicopter.png` (`96×32`, 8 quadros) como ponto de extração aérea no final da fase (desde que validada a licença de `helicopter.zip`).

---

## Itens Opcionais (Melhorias Futuras — Não Bloqueantes)

Estes itens **não são necessários** para substituir desenhos geométricos, pois os assets atuais ou procedurais já cumprem bem o papel, mas podem ser produzidos caso se busque polimento extra:
- **Animações extras para `guard.png` e `boss.png`**: caminhada, tiro e destruição para `guard.png` (`96×128`) e `boss.png` (`240×144`), já que hoje possuem 1 quadro cada.
- **Ícone de Coração HUD (`heart_hud.png`)**: `16×16`, 2 quadros (cheio/vazio), substituindo o polígono procedural de 8 pontas.
