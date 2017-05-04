# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from wechat.models import VAccount, Blog

class RengzanPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

class RengZanImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img in item["image_urls"]:
            yield scrapy.Request(img, meta={'item': item})

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        image_url = ""
        avatar_url = ""
        if len(image_path) != 0:
            image_url = image_path[0]
            if len(image_path) >= 2:
                avatar_url = image_path[1]
        vAccount = VAccount(vName = item['vName'],
                            vAccount = item['vAccount'],
                            vQQ = item['vQQ'],
                            category = item['category'],
                            area = item['area'],
                            tags = item['tags'],
                            link = item['link'],
                            description = item['description'],
                            qrCode = image_url,
                            avatar = avatar_url,
                            crawl_url = item['crawl_url'],
                            )
        vAccount.save()
        return vAccount