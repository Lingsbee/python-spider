# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import requests
import re
from lxml import etree
class Hushen:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.stocktickers = []

    # -*- 先获取沪深名单再获取文本 -*-
    def search(self):
        self.getHushenlist()
        driver = self.driver
        url='http://guba.eastmoney.com/'
        driver.get(url)
        time.sleep(1)
        for i in range(293,301):
            inputname=self.stocktickers[i]
            # inputname=('金隅股份')
            enter=driver.find_element_by_css_selector('#gbhsckey').clear()
            driver.find_element_by_css_selector('#gbhsckey').send_keys(inputname)
            search=driver.find_element_by_css_selector('#gbhscsbm').click()
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(1)
            #############################        get news       ##############################
            try:
                if(driver.find_element_by_css_selector('#searchbarlist > ul > li:nth-child(1) > div > a')):
                    switchurl=driver.find_element_by_css_selector('#searchbarlist > ul > li:nth-child(1) > div > a').get_attribute('href')
                    driver.get(switchurl)
                    click = False
                    while click == False:
                        # 寻找
                        try:
                            Get = driver.find_element_by_css_selector('#pagenav > ul > li:nth-child(3) > a')
                            Get.click()
                            click = True
                        except:
                            pass
            except:
                click = False
                while click == False:
                    # 寻找
                    try:
                        Get = driver.find_element_by_css_selector('#pagenav > ul > li:nth-child(3) > a')
                        Get.click()
                        click = True
                    except:
                        pass
            nextpage=True
            page = 1
            while nextpage:
                time.sleep(1)
                Newslist = driver.find_element_by_css_selector('#articlelistnew')
                news = Newslist.find_elements_by_css_selector('div')
                start=1
                date=0
                start = 1
                date = 0
                neednate = 7
                for each in news:
                    if (start == 1):
                        start = 2
                    else:
                        try:
                            title=each.find_element_by_css_selector('span.l3>a').get_attribute('title')
                            date = each.find_element_by_css_selector('span.l6').text
                            date = int(re.search('(\d*)', date, re.S).group(1))
                            if '融资融券'in title:
                                pass
                            else:
                                if (date >= neednate):
                                    newsurl = each.find_element_by_css_selector(' span.l3 > a').get_attribute('href')
                                    self.analysenews(newsurl,inputname)
                                    print(newsurl)
                                else:
                                    break
                        except:
                            pass
                        if (date < neednate):
                            break
                if (date < neednate):
                    break
                page=page+1
                pagee=str(page)
                try:
                    driver.find_element_by_xpath( '//*[@id="articlelistnew"] / div[@class="pager"] / span / span / a[@data-page="'+pagee+'"]').click()
                except:
                    nextpage = False
             ####################           get announcement        ##############################
            nextpage = True
            click=False
            while click == False:
                # 寻找
                try:
                    Get = driver.find_element_by_css_selector('#pagenav > ul > li:nth-child(4) > a')
                    Get.click()
                    click = True
                except:
                    pass
            page = 1
            while nextpage:
                time.sleep(1)
                Newslist = driver.find_element_by_css_selector('#articlelistnew')
                news = Newslist.find_elements_by_css_selector('div')
                start = 1
                date = 0
                neednate = 7
                for each in news:
                    if (start == 1):
                        start = 2
                    else:
                        try:
                            date = each.find_element_by_css_selector('span.l6').text
                            date = int(re.search('(\d*)', date, re.S).group(1))
                            if (date >= neednate):
                                newsurl = each.find_element_by_css_selector(' span.l3 > a').get_attribute('href')
                                self.analyseannoment(newsurl,inputname)
                                print(newsurl)
                            else:
                                break
                        except:
                            pass
                        if (date < neednate):
                            break
                if (date < neednate):
                    break
                page = page + 1
                pagee = str(page)
                try:
                    driver.find_element_by_xpath('//*[@id="articlelistnew"] / div[@class="pager"] / span / span / a[@data-page="' + pagee + '"]').click()
                except:
                    nextpage=False
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

    def analysenews(self,url,stock):
        html = requests.get(url)
        selector = etree.HTML(html.text)
        time = selector.xpath('//*[@id="zwconttb"]/div[2]')[0].text.replace('股吧网页版','').replace('发表于','')
        txt = time + '&'+stock+'&'

        title = selector.xpath('//*[@id="zwconttbt"]')[0].text.replace('\r', '').replace(' ', '').replace('\n', '').replace('　','')
        txt = txt + title + '&'
        article = selector.xpath('//*[@id="zw_body"]/ul/li/p')
        article = selector.xpath('//*[@id="zw_body"]/ul/li/p')
        if (article):
            pass
        else:
            article = selector.xpath('//*[@id="zw_body"]/p')
        for each in article:
            if (each.text):
                paragraph = each.text.replace('\r', '').replace('\n', '').replace(' ', '')
                txt = txt + paragraph
        txt = txt+ '\n'
        with open('news.txt', 'a') as f:
            f.write(txt)
            f.close()

    def analyseannoment(self, url,stock):
        html = requests.get(url)
        selector = etree.HTML(html.text)
        time = selector.xpath('//*[@id="zwconttb"]/div[2]')[0].text
        txt = time + '&' + stock + '&'
        title = selector.xpath('//*[@id="zwconttbt"]')[0].text.replace('\r', '').replace(' ', '').replace('\n', '').replace( '　', '')
        txt = txt + title + '&'
        article = selector.xpath('//*[@id="zwconbody"]/div/p/text()')
        for each in article:
            txt = txt + each
        txt=txt.replace('提示：本网不保证其真实性和客观性，一切有关该股的有效信息，以交易所的公告为准，敬请投资者注意风险。', '')
        txt=txt+'\n'
        with open('annoucement.txt', 'a') as f:
            f.write(txt)
            f.close()

    def getHushenlist(self):
        url = 'http://data.eastmoney.com/other/index/hs300.html'
        self.driver.get(url)
        time.sleep(1)
        for j in range(1, 7):
            data = self.driver.find_elements_by_css_selector('#dt_1 > tbody > tr')
            for each in data:
                stocktickers = each.find_element_by_css_selector('td:nth-child(3) >a')
                self.stocktickers.append(stocktickers.text)
            nextpage = self.driver.find_element_by_css_selector('#PageCont > a:nth-child(8)').click()
            time.sleep(1)

if __name__ == "__main__":
    spider=Hushen()
    spider.search()
