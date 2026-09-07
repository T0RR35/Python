# G1 Spider

Este projeto é um spider feito com Scrapy para coletar notícias do site [G1](https://g1.globo.com/). O spider navega pelas páginas de listagem de notícias (seguindo a paginação incremental do feed), acessa cada notícia individualmente e extrai título, data de publicação, subtítulo e resumo, salvando todos os dados em um arquivo JSON.

## Estrutura do Projeto

```
scrapy-g1/
├── G1_scraper.py
├── noticias.json
└── requirements.txt
```

## Como Usar

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nome-da-pasta
   ```

2. **Crie e ative o ambiente virtual:**

   É recomendável usar um ambiente virtual para gerenciar suas dependências.

   a. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   ```

   b. Ative o ambiente virtual:
   - No macOS e Linux:
     ```bash
     source .venv/bin/activate
     ```
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```

3. **Instale as dependências:**

   Certifique-se de que o Python e o Scrapy estejam instalados:
   ```bash
   pip install scrapy
   ```

4. **Execute o spider**:

   O nome do spider definido no código é `Noticias`. Rode com um dos comandos abaixo, dependendo de como o projeto está organizado:

   - Se `G1_scraper.py` for um arquivo solto (sem estrutura de projeto Scrapy):
     ```bash
     scrapy runspider G1_scraper.py
     ```

   - Se o arquivo estiver dentro de um projeto Scrapy (com `scrapy.cfg` na raiz):
     ```bash
     scrapy crawl Noticias
     ```

   O spider irá coletar as notícias disponíveis, seguindo a paginação incremental do site, e salvar os dados em `noticias.json`.

## Resultados

Após a execução do spider, você encontrará o arquivo `noticias.json` na pasta do projeto, contendo as notícias coletadas no seguinte formato:

```json
[
    {
        "titulo": "Título da notícia 1",
        "data": "07/09/2026 10:30",
        "subtitulo": "Subtítulo da notícia 1",
        "resumo": "Resumo ou trecho inicial da notícia 1"
    },
    {
        "titulo": "Título da notícia 2",
        "data": "07/09/2026 09:15",
        "subtitulo": "Subtítulo da notícia 2",
        "resumo": "Resumo ou trecho inicial da notícia 2"
    }
]
```

> **Observação:** os seletores CSS usados para extrair os campos dependem da estrutura HTML atual do G1, que pode mudar com o tempo. Se o spider parar de retornar dados, vale inspecionar o HTML da página e ajustar os seletores em `G1_scraper.py`.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests se você tiver sugestões de melhorias!