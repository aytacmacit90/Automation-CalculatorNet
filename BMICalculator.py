from selenium import webdriver
import time



driver = webdriver.Chrome("C:\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://www.calculator.net/")
time.sleep(5)


driver.find_element_by_xpath("//*[@id='hl2']/li[1]/a").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='topmenu']/ul/li[2]/a").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='cage']").clear()
driver.find_element_by_xpath("//*[@id='cage']").send_keys("27")

driver.find_element_by_xpath("//*[@id='csex1']").click()

driver.find_element_by_xpath("//*[@id='cheightmeter']").clear()
driver.find_element_by_xpath("//*[@id='cheightmeter']").send_keys("167")

driver.find_element_by_xpath("//*[@id='ckg']").clear()
driver.find_element_by_xpath("//*[@id='ckg']").send_keys("65")

time.sleep(3)


driver.find_element_by_xpath("//*[@id='content']/div[3]/div[2]/table[4]/tbody/tr/td[1]/input[2]").click()
time.sleep(3)

result =driver.find_element_by_xpath("//*[@id='content']/div[4]/div/b").text

status =driver.find_element_by_xpath("//*[@id='content']/div[4]/div/font/b").text
print(result)
print(status)