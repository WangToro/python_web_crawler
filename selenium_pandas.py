from selenium import webdriver
from time import sleep
import pandas

browser = webdriver.Firefox()

browser.get('https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html')

element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/form/select/option[5]')

element.click()

sleep(3)

element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/form/a')

element.click()

sleep(3)

element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/main/div[4]/div[28]/div/div[1]/label/select/option[5]')

element.click()

sleep(5)

df = pandas.read_html(browser.page_source)[8]

print(df)