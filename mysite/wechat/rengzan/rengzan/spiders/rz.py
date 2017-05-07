# -*- coding: utf-8 -*-
import scrapy
import urlparse
from rengzan.items import VAccountItem, BlogItem

class RzBlogSpider(scrapy.Spider):
    name = "rzBlog"
    allowed_domains = ["rengzan.com"]
    start_urls = ['http://www.rengzan.com/photo-index-id-191.html']

    def parse(self, response):
        item_urls = response.css(".ft .list-h3 a::attr(href)").extract()
        for url in item_urls:
            yield scrapy.Request(urlparse.urljoin(response.url, url), callback=self.parse_item)

        page_urls = response.css(".pagewx a::attr(href)").extract()
        for url in page_urls:
            yield scrapy.Request(urlparse.urljoin(response.url, url), callback=self.parse)

    def parse_item(self, response):
        title = response.css(".content-box .up-box .list-h3::text").extract_first()
        contents = response.css(".entry p::text").extract()
        vName = response.css(".R-mainbox1 .author-info .userinf a::text").extract_first()
        vAccount = response.css(".R-mainbox1 .author-info .summary::text").extract_first()

        blog = BlogItem()
        blog['title'] = title
        blog['content'] = "\n".join(contents)
        blog['vName'] = vName
        blog['vAccount'] = vAccount
        return blog

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
        vName, vAccount, vQQ, category, area, tags, link = \
        "",    "",       "",  "",        "",  [],   []
        for container in containers:
            x = container.css("::text").extract()
            x = [j.strip() for j in x if j.strip() != ""]
            if len(x) >= 2:
                if u"微信名称：" in x[0]:
                    vName = x[1]
                    print(vName)
                if u"微信帐号：" in x[0]:
                    vAccount = x[1]
                    print(vAccount)
                if u'客服QQ：' in x[0]:
                    vQQ = x[1]
                    print(vQQ)
                if u'行业分类：' in x[0]:
                    category = x[1]
                    print(category)
                if u'所在地区：' in x[0]:
                    area = x[1]
                    print(area)
                if u'标签tag：' in x[0]:
                    tags = x[1:]
                    print(tags)
                if u'关联推广：' in x[0]:
                    link = container.css("a::attr(href)").extract()
        try:
            description = response.css(".main_case.l .scroll.l p::text").extract_first().strip()
        except:
            description = ""
        qrCodeUrlPart = response.css(".main_case.l .cont_cat.l img::attr(src)").extract_first().strip()
        qrCodeUrl = urlparse.urljoin(response.url, qrCodeUrlPart)
        avatar_url = response.css(".main_case.l .wrappic.l img::attr(src)").extract_first().strip()
        avatar_url = urlparse.urljoin(response.url, avatar_url)
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
        item['image_urls'] = [qrCodeUrl, avatar_url]
        item['crawl_url'] = crawl_url
        return item

