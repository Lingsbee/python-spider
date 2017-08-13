# -*- coding: utf-8 -*-
import scrapy
import re
from items  import HushenItem

class HushensSpider(scrapy.Spider):
    name = "Hushens"
    # allowed_domains = ["http://guba.eastmoney.com/"]
    start_urls = ['http://http://guba.eastmoney.com']

    def parse(self, response):
        selector = scrapy.Selector(response)
        item = HushenItem()
        Enter=selector.css('#gbhsckey')


        pass
        
