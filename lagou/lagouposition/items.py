# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagoupositionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    workName=scrapy.Field()
    companyName = scrapy.Field()
    companySize = scrapy.Field()
    positionName = scrapy.Field()
    companyLabelList = scrapy.Field()
    salary = scrapy.Field()
    pass
