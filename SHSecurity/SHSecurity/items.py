# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShsecurityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    证券代码 = scrapy.Field()
    证券简称= scrapy.Field()
    监管类型= scrapy.Field()
    处理事由= scrapy.Field()
    涉及对象= scrapy.Field()
    处理日期= scrapy.Field()
    pass
