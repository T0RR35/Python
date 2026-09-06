# G1 Spider
Este projeto é um spider feito com Scrapy para coletar notícias do site [G1](https://g1.globo.com/). O spider navega pelas páginas de notícias (incluindo o carregamento incremental de conteúdo) e extrai o título e o link de cada notícia, salvando todos os dados em um arquivo JSON.

## Estrutura do Projeto
```
scrapy-g1/
├── G1_scraper.py
└── noticias.json
```

## Como Usar

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nome-da-pasta
   ```

2. **Crie e ative o ambiente virtual:**
   É recomendável usar um ambiente virtual para gerenciar suas dependências.
   Siga os passos abaixo para configurar um ambiente virtual:

   a. Crie um ambiente virtual usando o seguinte comando:
   ```bash
   python3 -m venv .venv
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
   Certifique-se de que você tenha o Python e o Scrapy instalados.
   Você pode instalar o Scrapy usando o seguinte comando:
   ```bash
   pip install scrapy
   ```

4. **Execute o spider**:
   Para executar o spider, você pode usar o seguinte comando:
   ```bash
   scrapy runspider G1_scraper.py  # roda um spider diretamente de um arquivo Python
   scrapy crawl G1_scraper         # roda um spider dentro de um projeto Scrapy
   ```
   O spider irá coletar as notícias disponíveis, seguindo a paginação incremental do site, e salvar os dados em `noticias.json`.

## Resultados
Após a execução do spider, você encontrará um arquivo chamado `noticias.json` na pasta do projeto. Este arquivo conterá as notícias coletadas em formato JSON. O conteúdo do arquivo terá a seguinte estrutura:
```json
[
    {
        "titulo": "Título da notícia 1",
        "link": "https://g1.globo.com/noticia-1.ghtml"
    },
    {
        "titulo": "Título da notícia 2",
        "link": "https://g1.globo.com/noticia-2.ghtml"
    }
]
```

## Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests se você tiver sugestões de melhorias!