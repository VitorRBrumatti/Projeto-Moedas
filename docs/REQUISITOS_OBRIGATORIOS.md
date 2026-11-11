# Matriz de requisitos obrigatórios — atividade de POO

**Fontes:** documentos fornecidos anteriormente pelo usuário, intitulados "Atividade Prática - Jogo Multi-Telas com Python Arcade e POO" (Parte 1) e "Atividade Prática - Jogo Multi-Telas com Python Arcade e POO - Parte 2". Este arquivo é um resumo operacional para agentes; confira os originais quando disponíveis. **NÃO descaracterize** uma exigência para acomodar o redesign Metal Slug.

## P1 — Atividade inicial (múltiplas telas, POO e moedas)
- [ ] `arcade.Window` como janela; telas separadas por subclasses de `arcade.View`: menu, instruções, sobre, jogabilidade e Game Over.
- [ ] Menu exibe título e opções visíveis `[J]` Jogar, `[I]` Instruções, `[S]` Sobre e `[ESC]` Sair.
- [ ] Instruções explicam objetivo, inimigos e comandos de teclado. `[ESC]` ou `[M]` retornam ao menu.
- [ ] Sobre apresenta nomes dos desenvolvedores e **fotos ou avatares usando sprites**. `[ESC]` ou `[M]` retornam ao menu.
- [ ] Gameplay com interrupção via `[ESC]` para retorno à tela inicial (comparar com pausa atual e resolver conflito explicitamente).
- [ ] Game Over após coletar **todas** as moedas da lista, com pontuação, tempo e distinção entre pontuação máxima sem dano e pontuação parcial; `[M]` Menu ou `[ESC]` sair.
- [ ] Personagem herda `arcade.Sprite`, reage a setas/WASD, respeita limites internos, troca textura conforme direção.
- [ ] Moeda comum estática soma +1, desaparece ao colidir; pelo menos 25 moedas semeadas via `random` e laço.
- [ ] MoedaEspecial móvel soma +5 e rebate nas bordas invertendo vetor de velocidade; desaparece ao coletar.
- [ ] Inimigo comum persiste após colisão, move-se autonomamente, desconta 1 ponto e mostra alerta visual; efeito de rebote previsto no critério avaliativo.
- [ ] InimigoEspecial persegue o jogador mais lentamente, desconta 1 ponto e **teletransporta** após a colisão, continuando a perseguir.
- [ ] Entidades em `arcade.SpriteList`; colisões e tempo de jogo atualizados no ciclo de gameplay; HUD mostra pontos, tempo e alerta de dano.
- [ ] POO: herança, sobrescrita, encapsulamento e polimorfismo explicáveis na arguição TESTAI.

## P2 — Complemento posterior (física, animação e persistência)
- [ ] `arcade.PhysicsEnginePlatformer`, gravidade e proibição de pulo duplo via `can_jump()`.
- [ ] Classe `Bloco(arcade.Sprite)`; chão e plataformas suspensas em `arcade.SpriteList`.
- [ ] Spritesheet carregada com `arcade.load_spritesheet()` e `get_texture_grid()`; quadros de 96x128: idle (0), salto (1), caminhada (2 a 9).
- [ ] `Jogador.update(delta_time)` prioriza salto/queda, depois idle, depois caminhada com troca a cada 100 ms e orientação esquerda/direita.
- [ ] SQLite `ranking.db`, Peewee `SqliteDatabase`, `BaseModel(Model)` e `Pontuacao(BaseModel)`.
- [ ] Campos: `nome_jogador = CharField()`, `pontos = IntegerField()`, `tempo_partida = FloatField()`, `data_hora = DateTimeField(default=datetime.datetime.now)`, além de `__str__` legível.
- [ ] Ao finalizar, coletar nome via eventos `on_text/on_key_press` e inserir pontuação com `Pontuacao.create()`.
- [ ] `TelaRanking(arcade.View)` consulta `Pontuacao.select().order_by(Pontuacao.pontos.desc()).limit(10)` uma vez em `__init__` (empates adicionais permitidos sem alterar ordenação principal). Nunca consultar no `on_draw`.
- [ ] Renderizar Top 10 com `enumerate()` e `arcade.draw_text()`, com estado vazio e opção `[R]` no menu ou Game Over.
- [ ] Interface separada da lógica de banco e efeitos sem perda de desempenho.

## Compatibilidade com a campanha atual
O jogo atual possui quatro fases, scroll, AK-47, outras armas, loja, boss e saída com 70% de moedas. **Esses recursos são melhorias do projeto**, mas algumas regras da Parte 1 não batem literalmente. Não assumir que a Parte 2 revogou a Parte 1: ela se apresenta como integração adicional. Qualquer desvio requer decisão explícita do usuário e, idealmente, validação com o professor.

## Aceite por mudança
Uma melhoria somente está concluída quando: (a) não remove requisitos, (b) passa testes relevantes, (c) cumpre os critérios objetivos da tarefa, (d) não inventa que houve teste visual e (e) lista conflitos ainda abertos.
