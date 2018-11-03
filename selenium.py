from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import urllib2
import csv
import time
import sys
import re

#driver=webdriver.Chrome("c:/python27/chromedriver.exe")
driver=webdriver.Firefox()
driver.switch_to_frame("entry.jsp") 
#driver.get("https://www.comptia.org/")
driver.get("http://125.221.35.78:8080/selfservice/")

def myFunction():

    driver.implicitly_wait(50)
    time.sleep(3)

    loginPath="//input[@id='TopNavigation_TopNavigation_LoginBox_txtUsername']"
    login=driver.find_element_by_xpath(loginPath)
    login.send_keys("dina@saasmax.com")

    PasswordPath="//input[@id='TopNavigation_TopNavigation_LoginBox_txtPassword']"
    Password=driver.find_element_by_xpath(PasswordPath)
    Password.send_keys("matrix7!")
    
    SubmitPath="//div[@class='form-field form-submit']/input[@value='Submit']"
    Submit=driver.find_element_by_xpath(SubmitPath).click()
    
    driver.implicitly_wait(50)
    time.sleep(3)

    driver.get("https://www.comptia.org/insight-tools/individual-directory/")
    driver.implicitly_wait(50)
    time.sleep(3)

    SearchPath="//span[@class='rsbIcon rsbIconSearch']"
    Search=driver.find_element_by_xpath(SearchPath).click()

    driver.implicitly_wait(50)
    time.sleep(3)

    PagesPath="//li[@class='current-page']"
    Pages=driver.find_element_by_xpath(PagesPath).text
    #print Pages

    nroftimes= (int(Pages[5:len(Pages)]))
    #print nroftimes

    TotalItemsPath="//p[@class='tableresult']/span"
    TotalItems = driver.find_element_by_xpath(TotalItemsPath).text
    #print TotalItems

    possibleItems = nroftimes*30
    #print possibleItems

    lastPageExtra = possibleItems-int(TotalItems)

    #paths = 'ctl00_LeftColumn_C001_RadGrid1_ctl00__0'
    f = open("output3.txt", "w")
    for j in range(nroftimes):
        iterations = 0
        if j == nroftimes:
            for i in range(30-lastPageExtra):
                PagesPath="//tr[@id='ctl00_LeftColumn_C001_RadGrid1_ctl00__" +str(iterations) + "']/td[2]/a"
                Pages = driver.find_element_by_xpath(PagesPath)
                url = Pages.get_attribute("href")
                iterations = iterations + 1
                print url
                #url = url.text
                f.writelines(url + "\n")
        else:
            for i in range(30):
                PagesPath="//tr[@id='ctl00_LeftColumn_C001_RadGrid1_ctl00__" +str(iterations) + "']/td[2]/a"
                Pages = driver.find_element_by_xpath(PagesPath)
                url = Pages.get_attribute("href")
                iterations = iterations + 1
                print url
                #url = url.text

                f.writelines(url + "\n")
        if j >= nroftimes:
            print "exitor"

        else:
            NextPagePath="//li[@class='next-page']/a"
            NextPage=driver.find_element_by_xpath(NextPagePath).click()
            driver.implicitly_wait(50)
            time.sleep(3)
    

myFunction()
    
