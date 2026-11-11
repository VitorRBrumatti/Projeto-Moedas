# COIN COMMANDO V5 — ASSET INTEGRATION, ARCADE VISUAL OVERHAUL & CINEMATIC POLISH

## PAPEL E MISSÃO

Atue como uma equipe de desenvolvimento coordenada por um Tech Lead: Game Director, Senior Python Arcade Developer, Technical Pixel Artist, UI/UX Designer de jogos arcade, Animation Director, Level/Combat Designer e QA Engineer.

**Sua tarefa NÃO é refazer o jogo.** Evolua o Coin Commando que existe hoje, com alterações pequenas, verificáveis e reversíveis. A referência é a sensação de um run-and-gun militar 2D clássico (energia, clareza, impacto e ritmo), com identidade própria. Não copie sprites, mapas, personagens, marcas ou outros materiais protegidos de Metal Slug/Contra.

**OBJETIVOS DO V5:** integrar os melhores sprites e ZIPs/RAR locais; aproveitar os sprites novos feitos para o projeto; reformular TODOS os menus e HUD em uma direção visual militar/fliperama coerente; melhorar animação, combate, cenários, veículos, boss e apresentação; preservar os requisitos obrigatórios da atividade de POO.

**Regra-mestra: SOURCE FIRST → ADAPT → CREATE ONLY IF MISSING.** Nunca desenhe visualmente um objeto por primitivas se houver um sprite local apropriado e licenciado que possa ser adaptado. Entretanto, primitivas continuam permitidas quando tecnicamente melhores para hitboxes, efeitos discretos, depuração e indicadores de interface; não sacrifique legibilidade só para usar imagens.

## 0 — CONTEXTO REAL / CAMINHOS

Execute a partir da pasta `ProjetoHermesJogo/Projeto-Moedas/` e descubra o caminho absoluto com `Path.cwd()`. Não assuma sistema operacional ou letras de unidade.

O projeto contém:
- `main.py`, `game.py`, `actors.py`, `campaign.py`, `combat.py`, `level_design.py`, `models.py`;
- `arcade_style.py`, `ui_fx.py`, `weapon_art.py`, `world_fx.py`, `effects.py`, `sound.py`, `polish.py`;
- `assets/` (recursos atuais), `tests/`, `AGENTS.md`, `skills/coin-commando-dev/SKILL.md`;
- `docs/REQUISITOS_OBRIGATORIOS.md`, `docs/ASSET_AUDIT.md`, `docs/MISSING_ASSETS.md`, `docs/ASSET_SOURCES.md`, `docs/asset_gallery.html`, `docs/GAPS_AUDITORIA_INICIAL.md`.

O diretório `_audit_workspace/` JÁ contém material extraído. Não reinicie uma auditoria do zero: atualize e valide a auditoria existente. Os arquivos originais estão na pasta PAI do jogo (`../`), inclusive:
- `AssortedPixelArt.rar`;
- `helicopter.zip`;
- `kenney_crosshair-pack.zip`;
- `kenney_tanksPack.zip`;
- `Pixel Art - City Landscape V2.zip`;
- `pvfx-foundry-thirteen-spritesheets.zip`;
- `Sprites.zip` (Army Soldier, Terrorist Sprites etc.);
- `vacaroxa--generic-run-n-gun-pack--v.1.0.zip`;
- `vista-ten-1.0.0.zip`.

**ASSETS NOVOS, TAMBÉM NA PASTA PAI — prioridade de inspeção e integração:**
- `../commando_unarmed_10f_960x128.png` — candidato a protagonista, folha horizontal de 10 quadros 96×128, sem arma embutida; arma deve ser sobreposta com pivô e mira coerentes;
- `../commando_unarmed_run_10fps.gif` e `../commando_unarmed_preview_2x.png` — referências de prévia, não substitutos do PNG técnico;
- `../combat_drone_8frames_384x128.png` — candidato a drone, 8 quadros, 48×128 SE a grade horizontal for exatamente como descrita pelo nome (confirmar visualmente);
- `../combat_drone_hover_8frames.gif` — referência de prévia;
- `../iron_commander_attack_8f_1152x320.png` — candidato ao boss/ataque, 8 quadros, 144×320 SE a grade horizontal for como descrita pelo nome (confirmar visualmente);
- `../iron_commander_attack_11fps.gif` — referência de prévia.

