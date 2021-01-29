import scrapy


class FormSpider(scrapy.Spider):
    name = "formspider"

    def start_requests(self,url):
        scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        return response.body