#-*- coding:utf-8 -*-
import re
import requests
import time
from lxml import etree
from selenium import webdriver
import urllib
def wet1():
    url = 'http://item.btime.com/37k8ve9mo319a9ano11rt9sgfue'
    html = requests.get(url)
    html.encoding='utf-8'
    text = re.search('data-type="news">(.*?)</h1>',html.text,re.S).group(1)
    print(text)
    url = re.search('<!-- 文章简介 -->(.*?)<!--end content-share-->',html.text,re.S).group(1)
    urls=re.findall('<p>(.*?)</p>',url,re.S)
    for each in urls:
        print(each)
def wet2():
    html ='''
    <div id="test1">content1</div>
    <div id="test2">content2</div>
    <div id="test3">content3</div>
    '''

    selector = etree.HTML(html)
    content = selector.xpath('//div')
    for each in content:
        print(each.text)

def test():
    driver = webdriver.PhantomJS()
    driver.get("http://www.du7.cc/modules/article/search.php?searchkey=%C4%A7%B7%A8&searchtype=articlename&page=1")
    list=driver.find_element_by_xpath('//*/body/div[@class="layout"]/div[@id="mainbox"]/table/tbody/tr[2]')
    print(list)


def test1():
    url = 'http://guba.eastmoney.com/list,603993.html'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    # frame=driver.find_element_by_css_selector('body > div.mainFrame')
    # driver.switch_to_frame(frame)
    driver.find_element_by_css_selector('#pagenav > ul > li:nth-child(3) > a').click()
    Newslist = driver.find_element_by_css_selector('#articlelistnew')
    news = Newslist.find_elements_by_css_selector('div')
    start = 1
    date = 0
    for each in news:
        if (start == 1):
            start = 2
        else:
            try:
                date = each.find_element_by_css_selector('span.l6').text
                date = int(re.search('(\d*)', date, re.S).group(1))
                neednate = 7
                if (date >= neednate):
                    newsurl = each.find_element_by_css_selector(' span.l3 > a').get_attribute('href')
                    # analysenews(newsurl)
                    print(newsurl)
                else:
                    break
            except:
                pass

def wet3():
    url='http://guba.eastmoney.com/news,603993,666242974.html'
    html = requests.get(url)
    selector = etree.HTML(html.text)
    time = selector.xpath('//*[@id="zwconttb"]/div[2]')[0].text
    txt = time + '&'
    title = selector.xpath('//*[@id="zwconttbt"]')[0].text.replace('\r', '').replace(' ', '').replace('\n', '').replace(
        '　', '')
    txt = txt + title + '&'
    article = selector.xpath('//*[@id="zw_body"]/ul/li/p')
    if (article):
        pass
    else:
        article = selector.xpath('//*[@id="zw_body"]/p')
    for each in article:
        if (each.text):
            paragraph = each.text.replace('\r', '').replace('\n', '').replace(' ', '')
    txt = txt.replace('股吧网页版', '').replace('发表于', '') + paragraph + '\n'
    print(txt)
def jianzhi():
    url='http://mm.faloo.com/girl/0/1.html?t=0&k=%D6%D8%C9%FA'
    html = requests.get(url)
    print(html.text)
    selector = etree.HTML(html.text)
    title=selector.xpath('//*[@class="l_page"]/table/tr/td[1]/font/span/font/font[4]/strong/text()')
    print(title)
jianzhi()

