# V8 — cadência, mira, fullscreen e legibilidade — 11/11/2026

## Implementado
- Inversão dos intervalos pedidos:AK47 0,32→0,11s; Glock0,11→0,32s.
  Velocidade dos projéteis continua AK30/Glock18; o problema era a cadência.
  Minigun continua mais rápida0,035s. Testes de perfis atualizados ao novo pedido.
- Recuo físico zerado e dispersão retirada; o sprite ainda tem animação de disparo.
  Mira não soma tremor da câmera. Pivô perto do corpo agora depende do alvo,
  não do ângulo anterior, eliminando alternância esquerda/direita.
  Tremor desativado durante a arena para não deslocar a referência de mira.
- F11 em todas as telas, inclusive entrada de nome, e botão em Opções.
  Render em960×640 lógico com escala proporcional e faixas laterais quando preciso.
  Mouse é convertido no limite da janela para coordenadas lógicas antes de mirar
  ou clicar. Troca deliberada de modo limpa input sem provocar pausa por foco;
  perda de foco normal continua pausando. Sem alterar física ou layouts de colisão.
- Plataformas/solo/parede com sprites novos de concreto e aço militar.
  Caixas de cobertura de madeira substituídas por caixa militar de aço animada.
  A versão anterior já usava PNG Kenney, mas sua aparência não atendia ao pedido.
- Insígnia com contorno escuro e claro e face estável para contrastar em cenários
  claros/escuros e continuar visível quando o quadro giratório fica de lado.
  Collider original da insígnia foi mantido por textura separada de inicialização;
  +1/+5, créditos, meta e economia de coleta não foram modificados.

## Banco real — operação autorizada explicitamente pelo usuário
O pedido atual para limpar o DB prevalece sobre a restrição padrão de não tocá-lo.
Antes da limpeza:integrity_check=ok e3 registros em pontuacao. Não foi encontrada
corrupção estrutural; não foi afirmado que havia corrupção do arquivo.
Backup consistente via SQLite backup API em:
`.local-backups/ranking-before-reset-20261111T030819Z.sqlite3`.
Integridade do backup verificada antes do DELETE transacional; tabela pontuacao
ficou vazia. Esquema/modelos mantidos. Diretório de backup adicionado ao .gitignore.
Não foram expostos nomes ou pontuações. Testes ORM continuam com banco temporário.

## Arquivos
campaign.py; game.py (mira, Bloco, input/tela cheia/opções); combat.py (caixa);
assets/v6/sprites.json (mapeamento para novos arquivos); assets/v8/ (fontes e derivados);
.gitignore; README; testes afetados; tools/capture_v8.py e esta documentação.
Sprite SpriteList, PhysicsEnginePlatformer, can_jump, Views, contrato96×128/10frames,
Peewee e ranking Top10 no construtor continuam preservados. Meta70% não alterada.

## Verificação
- PASS:85 testes completos no contexto nativo Windows,4 avisos draw_text.
- PASS:py_compile, pip check e git diff --check.
- PASS:captura real em tela cheia1920×1080, viewport1620×1080 com laterais150px,
  conversão do centro para(480,320), ida/volta de fullscreen sem pausa involuntária.
- PASS:teste de clique no menu escalado1280×800 e viewport da tela seguinte.
- PASS:regressão de mira estável na arena, sem recuo após fire.
- BLOCKED:pytest headless por EGL ausente,3 erros de coleta em log separado.
- Capturas revisadas em evidence/v8/gallery.html; capturador não abre o banco real.
  Carteira999/Minigun, arena e projéteis de contraste são estados preparados para QA.

## Executar
Fechar a janela antiga e rodar `./.venv/Scripts/python.exe main.py`.
F11 alterna tela cheia; Opções também oferece o botão. F8som/F9efeitos preservados.

## Mobile
Pedido de port fica para a próxima etapa, conforme “depois” no pedido do usuário.
Esta entrega continua desktop: não há APK nem alegação de suporte Android/iOS.
A separação entre coordenadas lógicas e janela ajuda uma UI futura, mas não prova
compatibilidade mobile. Antes do port:confirmar plataforma alvo, controles touch,
renderizador/empacotamento e testar num dispositivo físico. Nenhuma dependência
mobile foi adicionada ou migração de framework foi feita nesta correção.

Limites:sem partida humana completa, escuta crítica ou teste em celular. Fontes
originais e versões anteriores preservadas. Sem commit, push ou publicação.
