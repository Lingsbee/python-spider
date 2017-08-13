# -*- coding: utf-8 -*-
import scrapy
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from items import ShsecurityItem
import time
class SecuritySpider(scrapy.Spider):
    name = "security"
    # allowed_domains = ["http://www.sse.com.cn/disclosure/credibility/supervision/measures/"]
    start_urls = ['http://www.sse.com.cn/disclosure/credibility/supervision/measures//']
    def parse(self, response):
        item=ShsecurityItem()
        browser = webdriver.PhantomJS()
        browser.get(response.url)
        browser.set_window_size(1920, 1080)
        time.sleep(3)
        for j in range(1,): #抓取一页
            j = str(j + 1)
            for i in range(1,16): #抓取每一行
                i=str(i+1)
                证券代码 = browser.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/div/table/tbody/tr['+i+']/td[1]')[0].text.replace(' ', '').replace('\n', '')
                证券简称 = browser.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/div/table/tbody/tr['+i+']/td[2]')[0].text.replace(' ', '').replace('\n', '')
                监管类型 = browser.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/div/table/tbody/tr['+i+']/td[3]')[0].text.replace(' ', '').replace('\n', '')
                处理事由 = browser.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/div/table/tbody/tr['+i+']/td[4]')[0].text.replace(' ', '').replace('\n', '')
                涉及对象 = browser.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/div/table/tbody/tr['+i+']/td[5]')[0].text.replace(' ', '').replace('\n', '')
                处理日期 = browser.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/div/table/tbody/tr['+i+']/td[6]')[0].text.replace(' ', '').replace('\n', '')
                print(证券简称)
                print(监管类型)
                print(处理事由)
                print(涉及对象)
                print(处理日期)
                item['证券代码'] = 证券代码
                item['证券简称'] = 证券简称
                item['监管类型'] = 监管类型
                item['处理事由'] = 处理事由
                item['涉及对象'] = 涉及对象
                item['处理日期'] = 处理日期
                yield item

            '''翻页'''
            element=browser.find_element_by_xpath('//*[@id="panel-1"]/div[2]/nav/ul/li/a[@page='+j+']/span')
            element.click()
            time.sleep(3)