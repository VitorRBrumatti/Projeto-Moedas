# Assets

| Pasta/arquivo | Uso |
| --- | --- |
| sprites/ | Folhas usadas pelo jogo; sprites.json define dimensões, frames e FPS |
| ui/ | Ícones do HUD e menus |
| audio/ | Sons e marcha do menu |
| licenses/ | Textos de licença de terceiros, preservados sem alteração |
| sources.json | Caminhos atuais, autoria/permissão, origem anterior e SHA-256 |
| archive/ | Fontes/versões preservadas localmente, ignoradas pelo Git |
| PNGs na raiz | Bases originais, fundos e compatibilidade de hitboxes |

O jogo não carrega arquivos de archive/. Fontes e versões antigas foram preservadas;
a limpeza reorganizou os caminhos, sem redesenhar sprites ou sintetizar áudio novo.
`player.png` original continua na raiz para o contrato/hitbox da atividade;
o protagonista visível está em `sprites/player.png`.

Mapeamento antes/depois: [ASSET_RELOCATION.json](../docs/ASSET_RELOCATION.json).
Detalhes históricos: [ASSET_SOURCES.md](../docs/ASSET_SOURCES.md).
Pastas locais ignoradas, como `_staging_v5/`, não fazem parte da distribuição.
