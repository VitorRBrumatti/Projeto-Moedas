# Correções após feedback da V6 — 11/11/2026

- Seleção de menu:1,65→0,85s, viagem da granada0,12s e explosão acelerada1,9×.
  F9 continua com0,25s. Som sincronizado à chegada, ação depois do efeito.
- Balas inimigas: sprite32×12 em vez20×7, contorno escuro e núcleo claro opaco,
  recortado do raster original; velocidades e colisão permanecem iguais.
- Aparência do inimigo trocada por combatente irregular fictício com boné,
  rosto visível e rifle de duas mãos. Não utiliza capuz/balaclava/cachecol.
- Quatro estados separados: espera armada, caminhada, mira e disparo.
  Guarda/shooter param ao mirar/disparar, em vez de continuar correndo.
  Charger preserva sua função de investida. Rifle visível nas quatro folhas.
  Sete frames reais por estado, validados; não foram presumidos oito pelo prompt.
- Origem do tiro inimigo ajustada ao rifle:offset32/14 no combatente,98/10 no boss,
  com direção espelhada e vetor de mira calculado a partir dessa origem.
- Ponte: nova folha reta, oito frames; ocupa toda a largura da plataforma,
  sem a antiga curva e suportes grandes. Plataformas, colisão e saltos preservados;
  a nova arte não promete extensão caminhável além da superfície física.
- Originais V6 preservados; folhas novas em assets/v7. Loader aceita file do
  registro, mantém preload/cache/espelhamento. Fontes/hashes/briefs na pasta nova.

Código: game.py, combat.py, ui_fx.py, sprites_v6.py; registro assets/v6/sprites.json;
testes pertinentes e tools/capture_v7.py. Arte e documentos novos em assets/v7/docs.
Modelos, ranking.db, moedas+1/+5 e requisitos obrigatórios não alterados.

## Verificação
- PASS:82 testes completos no contexto nativo Windows,4 avisos draw_text;
  log evidence/v7/native-tests.txt. Regressões de mira parada e atraso falharam
  antes da correção; agora passam. Também testados estados7frames, contorno opaco,
  tamanho do traçante e origem do rifle.
- PASS:teste de projétil repetido após refinar o raster; compilação, pip check e
  git diff --check sem erros.
- BLOCKED:pytest headless por EGL ausente,3 erros de coleta em log separado.
- Capturas reais e GIF do menu:evidence/v7/gallery.html. As três balas da captura
  hostile-visibility foram posicionadas para QA de contraste, não são uma gravação
  de combate. Carteira/Minigun e arena também são estados preparados pelo capturador.
- Sem partida humana completa, escuta crítica ou benchmark de FPS. Sem commit/push.

Fechar a janela antiga e rodar `./.venv/Scripts/python.exe main.py`.
