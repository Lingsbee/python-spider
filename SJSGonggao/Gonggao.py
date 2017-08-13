from selenium import webdriver
import time
import unittest
import requests
from lxml import etree
class Gonggao:
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        # USER_AGENTS = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    def spider(self):
        driver=self.driver
        driver.maximize_window()
        driver.get('http://www.sse.com.cn/disclosure/announcement/general/')
        time.sleep(1)
        for j in range(1,3):
            j = str(j+1);
            urls = driver.find_elements_by_css_selector('#sse_list_1 > dl > dd>a')
            # url=urls[0].get_attribute('href')
            # print(url)
            for each in urls:
                url=each.get_attribute('href')
                print(url)
                self.analyse(url)
            element = driver.find_element_by_xpath('//*[@class="pagination"]/li/a[@page=' + j + ']/span')
            element.click()
            time.sleep(3)
    def analyse(self,url):
        html=requests.get(url)
        html.encoding='utf-8'
        selector = etree.HTML(html.text)
        title = selector.xpath('//div[@class="article-infor"]/h2/text()')[0]
        print(title)
        wens = selector.xpath('//div[@class="allZoom"]/p//text()')
        for each in wens:
            print(each)

if __name__ == "__main__":
    Gonggao=Gonggao()
    Gonggao.spider()