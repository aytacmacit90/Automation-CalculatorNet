from selenium import webdriver
import time



def BMICalculator(age,gender,height,weight):

    male = "m"
    female = "f"

    if gender == male:
        BMICalculate(age,"m",height,weight)
    elif gender == female:
        BMICalculate(age,"f",height,weight)
    else:
        print("Please enter a valid gender: m or f!!!")


def BMICalculate(a,g,h,w):


    driver = webdriver.Chrome("C:\chromedriver.exe")

    driver.set_page_load_timeout(10)
    driver.get("http://www.calculator.net/")
    time.sleep(5)

    # BMI link
    driver.find_element_by_xpath("//*[@id='hl2']/li[1]/a").click()
    time.sleep(3)
    # Chosing Metric System
    driver.find_element_by_xpath("//*[@id='topmenu']/ul/li[2]/a").click()
    time.sleep(3)
    #Age area
    driver.find_element_by_xpath("//*[@id='cage']").clear()
    driver.find_element_by_xpath("//*[@id='cage']").send_keys(str(a))

    #Gender Area
    if g == "m":
        driver.find_element_by_xpath("//*[@id='csex1']").click()
    else:
        driver.find_element_by_xpath("//*[@id='csex2']").click()


    #Height Area
    driver.find_element_by_xpath("//*[@id='cheightmeter']").clear()
    driver.find_element_by_xpath("//*[@id='cheightmeter']").send_keys(str(h))
    #Weight Area
    driver.find_element_by_xpath("//*[@id='ckg']").clear()
    driver.find_element_by_xpath("//*[@id='ckg']").send_keys(str(w))
    time.sleep(3)

    #Submit Button
    driver.find_element_by_xpath("//*[@id='content']/div[3]/div[2]/table[4]/tbody/tr/td[1]/input[2]").click()
    time.sleep(3)

    result =driver.find_element_by_xpath("//*[@id='content']/div[4]/div/b").text

    status =driver.find_element_by_xpath("//*[@id='content']/div[4]/div/font/b").text

    print(result)
    print(status)



# for male
BMICalculator(26,"m",167,64)
# for female
BMICalculator(25,"f",156,56)
# for invalid gender
BMICalculator(30,"b",180,96)
