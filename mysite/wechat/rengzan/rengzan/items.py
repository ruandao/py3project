# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from wechat.models import VAccount, Blog


class VAccountItem(scrapy.Item):
    vName = scrapy.Field()
    vAccount = scrapy.Field()
    vQQ = scrapy.Field()
    category = scrapy.Field()
    area = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    crawl_url = scrapy.Field()

class BlogItem(scrapy.Item):
    vName = scrapy.Field()
    vAccount = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
