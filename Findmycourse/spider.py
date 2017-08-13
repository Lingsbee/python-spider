from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image,ImageEnhance
import time
from pytesseract import *
from selenium.webdriver.chrome.options import Options


class  grabcourse:
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_extension('C:/Users/msi/AppData/Local/Google/Chrome/User Data/Default/Extensions/hehijbfgiekmjfkfjpbkbammjbdenadd/10.5.10.1_0.crx')
    # driver=webdriver.Chrome(chrome_options=chromeOptions)
    driver = webdriver.Ie( )
    driver.maximize_window()
    def spider(self):
        driver=self.driver
        driver.get('http://jwc.bjtu.edu.cn/')   
        driver.find_element_by_css_selector(' span > a:nth-child(1) > strong').click()
        time.sleep(0.5)
        ######登陆######
        #输入学号
        username=driver.find_element_by_id('TextBoxUserName')
        ActionChains(driver).move_to_element( username).perform()
        # yourname=input()
        username.send_keys('15281115')
        #输入密码
        password=driver.find_element_by_id('TextBoxPassword')
        ActionChains(driver).move_to_element(password).perform()
        # yourpassword= input()
        password.send_keys('maoxian123')
        #绕过验证码

        driver.find_element_by_id('ButtonLogin').click()
        time.sleep(2)
        driver.find_element_by_css_selector(' div.speedWay1 > span > a > strong').click()
        time.sleep(1)
        # driver.find_element_by_css_selector('#ctl00_ctl00_ctl00_ctl00_placeHolderContent_placeHolderContent_placeHolderMenuBar_navMenu_tvNavMenu > table:nth-child(1) > tbody > tr > td:nth-child(2)').click()
        url=driver.find_element_by_css_selector('#ctl00_ctl00_ctl00_ctl00_placeHolderContent_placeHolderContent_placeHolderMenuBar_navMenu_tvNavMenu > table:nth-child(1) > tbody > tr > td:nth-child(2)>a').get_attribute('href')
        driver.get(url)
        time.sleep(1)
        driver.switch_to_frame('topFrame')
        driver.find_element_by_css_selector('#moduleTab > tbody > tr > td.btn3 > a').click()
        driver.switch_to_default_content()
        driver.switch_to_frame('bottomFrame')
        driver.switch_to_frame('mainFrame')
        time.sleep(5)
        ######填入验证码#######

        # driver.save_screenshot('screenshot.png')
        # element=driver.find_element_by_css_selector('#yzm_div > img')
        # left = element.location['x']
        # top = element.location['y']
        # right = element.location['x'] + element.size['width']
        # bottom = element.location['y'] + element.size['height']
        # im = Image.open('screenshot.png')
        # im = im.crop((left, top, right, bottom))
        # im.save('screenshot.png')
        # im = im.convert('L')  # 将彩色图像转化为灰度图
        # #处理验证码
        # str=pytesseract.image_to_string(Image.open('screenshot.png'))
        # print(str)
        # checkout = driver.find_element_by_name('v_yzm')
        # checkout.send_keys(str)
        # driver.find_element_by_css_selector('#btnSure').click()
        # time.sleep(1)

        # driver.find_element_by_css_selector('#yzm_div > input[type="text"]').send_keys(checkout)

        ######输入课程信息########
        course = '60S183T'
        coursenum = '05'
        driver.find_element_by_css_selector('#xrxk_cxtj > tbody > tr > td > input[name="cxkcid"]').send_keys(course)
        driver.find_element_by_css_selector('#xrxk_cxtj > tbody > tr > td > input[name="cxkxh"]').send_keys(coursenum)

        find=False
        while find==False:
            driver.find_element_by_css_selector('#xrxk_cxtj > tbody > tr > td > img[title="条件查询课程"]').click()
            Frame=driver.find_element_by_xpath('//*[@id="mainTable"]/tbody/tr/td/iframe')
            driver.switch_to_frame(Frame)
        #寻找
            try:
                Get=driver.find_element_by_css_selector('#user > tbody >tr>td>input')
                Get.click()
                find=True

            except:
                driver.switch_to.parent_frame()


        # 提交
        driver.switch_to.parent_frame()
        submit = driver.find_element_by_xpath('//*[@id="xrxk_cxtj"]/tbody/tr/td/img[@title="保存任选课"]')
        submit.click()

if __name__=="__main__":
    grabcourse=grabcourse()
    grabcourse.spider()
