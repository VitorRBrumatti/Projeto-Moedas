# Coin Commando — instruções obrigatórias para agentes de código

## Escopo
Projeto existente de jogo 2D arcade/plataforma com Python Arcade 3.3.3, Peewee/SQLite, sprites e testes automatizados. A inspiração estética é Metal Slug, sem cópia de sprites, sons, mapas, logotipos ou personagens protegidos. A missão é EVOLUIR O QUE JÁ EXISTE, não substituir o jogo.

## Hierarquia de requisitos
1. `docs/REQUISITOS_OBRIGATORIOS.md` resume dois enunciados oficiais da atividade de POO (Parte 1 e Parte 2). Se os PDFs/DOCX originais estiverem disponíveis, eles têm precedência em caso de discrepância com o resumo.
2. Requisitos da atividade e da defesa individual têm prioridade sobre preferências visuais.
3. Melhorias de jogabilidade, UI, dificuldade, bosses, cutscenes e novas fases são aditivas, desde que não violem itens obrigatórios.
4. Regras contraditórias entre a campanha atual e a atividade não devem ser 'resolvidas' silenciosamente. Reporte o conflito, proponha adaptação mínima/compatibilidade e peça aprovação humana antes de mudar o comportamento.

## Restrições inegociáveis
- Preservar arquitetura com múltiplas classes `arcade.View`.
- Preservar herança de `arcade.Sprite`, uso de `arcade.SpriteList`, POO e separação de responsabilidades.
- Preservar `arcade.PhysicsEnginePlatformer`, gravidade, plataformas `Bloco` e bloqueio de pulo duplo com `can_jump()`.
- Preservar `arcade.load_spritesheet()` e `get_texture_grid()` em quadros 96x128. Idle, salto/queda e caminhada com prioridade adequada; avanço a cada 0,1 s via `delta_time`.
- Preservar modelo Peewee `Pontuacao`: `nome_jogador`, `pontos`, `tempo_partida`, `data_hora`, com `__str__`, `Pontuacao.create()` e ranking Top 10 consultado no `__init__` de `TelaRanking` (nunca em `on_draw`).
- Não eliminar menu, instruções, sobre/autores, gameplay, Game Over, ranking e navegação por teclado.
- Não apagar funcionalidades existentes: quatro fases, armas, loja, progressão, moeda especial, chefão, HUD e efeitos, salvo autorização explícita após análise de impacto.
- Não editar `ranking.db` real; executar testes de persistência com banco temporário.
- Não mudar sistemas de física, colisão, input, economia ou câmera quando a tarefa for apenas UI/arte.
- Não substituir sprites por formas geométricas genéricas para 'simplificar' a arte sem justificar uma exceção técnica.
- Nunca publicar chaves, credenciais, arquivos `.env`, bancos reais, nem introduzir assets com licença incompatível.

## Procedimento por alteração
1. Ler `README.md`, os arquivos relevantes em `docs/`, a implementação existente e os testes pertinentes.
2. Descrever objetivo, impacto em requisitos e arquivos a mudar. Uma melhoria por branch/tarefa sempre que possível.
3. Antes de escrever, identificar comportamento anterior e adicionar/ajustar testes de regressão.
4. Fazer a menor modificação coerente possível, preservando responsabilidades dos módulos.
5. Rodar `python -m pytest -q`; quando apropriado, também executar o jogo e observar o resultado visual/áudio. Não afirmar teste visual se não foi executado.
6. Mostrar arquivos alterados, testes rodados (com resultados reais), efeitos colaterais, critérios de aceitação e itens ainda pendentes.
7. Se algum requisito obrigatório for violado, NÃO declarar a tarefa concluída.

## Cuidados com modelos gratuitos
- Planejar e implementar tarefas pequenas para economizar solicitações ao OpenRouter.
- Não alternar automaticamente para modelos pagos; se a cota gratuita acabar, parar e informar.
- Preferir ferramentas locais (pytest, leitura, grep, git diff) para tarefas determinísticas sem chamar outros agentes.
- Delegação paralela ou geração de imagem só mediante autorização específica. OpenRouter texto gratuito não significa imagens gratuitas.

## Organização real do repositório
- `main.py` entrada; `game.py` Views, física e integração (arquivo grande, não refatorar tudo de uma vez).
- `actors.py` sprite do jogador/estados; `campaign.py` armas e fases; `level_design.py` layout.
- `combat.py` projéteis/coberturas; `models.py` banco/ranking; `arcade_style.py`, `ui_fx.py`, `sound.py`, `world_fx.py` apresentação.
- `assets/` imagens e sons; `tests/` testes; `.github/workflows/tests.yml` CI.

## Modelo de entrega
Resumo objetivo / Requisitos preservados / Arquivos alterados / Testes executados e resultado / Riscos e pendências / Próxima melhoria pequena sugerida.
