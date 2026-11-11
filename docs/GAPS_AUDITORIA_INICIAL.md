# Auditoria inicial — diferenças observadas em 10/11/2026

Com base na `main` pública do repositório. Não substitui execução manual nem uma auditoria de ponta a ponta. **Estado:** pontos para confirmação, não autoriza mudanças automáticas.

| Ponto | Observação no código | Próxima verificação |
| --- | --- | --- |
| Meta das moedas | `game.py` define `coin_goal = ceil(total_coins * 0.7)`; Parte 1 pede TODAS as moedas | Propor modo compatível com atividade ou validar mudança com professor. Não retirar campanha sem autorização. |
| Sobre/autoria | `TelaSobre.on_draw()` desenha textos; Parte 1 pede avatares/fotos com sprites | Adicionar sprite(s) originais, mantendo créditos. |
| Menu | Atalho `[I]` existe, mas as opções visíveis são Jogar/Loja/Opções/Créditos/Sair; Parte 1 pede opção visível Instruções | Avaliar layout e exibição explícita sem eliminar Loja/Opções. |
| Moeda especial | `game.py` usa oscilação senoidal vertical; Parte 1 pede movimento vetorial e rebote nas bordas | Inspecionar requisitos de colisão no modo plataforma; criar comportamento testável compatível. |
| Inimigo especial | Código contém 'charger' que persegue em intervalo, mas não foi identificado teletransporte em colisão | Verificar implementação/necessidade de nova classe ou modo alternativo, com teste próprio. |
| Tela final | `TelaGameOver` diferencia vitória e derrota; Parte 1 pede mensagem própria para pontuação máxima sem danos vs pontuação parcial | Criar teste de variações da mensagem de resultado. |
| Área de jogo | Testes de render usam 960x640, e a campanha rola por extensão maior; Parte 1 descreve tela 800x600 e bordas internas | Confirmar se dimensões eram exemplificativas e como adaptar a regra no modo campanha. |
| Testes | Há múltiplos testes pytest e workflow CI; o commit mais recente anuncia 59 verificações | Rodar suíte localmente e comparar com o GitHub Actions; nenhuma aprovação foi simulada aqui. |
| P2 física/ORM | Há `PhysicsEnginePlatformer`, `can_jump()`, `Bloco`, spritesheet 96x128, Peewee e Top 10 carregado em `__init__` | Preservar e testar; isto é análise estática, não certificação de conformidade integral. |

## Decisão obrigatória antes de refatorar P1
Registrar uma entre: (A) manter todas as exigências originais e acrescentar modo compatível; (B) obter autorização do professor para uma equivalência funcional; (C) adiar mudanças conflitantes. Na ausência de decisão, corrigir apenas problemas que não afetem a regra do jogo.