**Não confunda presença do arquivo com adequação.** Cheque metadados com Pillow, transparência, cortes, ordem, posições, limites e animação. Uma folha chamada “attack” não prova existência de idle, movimento, dano ou morte. Não invente quadros faltantes. Preserve o `assets/player.png` original até comprovar que o novo atende ao contrato da atividade.

## 1 — CONTRATO ESCOLAR: INVIOLÁVEL

Leia `AGENTS.md`, `docs/REQUISITOS_OBRIGATORIOS.md` e os documentos da Parte 1/Parte 2 existentes; confronte com a implementação atual e testes antes de editar. Em especial:
- manter arquitetura multi-telas com `arcade.View` e POO;
- manter `PhysicsEnginePlatformer`, gravidade, plataformas via `Bloco(arcade.Sprite)`/`SpriteList`, `can_jump()`;
- manter spritesheet do jogador com **exatamente 10 quadros de 96×128** e compatibilidade com `arcade.load_spritesheet()`/`get_texture_grid()`;
- manter prioridade salto/queda > idle > caminhada e troca dos quadros de caminhada por `delta_time` aproximadamente a cada 100 ms;
- manter modelo Peewee `Pontuacao`, SQLite, campos e `__str__`; salvamento de nome e consulta Top 10 feita no construtor da TelaRanking, não em `on_draw()`;
- preservar as mecânicas avaliativas das moedas comuns e especiais, inimigo persistente, inimigo perseguidor/teletransportador, telas e controles; implementar lacunas ainda não concluídas sem remover gameplay existente;
- **não resolver sozinho a divergência** entre objetivo da campanha (70% das moedas) e texto inicial da atividade (100%): preserve o comportamento vigente e registre a pendência para decisão humana.

Preserve a campanha existente, armas, loja, ranking, conquistas de gameplay, fases e progressão. Nunca editar/apagar `ranking.db` real nem modificar balanceamento silenciosamente.

## 2 — DESCOBERTA, SELEÇÃO E PROVENIÊNCIA DOS ASSETS

1. Leia e atualize os documentos da auditoria atual. Compare todos os sprites em `assets/` e arte gerada via código com os arquivos de `_audit_workspace` e da pasta pai. Não varra milhares de crosshairs como se fossem candidatos diferentes: agrupe variações por família.
2. Priorize: `Sprites/Army Soldier Sprites` (idle, run, jump, fall, climb, crawl, death); `Sprites/Terrorist Sprites`; `vacaroxa.../Enemies/{ARMob,RPGmob,SniperMob}.png`; `kenney_tanksPack` (barris, caixas, trilhos, tanques, munição); `helicopter/separated_frames`; `pvfx-foundry` (explosion, muzzle flash, smoke, dust, hit, pickup); `AssortedPixelArt/IndustrialRuins_32x32.png`; `Pixel Art - City Landscape V2`; `vista-ten` (camadas sky/far/mid/near); `kenney_crosshair-pack` (apenas as variantes escolhidas).
3. **Cuidado com perspectiva:** um tanque top-down NÃO serve automaticamente para um side-scroller; `TopDownModernExterior_16x16.png` também não. Rejeite assets cuja perspectiva/estética seja incompatível; não force integração por terem sido baixados.
4. Inspecione licenças reais (`License.txt`, `LICENCE.txt`, `LICENSE.txt`, READMEs e proveniência) por pacote. Não presuma CC0 apenas pelo nome. Verifique uso, modificação, atribuição e redistribuição em GitHub público. Para cada arquivo integrado, documente origem, caminho relativo dentro do pacote, autor, URL quando conhecida, licença, hashes, alterações e eventual atribuição. Em dúvida: quarentena, NÃO integrar.
5. Gere/atualize `docs/ASSET_AUDIT.md`, `docs/ASSET_SOURCES.md`, `docs/MISSING_ASSETS.md`, `docs/ASSET_INTEGRATION_PLAN.md` e uma galeria HTML com *antes/depois* (ou caminho para previews), sem assumir que imagens foram visualmente validadas só por dimensões.
6. Trabalhe em staging, por exemplo `assets/_staging_v5/`, antes de promover recursos aprovados para `assets/`. Preserve originais e registre mapeamentos. Não commite `_audit_workspace`, conteúdo integral de packs ou arquivos temporários sem necessidade/licença. Use Pillow para recortes e tratamento com nearest-neighbor; não agrave baixa resolução com upscale que apenas amplia pixels.
7. Faça carregamento eficiente, cache de texturas e atlas quando adequado; não decodifique PNG nem spritesheet dentro de `on_draw()` ou a cada frame.

