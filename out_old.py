'''
实现：申请今日临时出校
'''

import os
from time import sleep
from random import choice
from selenium import webdriver
from selenium.webdriver.support import expected_conditions

USERNAME   = os.environ['ID']
PASSWORD   = os.environ['PASSWORD']

reasons = ['就餐', '出游', '探亲访友']

print('初始化浏览器...')
driver = None
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
option = webdriver.ChromeOptions()
option.headless = True
option.add_argument('user-agent='+ua)
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=option)

print('正在申请出校...')
# 统一认证登录
# driver.get('https://ids.hit.edu.cn/authserver/')
driver.get('http://ivpn.hit.edu.cn')
driver.find_element_by_id('mobileUsername').send_keys(USERNAME)
driver.find_element_by_id('mobilePassword').send_keys(PASSWORD)
driver.find_element_by_id('load').click()
sleep(1)

# 进入申请出校页面
## method1: 直接输网址, 进不去
# driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/yqxx')
# driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsCxsq')
## method2: 从学工主页点击进入
# driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsHome')    
driver.get('http://xg-hit-edu-cn-s.ivpn.hit.edu.cn:1080/zhxy-xgzs/xg_mobile/xsHome')
driver.execute_script('wjdc()')
# print(driver.page_source)
# 点击“新建”
driver.find_element_by_class_name('right_btn').click()
sleep(1)
# 新建页面
# 出校类型 点击“临时出校”
driver.find_element_by_xpath("//label[@for='cxlx01']").click()
# 出校日期选第一个（今天）
driver.find_element_by_id('rqlscx').click()
sleep(.5)
driver.find_element_by_id('weui-picker-confirm').click()
# print current date
cur_date = driver.find_element_by_id('rqlscx').text
print('current date picked: ', cur_date)
# 填写出校理由
driver.find_element_by_id('cxly').send_keys(choice(reasons))
# 勾选一堆
# driver.find_element_by_id('cxlxdiv1').find_elements_by_xpath()
# checkboxes = driver.find_elements_by_xpath("//*[@id='cxlxdiv1']//input")
checkboxes = driver.find_elements_by_xpath("//*[@id='cxlxdiv1']/div[not(contains(@id, 'xslbxsyc'))]/label")  # 注：这里去掉了实际看不到的“已经与导师联系，导师知情同意”
for checkbox in checkboxes:
    checkbox.click()
# 提交
driver.execute_script('save()')
sleep(.5)
driver.execute_script('document.getElementsByClassName("weui-dialog__btn primary")[0].click()')
# driver.find_element_by_class_name('weui-dialog__btn primary').click()

driver.quit()

print('申请today临时出校完成')
