# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from xca_amazon.items import XcaAmazonItem

class AmazonSearch(scrapy.spiders.CrawlSpider):
    name = 'start_search'
    start_urls = [
        'https://www.amazon.com/s/?url=search-alias=electronics'
    ]
    allowed_domains = ["amazon.com"]

    def __init__(self, search='action camera', expect='VanTop', *args, **kwargs):
        super(AmazonSearch, self).__init__(*args, **kwargs)
        self.search = search
        self.expect = expect

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'field-keywords': self.search},
            dont_filter=True,
            callback=self.after_search
        )

    def after_search(self, response):
        # check login succeed before going on
        # if "authentication failed" in response.body:
        #     self.logger.error("Search failed")
        #     return
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        # for item in response.css('li.s-result-item'):
        for item in response.xpath('//li[re:test(@id, "result_\d*")]'):
            detail = item.css('a.s-access-detail-page')
            info = XcaAmazonItem()

            # print('-'*80)
            info['search_id'] = item.css('::attr(id)').extract_first()
            info['asin'] = item.css('::attr(data-asin)').extract_first()
            info['desc'] = detail.css('::text').extract(),
            info['link'] = detail.css('::attr(href)').extract()
            yield info

            found = [i for i,x in enumerate(list(info['desc'])) if self.expect.lower() in "".join(x).lower()]
            if found:
                print(info)
                raise CloseSpider('search keyword has been found.')

        next_page = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, dont_filter=True, callback=self.after_search)
