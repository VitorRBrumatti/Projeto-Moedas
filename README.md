# Coin Commando

Jogo 2D de ação e plataforma em Python Arcade, desenvolvido para a atividade de
Programação Orientada a Objetos do IFPR — Campus Paranavaí.

Quatro setores, mira livre, arsenal com upgrades por arma, drones, perigos,
Iron Commander e ranking local. Arte militar com sprites animados e efeitos de fliperama.

## Rodar

Requisitos: Python 3.10+, OpenGL 3.3+ e as dependências de `requirements.txt`.
No Windows, o ambiente validado usa Python 3.13.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Git Bash, depois de instalar:

```bash
source .venv/Scripts/activate
python main.py
```

Linux/macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Mantenha `assets/` junto aos módulos Python. `ranking.db` é criado na primeira
execução e fica fora do Git, assim como `.venv/` e backups locais.

## Controles

| Comando | Ação |
| --- | --- |
| A/D ou setas | Andar |
| Espaço/W/seta para cima | Pular |
| Mouse | Mirar |
| Clique esquerdo/J/X | Disparar |
| R | Recarregar |
| 1/2/3 | Glock-18 / AK47 / Minigun |
| T | Lançar faca comprada |
| Shift | Dash |
| B | Loja no início ou perto da saída |
| P/Esc | Pausar/retomar |
| M na pausa | Voltar ao menu |
| F11 | Tela cheia |
| F8 | Som |
| F9 | Reduzir efeitos |
| R no menu ou resultado | Ranking |

Colete pelo menos **70% das insígnias** e alcance a saída. Na última fase,
derrote também o Iron Commander. Insígnias comuns somam +1 ponto; especiais, +5.
Créditos e pontuação são separados. Ao terminar, informe seu nome para salvar o resultado.

| Arma | Preço | Intervalo base | Característica |
| --- | ---: | ---: | --- |
| Glock-18 | Inicial | 0,32 s | Leve, mobilidade maior |
| AK47 | 120 créditos | 0,11 s | Dano alto |
| Minigun | 280 créditos | 0,035 s | Pesada, cadência fixa |

Upgrades pertencem à arma equipada. Minigun não recebe upgrade de cadência.
Plataformas sustentam personagens e granadas; chão e coberturas bloqueiam tiros.
Minas podem ser detonadas por disparos. O menu usa uma explosão curta antes de confirmar.

## Estrutura

```text
main.py                 Entrada do jogo
*.py                    Views, atores, campanha, combate, áudio e apresentação
assets/sprites/         Spritesheets ativos e registro de animação
assets/ui/              Ícones da interface
assets/audio/           Efeitos e música
assets/licenses/        Licenças de terceiros
assets/archive/         Fontes/versões locais ignoradas pelo Git; não carregadas pelo jogo
assets/sources.json     Proveniência e hashes dos assets ativos
assets/*.png            Bases originais e texturas de compatibilidade/colisão
tests/                 Testes de regras, persistência, física e renderização
tools/                 Capturador atual e gerador de áudio
docs/                  Requisitos, auditorias, índice e histórico
.github/workflows/     Testes no CI
```

## Verificar

```bash
python -m pip install pytest
python -m pytest -q
```

Os testes gráficos headless precisam de EGL/OpenGL, disponível no workflow Linux.
No Windows sem EGL, use o contexto nativo:

```bash
python -c "import arcade,pytest; raise SystemExit(pytest.main(['-q']))"
```

Os testes de persistência usam banco temporário. Para gerar capturas nativas:

```bash
python tools/capture.py
```

O capturador abre janelas, testa tela cheia e salva em `docs/evidence/current/`.
Não abre o ranking real. Estados de loja/arena são preparados para QA.

## Documentação

- [Índice dos documentos](docs/README.md)
- [Requisitos obrigatórios de POO](docs/REQUISITOS_OBRIGATORIOS.md)
- [Conflitos acadêmicos ainda pendentes](docs/GAPS_AUDITORIA_INICIAL.md)
- [Assets e licenças](assets/README.md)
- [Galeria](docs/asset_gallery.html)
- [Organização e validação da limpeza](docs/ORGANIZACAO.md)

A campanha mantém a meta de 70%; a divergência com o enunciado de 100% continua
registrada para decisão humana. Física, Views, SpriteList, spritesheet 96×128,
`can_jump()` e ranking Peewee foram preservados. Port mobile ainda não iniciado.

Desenvolvido por **Vitor Rufino Brumatti — 3º Info / IFPR**.
