from selenium import webdriver
from time import sleep


browser = webdriver.Firefox()
browser.get('https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html')

element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/form/select/option[5]')

element.click()

element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/form/a')

element.click()

sleep(3)

element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/main/div[4]/div[28]/div/div[1]/label/select/option[5]')

element.click()

sleep(5)

table = browser.find_elements_by_xpath('//*[@id="report-table9"]/tbody')


#print(trlist)
#test
#trist = table.find_elements_by_tag_name('tr')


#for row in trlist:
    
    #tdlist = row.find_elements_by_tag_name('td')
    
    #for col in tdlist:
        #print(col.text + '\t', end = '')
        
    #print('/n')
