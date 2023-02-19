# coding=utf-8 
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
import sys, traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

# 配置加载策略
# desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
# desired_capabilities["pageLoadStrategy"] = "eager"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
chrome_options = Options()  # 实例化一个启动参数对象

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  # 这里看清楚了，不是add_argument
# chrome_options.add_argument('--window-size=1366,1400')  # 设置浏览器窗口大小
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}  # 禁止加载图片和CSS样式
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument('window-size=1024,768')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--headless')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行


# driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄



driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄

wait = WebDriverWait(driver, 3)  # 后面可以使用wait对特定元素进行等待
        # 3.访问打卡页面并模拟点击来打卡
UID = os.environ["UID"]
SERVERPUSHKEY = os.environ["SERVERPUSHKEY"]

url_login = "https://jkjc.xust.edu.cn/#/pages/index/index?uid=" + UID
driver.get(url_login)
time.sleep(3)
a1 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-form/span/uni-view[1]/uni-view/uni-view/uni-view[2]/uni-view/uni-radio-group/uni-label[2]/uni-view[2]')
a1.click()
time.sleep(2)
a2 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-form/span/uni-view[2]/uni-view/uni-view[1]/uni-view[2]/uni-view/uni-radio-group/uni-label[2]/uni-view[2]')
a2.click()
time.sleep(2)
a3 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-form/span/uni-view[3]/uni-view/uni-view[1]/uni-view[2]/uni-view/uni-radio-group/uni-label[2]/uni-view[2]')
a3.click()
time.sleep(2)
a4 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-form/span/uni-view[4]/uni-view/uni-view[1]/uni-view[2]/uni-view/uni-radio-group/uni-label[2]/uni-view[2]')
a4.click()
time.sleep(2)
a5 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-form/span/uni-view[6]/uni-view/uni-view[1]/uni-view[2]/uni-view/uni-radio-group/uni-label[3]/uni-view[2]')
a5.click()
time.sleep(2)
a6 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-button')
a6.click()
time.sleep(3) 
a7 = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view')
text = a7.text
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)
print("打卡信息：", text)
if text == "提交成功" and SERVERPUSHKEY:
        driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄
        url = "https://api2.pushdeer.com/message/push?pushkey=" + SERVERPUSHKEY + "&text=✅今日健康打卡已完成✅"
        driver.get(url)

if text != "提交成功" and SERVERPUSHKEY:
        driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄
        url = "https://api2.pushdeer.com/message/push?pushkey=" + SERVERPUSHKEY + "&text=❌打卡失败❌可能为学校打卡页面崩溃，将在15分钟后再次尝试并提醒，直至成功。如需要请前往Github手动Cancle掉本次Action并手动打卡"