## 3 — NOVA IDENTIDADE VISUAL (UNIFICAR O JOGO)

Direção: **PIXEL ART 2D LATERAL, ARCADE MILITAR / GUERRA, RUÍNAS, SUJEIRA, FERRUGEM, IMPACTO CINEMATOGRÁFICO**. Evite menus futuristas, neon sci-fi aleatório, ícones infantis ou assets vistos de cima. Preserve proporção, perspectiva lateral, densidade de pixels, iluminação, paleta e contornos coerentes.

### Protagonista
- Compare `commando_unarmed_10f_960x128.png` com `assets/player.png`. Se o novo passar na verificação técnica/visual, integre como candidato prioritário;
- preserve 10 células 96×128: frame 0 idle, frame 1 salto, frames 2–9 caminhada; mantenha `get_texture_grid()` e o funcionamento da máquina de estados;
- faça armas **separadas do corpo**, sobrepostas com pivô de mão, origem do tiro compatível com `GunPose`/muzzle, inversão de direção e recuo. Não permitir arma flutuante, mão deslocada nem tiro saindo do lugar errado;
- para recarga, dano, dash e tiro: procurar quadros específicos nos packs; se não houver, complementar com poses/effects/recoil coerentes; não inventar falsa animação afirmando que existe.

### Drone, helicópteros, veículos e boss
- teste o drone `combat_drone_8frames_384x128.png` para hover/voo e hitbox estável; mantenha granadas e IA atual;
- teste `helicopter/separated_frames` para hélices/voo/queda; use partes quebradas para destruição se condizentes;
- avalie os tanques Kenney como gameplay ou decoração APENAS se houver perspectiva compatível; caso contrário, marque como não utilizáveis e preserve ou procure substitutos;
- `iron_commander_attack_8f_1152x320.png` é **candidato**, não obrigação de substituir boss existente. Teste escala, linha do chão, silhueta e leitura; implemente animação de ataque somente se correta. Preservar telegraph, hitbox e dano. Se faltarem idle/hurt/death/phase-change, registrar lacuna, não fingir que o ataque cobre tudo.

### Objetos e efeitos
- melhore barris explosivos, galões, caixas, covers, minas, laseres, ponte, paredes, terreno, granadas, projéteis, retículos, muzzle flashes, impactos, casings, destroços e fumaça com recursos dos packs;
- moedas continuam moedas funcionais com +1, moeda especial +5 e mesmas regras avaliativas. **Redesenhe representação** para fichas, créditos ou insígnias militares em vez de moeda de Mario. Adicione caixas de munição como pickup separado SOMENTE após preservar coleta, pontuação e economia;
- respeite animações de VFX (frame-rate, alpha, posição, expiração), som sincronizado e otimização. Não criar partículas caras em excesso.

### Cenários
- reconstruir composição artística de Selva, Deserto, Fundição e Neve usando VISTA/cidade/ruínas quando apropriados. Parallax de camadas sky/far/mid/near com velocidades distintas;
- adicionar destroços, vegetação, ruínas antigas, trincheiras, postes partidos, fumaça, viaturas destruídas e helicópteros no horizonte, com densidade sob controle;
- não colocar decoração à frente de hitboxes, tiros, saídas, plataformas ou informações essenciais;
- ambiente deve parecer cenário de guerra/apocalipse, sem simplesmente repetir a mesma imagem de fundo por 4 fases;
- manter FPS consistente em 960×640 e a câmera horizontal estável.

## 4 — REFATORAÇÃO VISUAL DOS MENUS: PRIORIDADE MÁXIMA

Os menus atuais não combinam com o tema. **Reprojetar como uma família visual coerente**, não só trocar cor/fonte. Inspiration: gabinete de fliperama militar com aço gasto, oliva, areia, ferrugem, vermelho de alerta e acentos amarelo-munição, mas sem sci-fi neon.

Abrangência obrigatória: **TelaMenu, TelaInstrucoes, TelaSobre, TelaOpcoes, TelaLoja, TelaPause, TelaRanking, TelaGameOver**, além de overlays, tela de transição, HUD e introdução de boss.

