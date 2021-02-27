import scrapy


class JobsdbSpider(scrapy.Spider):
    name = 'jobsdb'
    allowed_domains = ['hk.josbdb.com']
    start_urls = ['http://hk.josbdb.com/']

    def parse(self, response):
        pass
