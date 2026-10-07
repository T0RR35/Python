# 🚀 Projeto GitHubAPI ContributorStats

O **GitHubAPI ContributorStats** é uma ferramenta Python desenvolvida para analisar repositórios do GitHub (públicos e **privados**) e gerar um **ranking detalhado dos colaboradores** com base em métricas reais de código. O projeto utiliza o Token de Acesso Pessoal (PAT) do GitHub para acessar os dados e lida com o processamento assíncrono das estatísticas da API, garantindo uma execução robusta e automática.

### 🎯 Objetivo

O objetivo principal é fornecer uma visão clara de quem mais contribuiu para um repositório, não apenas em termos de frequência de *commits*, mas também pelo **volume de linhas de código** adicionadas e removidas (**Impacto Líquido**). O resultado é exportado para um arquivo CSV de fácil consumo.

---

## 🛠️ Pré-requisitos

- **Python 3.7+** instalado.
- Acesso a um **Personal Access Token (PAT)** do GitHub com o *scope* **`repo`** marcado (necessário para repositórios privados).

---

## 🐍 Ambiente virtual (recomendado)
1. **Crie o ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source .venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install requests
```

---

## ⚙️ Execução

### 1. Configuração

Substitua o *placeholder* `"SEU_TOKEN_AQUI"` (ou o token de exemplo) pela sua chave real de **PAT** na variável `GITHUB_TOKEN` do arquivo `contributor_stats.py`.

### 2. Comando Principal

Execute o script principal, passando a URL do repositório como argumento (ou usando a URL padrão definida no script):

```bash
python contributor_stats.py <URL_DO_REPOSITORIO_AQUI>
```

**Exemplo (com a URL padrão):**
```bash
python contributor_stats.py
```

## 📊 O que cada função faz

Abaixo seguem as assinaturas das funções presentes no script e uma explicação curta do propósito de cada uma:

| Função | Assinatura | Propósito |
| :--- | :--- | :--- |
| **`parse_repo_url`** | `(repo_url: str) -> tuple[str, str] | None` | Extrai o **dono** e o **nome** do repositório a partir da URL. |
| **`fetch_contributors_stats`** | `(owner: str, repo_name: str) -> list | None` | Faz requisições à API, implementando um **loop de retentativa** para lidar com o processamento de dados (`202 Accepted`). |
| **`fetch_last_commit_date`** | `(owner: str, repo_name: str, username: str) -> str` | Busca a **data exata do último commit** de um usuário no repositório, retornando no formato `DD/MM/YYYY`. |
| **`generate_ranking`** | `(contributors_data: list, owner: str, repo_name: str) -> list` | Processa os dados brutos, calcula o **Impacto Líquido** (`Inseridas - Deletadas`) e ordena os colaboradores. |
| **`export_to_csv`** | `(ranking: list, repo_name: str)` | Cria e salva um arquivo CSV com o ranking final, usando ponto e vírgula (`;`) como delimitador. |
| **`main`** | `(repo_url: str)` | Função principal que coordena a execução do script: analisa contribuições, gera ranking e exporta CSV. |

---

## 📚 Documentação e Links Úteis

- 🔑 **Página de Geração de Tokens (PATs) no GitHub:** [github.com/settings/tokens](https://github.com/settings/tokens)
- 🔑 **Como criar seu Personal Access Token (PAT):** [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- 🧩 **Documentação oficial da API do GitHub (Estatísticas):** [REST API Endpoints for Repository Statistics](https://docs.github.com/en/rest/metrics/statistics?apiVersion=2022-11-28)
- 🐍 **Documentação oficial do módulo `requests`:** [Python Requests](https://docs.python-requests.org/en/latest/)

---

## 🧾 Licença

Este projeto é disponibilizado sob a licença **MIT**.

---