- Criar sistema reutilizável em `ui_fx.py`/módulo novo SE justificar (tokens, estados, botões, fontes, painéis, ícones, animações, layout). Evitar reescrever `game.py` inteiro;
- Menu principal: título Coin Commando, personagem e cenário bélico, fundo com parallax/sutilezas, botões grandes de fácil leitura, selecionado/hover/click com feedback visual e sonoro. Mostrar claramente JOGAR, INSTRUÇÕES, LOJA, OPÇÕES, CRÉDITOS, SAIR, e acesso visível/adequado ao ranking;
- manter navegação por mouse e teclado, foco e atalho funcional; todos os 6 botões dentro de 960×640, sem overlap nem truncamentos;
- Loja: cards legíveis para armas/upgrades, preço, munição, descrição curta, estado comprado/equipado/indisponível, navegação simples, feedback claro, sem alterar lógica econômica;
- HUD: vida, munição, arma, progresso de moedas, créditos, combo, aviso de recarga, boss HP, objetivos. Hierarquia clara e telas livres para enxergar combate;
- Pausa, opções e instruções: contrastes, texto legível, comandos reais atualizados e voltar sem perder estado;
- Ranking: Top 10 consultado uma vez na criação da view; estilo novo sem SQL no render;
- Sobre: avatar mostra **frame individual** do protagonista, nunca a spritesheet completa; verificar interseção exata com textos;
- Game Over: resultados, nome, pontuação, tempo, próxima ação. Preservar gravação Peewee e feedback de vitória/derrota;
- implementar transições discretas (fade, wipe, hit flash), não longas ou repetitivas; respeitar F9/redução de efeitos e legibilidade.

**Critério de aprovação:** testar cada tela em 960×640, capturar screenshots e validar retângulos/botões/textos. Nunca declarar “menu aprovado” só com `py_compile` ou por ter calculado as posições.

## 5 — GAME FEEL, BOSSES E IMERSÃO (ROADMAP, NÃO TUDO NUM ÚNICO LOOP)

Após integração visual e UI estáveis, evoluir em sprints:

1. **Combate:** disparo e recarga com feedback; correção de origem de projéteis, animações de recoil, tiros, danos e morte; VFX sincronizados ao áudio; inimigos com telegraph e dificuldade justa; preservação da mira livre, arsenal e colisões.
2. **Fases:** mais variedade de espaços, coberturas, plataformas e emboscadas; fluxo de dificuldade progressiva; coleta menos trivial sem criar moedas inalcançáveis; validar as mudanças de balanceamento separadamente.
3. **Boss cinematográfico:** corredor de aproximação, arena limpa sem plataformas cobrindo visual ou tiro; câmera enquadra boss inteiro, entrada dramatizada/cutscene curta; ataques em padrões legíveis, múltiplas fases e derrota recompensadora. Não desativar controles por longos períodos e manter acessibilidade de jogo.
4. **Cutscenes curtas:** antes de missão e da arena do boss, com quadros/artes próprias quando houver; sem depender de vídeo externo; opção de pular e retomar corretamente.
5. **Conteúdo futuro:** novas fases depois do boss, veículos especiais e inimigos adicionais SOMENTE depois de preservar o loop atual, os requisitos e testes; documentar antes de expandir a campanha.

## 6 — IMPLEMENTAÇÃO EM SPRINTS CURTAS (ESSENCIAL PARA OPENROUTER FREE)

Trabalhe com orçamento pequeno de ferramentas/modelo. Não execute múltiplos subagentes concorrentes, nem varra 2.000 arquivos repetidamente. Use scripts determinísticos locais para inventário, thumbnails, testes, recortes e hashes. IA faz decisões e código, não operações repetitivas que Python pode fazer de graça.

**Executar SOMENTE a Sprint V5-A nesta sessão, sem se limitar a um relatório textual:**

