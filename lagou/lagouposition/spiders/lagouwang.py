# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from items import LagoupositionItem
class LagouwangSpider(scrapy.Spider):
    name = "lagouwang"
    #allowed_domains = ["www.lagou.com/zhaopin/"]
    start_urls = ['http://www.lagou.com/zhaopin//']
    def parse(self, response):
      #print(response.body)
      selector = scrapy.Selector(response)
      item = LagoupositionItem()
      result = selector.xpath('//li[@class = "con_list_item default_list"]')
      for each in result:
          workName=each.xpath('div[1]/div[1]/div[1]/a/h2/text()').extract()[0].replace(' ', '').replace('\n', '')
          companyName=each.xpath('div[1]/div[2]/div[1]/a/text()').extract()[0].replace(' ', '').replace('\n', '')
          companySize=each.xpath('div[1]/div[2]/div[2]/text()').extract()[0].replace(' ', '').replace('\n', '')
          positionName=re.search('<em>(.*?)</em',each.extract(),re.S).group(1).replace(' ', '').replace('\n', '')
          companyLabelList= re.search('<div class="li_b_r">(.*?)</div>',each.extract(),re.S).group(1)
          salary= re.search('<span class="money">(.*?)</span>',each.extract(),re.S).group(1)
          print(workName)
          print(companyName)
          print(companySize)
          print(positionName)
          print(companyLabelList)
          print(salary)
          item['workName'] = workName
          item['companyName'] = companyName
          item['companySize'] = companySize
          item['positionName'] = positionName
          item['companyLabelList'] =companyLabelList
          item['salary'] =salary
          yield item
          # nextPage = selector.xpath('//*[@id="s_position_list"]/div[2]/div/a[6]/@href').extract()

          string=response._url
          html = requests.get(string).text
          nextPage = re.search('<!-- 下一页处理 -->(.*?) class="page_no"', html, re.S).group(1)
          nextPage =re.search('<a href="(.*?)"', nextPage, re.S).group(1)
          if nextPage:
              yield scrapy.Request(nextPage, callback=self.parse)