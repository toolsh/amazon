# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class XcaAmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    search_id = Field()
    asin = Field()
    link = Field()
    desc = Field()
