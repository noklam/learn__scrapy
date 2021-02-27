import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rules
from scrapy.linkextractors import LinkExtractor

# class StationDetailSpider(CrawlSpider):
#     name = 'train'
#     start_urls = [someOtherWebsite]
#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//a[@class='next_page']"), follow=True),
#         Rule(LinkExtractor(allow=r"/trains/\d+$"), callback='parse_trains')
#     )
#     def parse_trains(self, response):
#         '''do your parsing here''


class JobsdbSpider(scrapy.Spider):
    name = "jobsdb"
    allowed_domains = ["hk.josbdb.com"]
    start_urls = ["http://hk.josbdb.com/"]
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    max_page = 10

    def parse(self, response):
        pass
