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
                link = noticia.css('a.feed-post-link::attr(href)').get()
                if link:
                    yield response.follow(
                    link,
                    callback=self.get_detalhe,
                )


            self.page += 1
            # Segue para a próxima página
            yield scrapy.Request(
                f"https://g1.globo.com/index/feed/pagina-{self.page}.ghtml",
                meta={"page": self.page},
            )

        # Quando não há mais páginas, salva os dados acumulados em um arquivo JSON
        with open('noticias.json', 'w', encoding='utf-8') as f:
            json.dump(self.noticias_list, f, ensure_ascii=False, indent=4)

    def get_detalhe(self, response):
        self.titulo = response.css('h1.content-head__title::text').get()
        self.subtitulo = response.css('h2.content-head__subtitle::text').get()
        self.data = response.css('div.content-publication-data__text time::text').get()
        self.resumo = response.css('p.content-text__container::text').get()

        noticia_data = {
            'titulo': self.titulo,
            'data': self.data,
            'subtitulo': self.subtitulo,
            'resumo': self.resumo
        }
        self.noticias_list.append(noticia_data)


process = CrawlerProcess()
process.crawl(NoticiasSpider)
process.start()