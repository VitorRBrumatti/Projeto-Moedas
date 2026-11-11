---
name: coin-commando-dev
description: Evoluir gradualmente o jogo Coin Commando em Python Arcade preservando os requisitos de POO e evitando regressões.
---

# Coin Commando Dev

Use esta skill quando a tarefa for auditar, planejar, corrigir, polir ou adicionar uma pequena funcionalidade ao repositório Coin Commando.

1. Localize a raiz do repositório. Leia `AGENTS.md`, `README.md`, `docs/REQUISITOS_OBRIGATORIOS.md` e `docs/GAPS_AUDITORIA_INICIAL.md`.
2. Leia apenas os módulos relevantes. Cite o comportamento atual com arquivo/funcionalidade; não presuma que o jogo está vazio.
3. Classifique o pedido em POO obrigatória, correção, polimento visual, balanceamento, fase, boss ou cutscene.
4. Faça análise de impacto sobre P1/P2; conflitos devem ser sinalizados antes da alteração.
5. Apresente um mini-plano em até 5 passos e critérios objetivos. Para tarefas grandes, use `/plan` e espere decisão do usuário antes de codificar.
6. Trabalhe em mudanças pequenas; testes antes/depois; mantenha assets licenciados e desempenho.
7. Execute `python -m pytest -q` quando o ambiente permitir. Não confunda teste de lógica com avaliação estética de vídeo ou imagem.
8. Em cada entrega, registre arquivos mudados, resultado real dos testes, requisito correspondente e risco residual.
9. Não faça push/merge em `main` nem remova assets/funcionalidades sem aprovação humana.
10. Nunca acione endpoints pagos como fallback. Se o modelo gratuito retornar 429/402, explique e pause as chamadas ao modelo.

## Foco de qualidade
- Combate: telegraph de inimigos, feedback de tiros/dano, hurtboxes honestas, recarga, câmera e recoil.
- Boss: chegada cinematográfica, arena limpa, fases de ataque, dificuldade justa e checkpoints.
- Arte: sprites pixel art consistentes, silhueta e escala coerentes, UI temática militar/arcade, sem estética futurista involuntária.
- Performance: sprite lists, estabilidade 60 FPS no hardware-alvo, renderização sem consultas SQLite em loop.
- Regras: moedas, pontuação, tempo, ranking, estados de animação e views devem permanecer auditáveis para a atividade.
