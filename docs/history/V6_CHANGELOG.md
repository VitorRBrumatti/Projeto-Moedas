# Coin Commando V6 — arsenal, sprites animados e Iron Commander

## Alterações efetivas — 10/11/2026
Pedido posterior à V5-B, com autorização explícita para trocar arsenal, ajustar
preços/recompensas, velocidade de projéteis e arena. Worktree já continha as
mudanças anteriores; preservado, sem commit ou push.

### Arsenal e loja
| Arma | Preço | Dano base | Intervalo | Velocidade do tiro | Pente | Movimento |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Glock-18 | inicial | 1 | 0,11 s | 18 | 18 | 1,12× |
| AK47 | 120 | 5 | 0,32 s | 30 | 24 | 0,96× |
| Minigun | 280 | 2 | 0,035 s | 25 | 90 | 0,82× |
Velocidades em unidades do motor por passo fixo. AK tem dispersão 0,065 rad e
recoil forte. Minigun é a mais cara e não aceita upgrade de cadência.
Cada Weapon guarda damage_level/rate_level próprios; trocar arma não transfere
upgrades. Dano até nível3; cadência até2 para Glock/AK. Preços de dano
40/85/130 (Minigun80/170/260); cadência45/100. Compras continuam atômicas.
Arsenal anterior foi substituído a pedido; arquivos antigos preservados.
Badges agora têm painel130×35 e texto pixelado maior; ícones das armas ampliados.
HUD, atalhos1–3, loja, sons, testes e README acompanham o novo arsenal.

### Economia e atividade de POO
Insígnias militares animadas substituem a arte da moeda. Coleta continua +1 comum
ou +5 especial na pontuação; SpriteList, desaparecimento e objetivo preservados.
Créditos: inicial12; coleta1/5; abatecomum2; boss50; transição intermediária25.
Preços de upgrades crescem e não podem ser pagos com a carteira inicial.
A meta vigente de70% permanece. Divergência70%×100% e demais lacunas P1 anteriores
continuam pendentes, sem edição dos requisitos obrigatórios ou ranking.db.
Não é declaração de conformidade integral com todos os pontos da atividade.

### Arte e animação
- Três spritesheets de armas,8 quadros cada, substituem o desenho procedural;
  cano normalizado ao GunPose, mirroring e recoil preservados.
- Insígnia, galão explosivo, mina, emissor laser, granada, espinhos, faca,
  projétil, cápsula, bandeira e ponte: spritesheets próprias,8 quadros cada.
- Bandido mascarado original:8 quadros de corrida e8 de ataque/recarga.
  Guarda/shooter/charger mantêm papéis, patrulha e telegraph; corpo animado real.
- Drone próprio do usuário: grade correta4×2,96×64 por quadro,8 de hover.
  Mantidos perseguição e lançamento de granadas. Helicopter.zip sem licença
  local confirmada não foi promovido; não foi necessário usar arte externa incerta.
- Iron Commander próprio: grade4×2,288×160 na fonte, adaptado240×160.
 8 frames de ataque a11fps; frame0 nas pausas. A fonte NÃO contém walk/hurt/death
  comprovados; deslocamento do boss usa essa silhueta com animação de ataque,
  não se apresenta a folha attack como animação completa de todos os estados.
- Explosão e impactos PVFX CC0 extraídos pelo manifesto; tempo e quadro final
  transparente preservados. Caixa de cobertura Kenney CC0 com arte de sprite.
- Cache central em sprites_v6.py, inclusive espelhados. Preload no construtor da
  janela; sem decodificar imagens ou construir novas texturas a cada draw/tick.
- Terreno/fundos continuam sprites originais. HUD, textos, barras e indicadores
  de segurança continuam UI; retângulos internos de colisão não são arte renderizada.
  Removidos overlays procedurais de equipamentos dos inimigos e acabamentos
  decorativos que estavam substituindo sprites. Clima/CRT são efeitos de tela.

Origens, SHA-256, licenças, tamanho/frames/fps: assets/v6/sources.json e sprites.json.
Quatro atlas de geração preservados como *-source.png, com briefs em
assets/v6/generation-prompts.md. Geração built-in image_gen, sem CLI/API externa.
Recortes/limpeza alpha/escala nearest foram adaptações técnicas, não desenhos
procedurais substituindo as artes. Fontes originais do usuário/packs intactas.

