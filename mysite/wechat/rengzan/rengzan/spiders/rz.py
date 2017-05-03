# -*- coding: utf-8 -*-
import scrapy
import urlparse
from rengzan.items import VAccountItem, BlogItem

class RzSpider(scrapy.Spider):
    name = "rz"
    allowed_domains = ["rengzan.com"]
    start_urls = ['http://www.rengzan.com/weixin-news-id-90.html']

    def parse(self, response):
        item_urls = response.css("p.userinf.clearfix a::attr(href)").extract()
        for url in item_urls:
            yield scrapy.Request(urlparse.urljoin(response.url, url), callback=self.parse_item)

        page_urls = response.css(".pagewx a::attr(href)").extract()
        for url in page_urls:
            yield scrapy.Request(urlparse.urljoin(response.url, url), callback=self.parse)

    def parse_item(self, response):
        containers = response.css(".cont.l ul li")
        vName = containers[0].css("::text").extract()[2].strip()
        vAccount = containers[1].css("::text").extract()[2].strip()
        vQQ = containers[2].css("::text").extract()[2].strip()
        try:
            category = containers[3].css("abbr::text").extract()[0].strip()
        except:
            category = ""
        area = containers[4].css("::text").extract()[2].strip()
        tags = containers[5].css("a::text").extract()
        try:
            link = containers[7].css("a::attr(href)").extract()
        except:
            link = ""
        description = response.css(".main_case.l .scroll.l p::text").extract_first().strip()
        qrCodeUrlPart = response.css(".main_case.l .cont_cat.l img::attr(src)").extract_first().strip()
        qrCodeUrl = urlparse.urljoin(response.url, qrCodeUrlPart)
        crawl_url = response.url

        item = VAccountItem()
        item['vName'] = vName
        item['vAccount'] = vAccount
        item['vQQ'] = vQQ
        item['category'] = category
        item['area'] = area
        item['tags'] = ",".join(tags)
        item['link'] = ",".join(link)
        item['description'] = description
        item['image_urls'] = [qrCodeUrl]
        item['crawl_url'] = crawl_url
        return item

