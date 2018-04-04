from selenium import webdriver
import time

result=""
status=""
name=""
surname=""
age=""
height=""
weight=""
filename=""

def CreateReport(name,surname,age,height,weight,result,status,information,filename):

    file = open(filename+".txt","w+")
    file.write("Name: " + name +"\n")
    file.write("Surname: " + surname +"\n")
    file.write("Age: " + age +"\n")
    file.write("Height: " + height +"\n")
    file.write("Weight: " + weight +"\n")
    file.write("Result: " + result +"\n")
    file.write("Status: " + status +"\n")
    file.write("Important Information: " + information + "\n")
    file.close()

def BMICalculator(name,surname,age,gender,height,weight):

    male = "m"
    female = "f"

    if gender == male:
        BMICalculate(name,surname,age,"m",height,weight)
    elif gender == female:
        BMICalculate(name,surname,age,"f",height,weight)
    else:
        print("Please enter a valid gender: m or f!!!")


def BMICalculate(n,s,a,g,h,w):


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

    time.sleep(3)

    status =driver.find_element_by_xpath("//*[@id='content']/div[4]/div/font/b").text

    age = str(a)
    height = str(h)
    weight = str(w)

    info =driver.find_element_by_xpath("//*[@id='content']/div[4]/ul/li[1]").text

    #Create file name for report
    filename = "Report"+n+s

    #Create a report
    CreateReport(n,s,age,height,weight,result,status,info,filename)



# for male
BMICalculator("Aytac","Macit",27,"m",167,64)

BMICalculator("Ertac","Macit",25,"m",168,74)



