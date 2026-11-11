# Coin Commando — fontes e licenças dos assets

Os arquivos originais estão na pasta pai do projeto. As cópias usadas para
inventário ficam em `_audit_workspace/`; elas são apenas material de trabalho.

| Pacote | Fonte local | Licença encontrada | Uso recomendado |
| --- | --- | --- | --- |
| Kenney Crosshair Pack | `../kenney_crosshair-pack.zip` | CC0 em `License.txt` | Crosshair, sem restrição de atribuição; creditar Kenney é recomendado. |
| Kenney Tanks | `../kenney_tanksPack.zip` | CC0 em `License.txt` | Minas, barris, caixas, explosões e veículos decorativos; adaptar perspectiva. |
| PVFX Foundry | `../pvfx-foundry-thirteen-spritesheets.zip` | CC0 para folhas/metadados em `README.md` e `LICENSE.txt`; toolkit citado é MIT | Efeitos, respeitando manifestos e a separação `lit`/`strict`. |
| vista-ten | `../vista-ten-1.0.0.zip` | CC0-1.0 em `LICENCE.txt` e nos `.json` | Fundos em camadas; adaptar para a câmera de `960x640`. |
| Sprites | `../Sprites.zip` | Não encontrado dentro do pacote | Não integrar/publicar até confirmar a licença na fonte original. |
| Generic Run 'n Gun | `../vacaroxa--generic-run-n-gun-pack--v.1.0.zip` | Não encontrado dentro do pacote | Não integrar/publicar até confirmar a licença na fonte original. |
| Helicopter | `../helicopter.zip` | Não encontrado dentro do pacote | Uso condicionado à confirmação da licença. |
| Assorted Pixel Art | `../AssortedPixelArt.rar` | Não encontrado dentro do pacote | Uso condicionado à confirmação da licença. |
| Pixel Art - City Landscape V2 | `../Pixel Art - City Landscape V2.zip` | Não encontrado dentro do pacote | Uso condicionado à confirmação da licença. |

## Rastreabilidade

- A auditoria foi feita sobre os nove arquivos compactados presentes em
  `Z:\ProjetoHermesJogo`.
- O `.rar` foi correlacionado com a pasta de trabalho já extraída
  `_audit_workspace/AssortedPixelArt/`; o arquivo original permaneceu intacto.
- Não foram baixados assets adicionais nem geradas imagens por IA.
- Antes de copiar qualquer arquivo para `assets/`, confirmar os termos na
  página de origem e registrar a atribuição necessária no projeto.

## Integração efetiva V5-A — 10/11/2026

| Fonte / caminho interno | Autor / permissão | Arquivo integrado | Adaptação |
| --- | --- | --- | --- |
| PNG avulso `../commando_unarmed_10f_960x128.png` (não pertence a ZIP/RAR) | Usuário Vitor, confirmou autoria e autorizou uso/modificação/redistribuição nesta sessão; sem licença padronizada declarada | `assets/v5/commando.png` | +6 px Y, RGBA; células mantidas; original intacto |

SHA-256 fonte: `614cb031152f03be6f677deea98b281b919fecdf5fe07cde2a8954efb385cdaa`.
SHA-256 integrado: `4db7666af7a49cde7322d1d4e2d419d50fa04eacc128011306c2e6518a77a943`.
Registro verificável: `assets/v5/sources.json`. Não há URL de origem externa conhecida.
Drone/boss também têm autoria confirmada, porém não foram integrados por incompatibilidade
da grade presumida. Fundo `assets/ruins.png` e armas locais foram reutilizados, não importados
de packs. Nenhum ZIP/RAR forneceu arquivo novo ao runtime nesta sprint.

## V5-B — quatro PNGs Kenney integrados
Munição, proteção e reparo: kenney_tanksPack.zip / PNG/Default size/tanks_crate{Ammo,Armor,Repair}.png.
Mira: kenney_crosshair-pack.zip / PNG/Outline/crosshair-002.png.
CC0 conferida nos License.txt locais, copiados em assets/v5/. Autor Kenney (kenney.nl).
Destinos ammo.png, armor.png, repair.png e crosshair.png em assets/v5/.
Hashes, caminhos exatos e recorte alpha da mira em assets/v5/sources.json.
Uso real no HUD/loja/mira; ver V5B_CHANGELOG.md e evidências.

## V6 — geração e integração real
Sprites novos em assets/v6/, incluindo armas, props e bandido gerados via built-in image_gen.
Drone/Iron Commander próprios integrados com grade4×2 validada. PVFX explosão/impactos
e Kenney cobertura/projétil adaptados sob suas licenças. Registro por arquivo, hash
e fonte em assets/v6/sources.json; briefs em generation-prompts.md. Originais intactos.

## Revisão V7
Folhas novas de combatente e ponte via built-in image_gen em assets/v7; fontes intactas,
hashes/briefs na mesma pasta. Combatente possui7frames reais por estado, ponte8.
Traçante é adaptação com contraste do raster V6. Ver V7_CORRECOES.md.

## V8
Plataformas/parede/caixa militar geradas por built-in image_gen; derivados e fonte
em assets/v8, com hashes e brief. Insígnia é adaptação de contraste do raster V6.
Original preservado; mapeamento ativo em assets/v6/sprites.json.
