import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import JobPagination

# class StationDetailSpider(CrawlSpider):
#     name = 'train'
#     start_urls = [someOtherWebsite]
#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//a[@class='next_page']"), follow=True),
#         Rule(LinkExtractor(allow=r"/trains/\d+$"), callback='parse_trains')
#     )
#     def parse_trains(self, response):
#         '''do your parsing here''
"div[data-automation='pagination-dropdown']+a::attr(href)"

class JobsdbSpider(CrawlSpider):
    name = "jobsdb"
    allowed_domains = ["hk.jobsdb.com"]
    start_urls = ["https://hk.jobsdb.com/hk/search-jobs/data-scientist/1"]
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    max_page = 10
    rules = (
        Rule(
            LinkExtractor(
                restrict_css=("div[data-automation='pagination-dropdown']+a",),
                attrs=("href",),
            ),
            follow=True,
            callback="parse_page",
        ),
    )

    def parse_page(self, response):
        o = JobPagination()
        o["url"] = response.url
        print("************NOK****************", o)
        yield o
