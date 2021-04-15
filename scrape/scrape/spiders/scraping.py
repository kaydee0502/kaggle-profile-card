import scrapy

class ScrapingSpider(scrapy.Spider):
    name = 'scraping'
    


    def start_requests(self):
        start_urls = [
                    'https://www.kaggle.com/aakashverma8900'
                ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        item = {}
        title = response.css('title::text').get()
        item['title'] = title
        yield item
