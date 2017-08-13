import selenium
from selenium import webdriver
import time
import requests
import re
from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait


class akqj10:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.stocktickers = []
    def getHushenlist(self):
        url = 'http://data.eastmoney.com/other/index/hs300.html'
        self.driver.get(url)
        time.sleep(1)
        for j in range(1, 2):
            data = self.driver.find_elements_by_css_selector('#dt_1 > tbody > tr')
            for each in data:
                stocktickers = each.find_element_by_css_selector('td:nth-child(2) >a')
                self.stocktickers.append(stocktickers.text)
            nextpage = self.driver.find_element_by_css_selector('#PageCont > a:nth-child(8)').click()
            time.sleep(1)
    def search(self):
        self.getHushenlist()
        driver=self.driver
        url = 'http://stockpage.10jqka.com.cn/'
        for i in range(0,300):
            try:
                url = url + self.stocktickers[i]
                driver.get(url)
                time.sleep(1)
                self.news()
            except:
                driver.quit()
    def news(self):
        driver = self.driver
        newslist=driver.find_element_by_css_selector('#xwgg > ul.news_list')
        news=newslist.find_elements_by_css_selector('li')
        for each in news:
            each.click()
            driver.switch_to_window(driver.window_handles[1])
            try:
                level =driver.find_element_by_css_selector('body > div.content-1200 > div.module-l.fl > div.pjtxprice').get_attribute('class')
                print(level)
                title=driver.find_element_by_css_selector('body > div.content-1200 > div.module-l.fl > div.atc-head').text
                time=driver.find_element_by_css_selector('#pubtime_baidu')
                passage=driver.find_element_by_css_selector('body > div.content-1200 > div.module-l.fl > div.atc-content').text.replace('\r', '').replace('\n', '').replace(' ', '')
                print(title)
                print(time)
                print(passage)
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
            except:
                try:
                    title = driver.find_element_by_css_selector(
                        'body > div.content-1200 > div.module-l.fl > div.atc-head').text
                    passage = driver.find_element_by_css_selector(
                        'body > div.content-1200 > div.module-l.fl > div.atc-content').text.replace('\r', '').replace('\n', '').replace(' ', '')
                    time = driver.find_element_by_css_selector('#pubtime_baidu')
                    print(time)
                    print(title)
                    print(passage)
                except:
                    pass
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
if __name__ == "__main__":
    spider=akqj10()
    spider.search()