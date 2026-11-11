# Briefs de geração — built-in image_gen

Fighter: adversário irregular fictício, rosto visível, boné oliva, colete e calça
cinza-azulada; sem capuz/balaclava/cachecol, sem marcas reais. Rifle grande nas duas
mãos, coronha no ombro. Estados idle, walk, aim e fire em linhas separadas.
A geração solicitava oito colunas, mas a inspeção confirmou **sete** por linha;
a adaptação usa os sete frames reais, sem inventar um oitavo.

Bridge: passarela lateral comprida, deck horizontal reto e cordas baixas,
quadros de vento discreto. Oito colunas reais; somente a primeira linha de spans
foi integrada. Bases extras da segunda linha preservadas na fonte, sem integração.

Destinos ativos e fps em assets/v6/sprites.json, com file apontando assets/v7/.
Fontes PNG preservadas em assets/v7/, geração via ferramenta embutida, sem CLI externa.
