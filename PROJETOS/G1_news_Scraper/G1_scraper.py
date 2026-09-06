import scrapy
from scrapy.crawler import CrawlerProcess
import json

class NoticiasSpider(scrapy.Spider):
    name = "Noticias"
    start_urls = ['https://g1.globo.com/']

    noticias_list = []
    page = 1

    def parse(self, response):

        if self.page < 10:
            for noticia in response.css('div.feed-post'):
                noticia_data = {
                    'titulo': noticia.css('p::text').get(),
                    'link': noticia.css('a.feed-post-link::attr(href)').get()
                }
                self.noticias_list.append(noticia_data)

            self.page += 1
            # Segue para a próxima página
            yield scrapy.Request(
                f"https://g1.globo.com/index/feed/pagina-{self.page}.ghtml",
                meta={"page": self.page},
            )

        # Quando não há mais páginas, salva os dados acumulados em um arquivo JSON
        with open('noticias.json', 'w', encoding='utf-8') as f:
            json.dump(self.noticias_list, f, ensure_ascii=False, indent=4)

# Executa o spider
process = CrawlerProcess()
process.crawl(NoticiasSpider)
process.start()