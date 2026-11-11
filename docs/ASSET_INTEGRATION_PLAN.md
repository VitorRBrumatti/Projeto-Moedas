# Sprint V5-A — integração e direção para V5-B

## Escopo executado em 10/11/2026
1. Baseline preservado: patch/status em `docs/evidence/v5-a/` (game.py e teste já modificados).
2. Inspeção Pillow e visual dos três PNGs, contact sheet e hashes.
3. Protagonista personalizado integrado; colisão original, estados e cadência preservados.
4. TelaMenu substituída por composição militar com personagem real, fundo de ruínas,
   botões em painel, seleção, atalhos e ranking clicável.
5. Testes nativos Windows, captura OpenGL e documentação; headless EGL separado.

## Escolhas e alternativas
Adotada integração do commando com preservação de colisão, em vez de trocar todo o
sistema de atores ou usar soldados sem licença confirmada. Menu reaproveita lettering,
ScreenMotion, áudio e fundo existentes. Sem novas dependências de runtime.
O usuário pediu execução imediata da sprint; nenhuma expansão de campanha foi feita.

## Contrato do protagonista
Fonte própria: `../commando_unarmed_10f_960x128.png`. Autoria e autorização de uso,
modificação e redistribuição pública confirmadas pelo usuário em 10/11/2026.
Staging `assets/_staging_v5/commando.png`; runtime `assets/v5/commando.png`.
Translação +6 px em Y (Pillow, sem interpolação); nenhum pixel opaco excede a folha.
10 células de 96×128, idle 0, salto 1, caminhada 2–9. Frames carregados uma vez via
load_spritesheet/get_texture_grid e cache. `assets/player.png` intacto é também a
fonte do polígono de colisão anterior; arte nova não redefine a física.
As poses não incluem recarga/dano/morte dedicados: efeitos atuais continuam responsáveis.

## Armas
GunPose é a fonte compartilhada para mãos, arma, cano e recuo. Âncora lateral
espelhada +9 px, altura +3 px, mira usa essa mesma origem. Correção de 1 px no centro
horizontal da textura para coincidir com a geometria do muzzle. Escala de apresentação
isolada usada no menu (3x), sem alterar alcance, cadência, dano ou economia.
Limite: mãos sobrepostas acompanham a arma, mas o corpo não tem rig de braços de mira;
poses extremas e todos os quadros em movimento ainda merecem revisão humana em jogo.

## Direção V5-B (não implementada)
Paleta MILITARY em arcade_style.py: aço/oliva, areia, amarelo-munição, ferrugem.
Aplicar aos painéis das outras Views sem reescrever game.py. Hierarquia título,
conteúdo, ação e retorno; foco visível, mouse e teclado, redução de efeitos F9.
- Loja: cards com preço, estado e comparação, sem mudar transações.
- Opções/Instruções: comandos reais, contraste e retorno preservado.
- Sobre: avatar individual do novo protagonista, sem folha completa.
- Ranking: Top 10 no construtor; nunca consultar durante draw.
- Pausa/Game Over: preservar instância, input de nome e salvamento.
- HUD/overlays: reorganizar sem encobrir combate; capturar cada tela em 960×640.

## Decisões pendentes
70% versus 100% das moedas e outras divergências P1 permanecem em
GAPS_AUDITORIA_INICIAL.md. Nenhum requisito foi editado; nenhuma conformidade integral
com P1 é declarada. Drone/boss, cenários e conteúdo são V5-C/D/E, não V5-B.

## Reparo de compatibilidade obrigatório
TelaSobre estava sem on_draw antes da sprint; desenho de autoria/avatar restaurado
com teste de regressão demonstrado. Sem antecipar seu redesign V5-B.

## Execução posterior autorizada — menus/HUD V5-B
Pedido do usuário após V5-A: unificar menus/HUD com tela inicial e usar sprites dos packs.
Implementado conforme V5B_CHANGELOG.md; galeria evidence/v5-b/gallery.html.
Integração de inimigos, boss e cenários não foi antecipada.

## V6 — ampliação autorizada pelo usuário
Arsenal/economia, geração de sprites, minas atingíveis e boss/arena foram solicitados
explicitamente depois de V5-B. Implementação e limites em V6_CHANGELOG.md.