### Menu, áudio e fliperama
Marcha instrumental original de16s sintetizada localmente (metais, caixa e bumbo),
loop apenas na tela inicial; interrompe ao navegar. F8 silencia música/efeitos.
Bomba viaja por0,25s até a opção, seguida da explosão de sprites; ação somente
após1,65s. F9 mantém caminho reduzido de0,25s. Seleção duplicada é bloqueada
pela ação pendente. Scanlines CRT intensificadas, sem impedir F9.
Sons locais novos para Glock/Minigun; script reprodutível tools/generate_v6_audio.py.
Não houve escuta crítica humana; reprodução/lifecycle e PCM foram testados.

### Perigos e boss
- Minas podem ser atingidas por tiros, detonam uma vez e saem das listas;
  colisão varrida impede atravessar uma mina fina em alta velocidade.
- Laser tem base de chão e topo visíveis, sprites animados e feixe conectado;
  janela de aviso/ativação preservada.
- Balas inimigas receberam **+0,45**, aditivo, no módulo da velocidade:
 3,45 + estágio×0,25. Não foi aplicado aumento de45%.
- Arena final ocupa os960px finais, x3040–4000, sem plataformas na frente do boss.
  Física do solo permanece. Na entrada, câmera enquadra a arena inteira e
  o jogador permanece dentro dela; encontro remove patrulhas restantes sem
  recompensa e impede novas emboscadas durante o boss.
- Iron Commander com460HP, deslocamento lateral limitado, telegraph,
  três padrões: rajadas, morteiros e cargas de chão com1,2s de aviso,
  também destrutíveis por tiros. Fase de fúria amplia rajadas e acelera ataques.
  Faixa de introdução colocada no alto para não cobrir o corpo.

## Arquivos de código alterados nesta continuação
campaign.py, game.py, level_design.py, weapon_art.py, sprites_v6.py (novo),
world_fx.py, combat.py, effects.py, polish.py, ui_fx.py, sound.py, arcade_style.py;
README.md; testes de campanha/arsenal/runtime/V4/interface e novo test_v6_rules.py;
tools/generate_v6_audio.py, tools/capture_v6.py; capturador antigo ajustado aos
nomes das armas atuais. Assets novos em assets/v6/, documentos e evidências.
Nenhuma alteração nos modelos Peewee ou enunciados obrigatórios.

## Verificações
- PASS: **79 testes** no contexto gráfico nativo Windows,4 PerformanceWarnings
  existentes de draw_text. Log docs/evidence/v6/native-tests.txt.
- PASS: py_compile dos módulos e ferramentas afetados; pip check; git diff --check.
- PASS: contrato96×128/10quadros do jogador e hash do player original;
  física/can_jump, quatro fases e ranking em banco temporário na suíte.
- PASS: regressões novas para arsenal, upgrades isolados, economia inicial,
  mina atingida uma vez, arena/câmera livre, +0,45 na velocidade,
  bomba com atraso, lifecycle de música, cache espelhado e transparência/frames.
- BLOCKED: pytest padrão headless Windows,3 erros de coleta por EGL ausente;
  log separado headless-tests.txt. CI/Linux com EGL deve executar esse caminho.
- Capturas nativas reais e GIF em docs/evidence/v6/gallery.html. Inspeção visual
  corrigiu alpha residual, tamanho/alinhamento das armas, laser desconectado,
  texto reduzido de upgrade e faixa de intro sobre o boss.
- Capturador prepara carteira999/Minigun e arena para QA; não apresenta esses
  estados como campanha jogada ou créditos legítimos. Não abre o ranking real.

## Execução e limites
Fechar a janela antiga e executar `./.venv/Scripts/python.exe main.py`.
Controles1Glock,2AK,3Minigun; F8som, F9redução de efeitos.
Evidências: `python tools/capture_v6.py`.
Faltam partida humana completa, revisão auditiva e benchmark no hardware de uso.
Balanceamento é implementação real e testada, mas ainda precisa do seu feedback
em campanha; não há promessa de duração/dificuldade medida. Boss ainda não tem
folhas dedicadas de caminhada, dano e morte. Sem commit, push ou publicação.

## Correções posteriores solicitadas pelo usuário
Menu acelerado, projéteis legíveis, novo inimigo armado com estados separados e
ponte reta: V7_CORRECOES.md; capturas em evidence/v7/gallery.html.

## Continuação V8
Cadência invertida, mira estável, fullscreen, arte militar e limpeza autorizada
do ranking com backup:V8_CORRECOES.md; galeria evidence/v8/gallery.html.