**Sprint V5-A — baseline + 1 vertical slice funcional**
1. Ler `AGENTS.md`, requisitos e documentos de auditoria existentes; registrar snapshot `git status` e eventuais alterações não commitadas (não sobrescrever trabalho anterior).
2. Validar os 3 PNGs novos (commando, drone, Iron Commander) e o inventário/estado das licenças dos packs; produzir *contact sheet* pequena e compatibilidade por arquivo. Não usar GIF como fonte única quando houver PNG.
3. Selecionar, adaptar e integrar de verdade **um grupo coerente de melhorias**: prioritariamente protagonista sem arma + alinhamento das quatro armas, se aprovado pelos testes visuais; alternativamente, se não couber, barris/coletáveis/VFX como vertical slice. Não misturar mudanças enormes em um único commit.
4. Reprojetar e implementar **TelaMenu** com identidade nova e navegação/posicionamento correto; documentar plano de estilo que permita aplicar às outras telas na Sprint V5-B. Se não houver tempo para concluir protagonista e menu com qualidade, priorizar menu e registrar o resto como pendência.
5. Atualizar os testes de interface/animacão afetados; rodar `python -m py_compile` e `pytest` com o interpretador correto e `python -m pip check`. Se EGL no Windows bloquear testes gráficos, registrar `BLOCKED` (não `PASS`), testar visualmente em modo visível se disponível, e instruir execução em Linux/CI. Não modificar ou apagar `ranking.db`.
6. Capturar screenshots/miniaturas de antes/depois quando possível, revisar tamanho da arma, transparência, clipping, layering, mira e hitbox. Corrigir erros encontrados antes de seguir.
7. Atualizar documentos `docs/ASSET_INTEGRATION_PLAN.md`, `docs/ASSET_SOURCES.md`, `docs/MISSING_ASSETS.md` e criar `docs/V5_CHANGELOG.md` com alterações efetivas e pendências.

**Sprints posteriores (não implementar na mesma sessão):**
- V5-B: Loja, Opções, Sobre, Instruções, Ranking, Pausa, Game Over e HUD;
- V5-C: drones, helicópteros, inimigos, projéteis, explosões e VFX;
- V5-D: parallax, destroços, plataformas, quatro cenários e iluminação;
- V5-E: boss, arena, cutscenes, dificuldade e continuidade de campanha.

Cada sprint deve ficar jogável, incluir testes aplicáveis, trazer screenshots reais quando possíveis e poder ser revertida. Nunca afirmar que integrou algo se só criou checklist ou documentação.

## 7 — RESTRIÇÕES E QA

- **NÃO executar `git push`, remover originals, apagar ranking, modificar API/configuração do Hermes, usar APIs de imagem pagas, instalar licenças comerciais, reescrever tudo de uma vez ou copiar propriedades intelectuais protegidas.**
- Não exigir novo asset de IA se houver pack adequado; se faltar, registrar `docs/MISSING_ASSETS.md` com contrato exato de sprite/frames/estilo, sem iniciar geração paga.
- Usar caminhos relativos e `Path` para evitar quebra entre Windows/Git Bash/WSL. Sanitizar extração dos ZIPs/RAR contra path traversal, duplicações e sobrescritas; não extrair de novo o que já está extraído.
- Cobrir com testes: contrato 960×128 do protagonista, 10 quadros 96×128, ordem das animações, pivôs e muzzle, origem de tiros, hitboxes, botão acessível, bounds, estado de seleção/navegação, ordem dos sprites, carregamento único de texturas, licenças e arquivos ausentes.
- Proteger funcionalidades da Parte 1 e Parte 2, inclusive ranking, ORM e moeda especial. Caso a Sprint 02 de moedas/inimigos ainda não esteja implementada, registrar e não assumir concluída.
- Fazer revisão visual humana de screenshots e ação real; testes unitários aprovados não garantem qualidade visual ou *game feel*.

## 8 — ENTREGA OBRIGATÓRIA

Responda com um relatório objetivo:
- estado inicial do Git e arquivos lidos;
- lista de recursos escolhidos com **ZIP/RAR + caminho interno + licença verificada + arquivo integrado**;
- o que foi EFETIVAMENTE alterado, com paths, classes e alterações;
- screenshots/galeria antes/depois ou motivo concreto da ausência;
- testes `PASS`, `FAIL` e `BLOCKED` separados;
- requisitos preservados e decisões pendentes (70% versus 100%);
- pendências precisas para a próxima sprint;
- como executar/validar em modo visível no Windows;
- pontos sobre os quais precisa de aprovação humana.

**Comece a Sprint V5-A imediatamente. Não finalize apenas com outro inventário. Não afirme conclusão sem código alterado, teste aplicável e validação visual possível.**
