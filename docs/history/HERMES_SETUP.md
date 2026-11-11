# Instalação do kit Hermes — Coin Commando

**Não apliquei alterações ao GitHub, à sua máquina ou ao seu Hermes.** O kit contém arquivos prontos para COPIAR após revisão. Não é uma instalação remota.

## 1. Projeto

Na raiz local do repositório `Projeto-Moedas`, copie:
- `AGENTS.md` para a raiz.
- os arquivos da pasta `docs/` para `<repositorio>/docs/`.

A skill pode ser instalada em `~/.hermes/skills/coin-commando-dev/SKILL.md` (dentro do Linux/WSL se Hermes foi instalado lá). O mesmo arquivo está na pasta `skills/coin-commando-dev/` do kit.

## 2. Configuração de modelos

Rode `hermes config edit` e mescle manualmente o conteúdo de `hermes/config-snippet.yaml` com as chaves existentes em `~/.hermes/config.yaml`. Se `model` já estiver configurado, mude apenas `provider`/`default`. Não duplique chaves YAML; não cole dentro do `.env`.

Confirme `OPENROUTER_API_KEY` existente, mas não a compartilhe nem faça commit. Revise qualquer outra rota em `fallback_providers`, `auxiliary`, `delegation` e configurações herdadas para garantir que não use modelos pagos.

Rode:

```bash
hermes config check
hermes fallback check
```

`hermes fallback check --live` é opcional: consome requisições gratuitas. Para editar o jogo com ferramentas locais:

```bash
cd /caminho/para/Projeto-Moedas
hermes chat --toolsets "file,terminal,todo,skills"
```

Na sessão, use `/coin-commando-dev` ou cole `prompts/PRIMEIRA_SESSAO.md` (a skill pode precisar reiniciar a sessão para aparecer). Se precisar planejar sem editar, use `/plan <descrição>`.

## 3. Ambiente Python

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt pytest
python -m pytest -q
python main.py
```

No PowerShell Windows, ativação alternativa: `.\\.venv\\Scripts\\Activate.ps1`, ou execute `.\\.venv\\Scripts\\python.exe` diretamente. Testes gráficos headless Linux podem requerer EGL/OpenGL e `ARCADE_HEADLESS=1`; ver workflow `.github/workflows/tests.yml`. Se rodar no WSL, uma janela gráfica requer suporte WSLg ou execução nativa Windows.

## 4. Operação segura

Antes de alterações: crie branch `git switch -c feat/nome-da-melhoria` e verifique `git status`. Preserve e teste módulos existentes. Depois de editar: `python -m pytest -q` e `git diff --stat`.

## 5. Custos e limites

A escolha de modelos `:free` protege contra cobrança **somente nas rotas configuradas**. Chaves ou rotas auxiliares pagas preexistentes podem ser acionadas sem revisão. Para proteção adicional, use chave do OpenRouter dedicada ao projeto com limite de gastos adequado e monitore a página Activity. Limites gratuitos podem ser atingidos e são compartilhados pela conta; um modelo gratuito não garante imagens/vídeos gratuitos nem execução ilimitada.
