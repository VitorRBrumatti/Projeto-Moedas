# Coin Commando — assets que realmente faltam

Esta lista contém somente arte que não tem substituto adequado nos pacotes
locais. Itens com candidato utilizável, mesmo exigindo recorte ou adaptação,
ficaram fora e estão em [ASSET_AUDIT.md](./ASSET_AUDIT.md).

| Nome do sprite | Função no jogo | Dimensões recomendadas | Quadros necessários | Animações necessárias | Prioridade | Adaptar existente? |
| --- | --- | --- | --- | --- | --- | --- |
| Drone militar voador | Inimigo aéreo que persegue e lança granadas | corpo visível de `78x66` ou `96x64`, transparente | 4–8 | voo/hover, dano, destruição | Alta | **Não**. O helicóptero `768x32` é veículo horizontal e não possui silhueta/ângulo adequados. |
| Guardião/boss humanoide | Chefe final da quarta fase, com barra de vida e ataques | `240x144` ou `288x160`, transparente | 4–8 por estado | idle, ataque, dano, morte, fase enfurecida | Alta | **Não**. Tanques Kenney são top-down e não preservam a leitura do boss atual. |
| Protagonista compatível com a atividade | Jogador e avatar de autoria, se a silhueta atual for substituída | folha `960x128`, células `96x128` | 10 | idle, salto/queda, caminhada de 8 quadros | Baixa / condicional | **Não diretamente**. Os soldados têm dimensões e proporções incompatíveis; o atual já atende ao requisito e deve ser mantido. |

## Não faltam

- Soldados comuns, shooter e charger: há material em `Sprites` e
  `vacaroxa`, classificado como **ADAPTAR**.
- Explosões e impactos: PVFX Foundry cobre as famílias necessárias, mas
  requer integração de spritesheet/manifesto.
- Mira: o pacote Kenney Crosshair pode substituir a mira procedural.
- Minas, barris, caixas e veículos decorativos: Kenney Tanks e o pacote de
  helicóptero têm candidatos, porém com ajuste de escala e perspectiva.
- Fundos e tiles: há várias opções, mas nenhuma é substituição direta para os
  quatro cenários sem composição e compatibilização de escala.

## Regra de produção

Criar somente os três itens da tabela, nesta ordem: drone, boss e, se
necessário após o protótipo de soldados, uma nova folha de protagonista
`960x128`. Não criar moedas, armas, crosshair, explosões ou fundos antes de
testar os candidatos existentes.

## Atualização V5-A — prioridades substituídas

Protagonista 960×128 deixou de faltar: personalizado integrado em `assets/v5/commando.png`.
Drone e boss agora têm fontes próprias, mas exigem adaptação de grade 2D e confirmação
visual da ordem dos frames; não gerar arte nova antes desse teste. A auditoria anterior
que dizia CRIAR não deve mais ser usada como autorização de geração.
Continuam ausentes animações dedicadas de recarga/dano/morte do protagonista e
idle/hurt/death/phase-change comprovados do boss. Preservar efeitos atuais até haver
folhas compatíveis e validadas. Não inferir essas animações de uma folha attack.

## V6 — lacunas atualizadas
Resolvidos: arte de drone, boss ataque, bandido, armas, galão, mina, emissorlaser,
insígnia, granada, projéteis e props. Boss ainda não tem walk/hurt/death dedicados;
a folha attack não comprova esses estados. Nenhuma geração adicional é exigida
para rodar a V6; revisão humana de áudio/balanceamento continua necessária.
