__author__ = 'Ratnesh Mallah'

from selenium import webdriver
from utilities.handy_wrapper import HandyWrapper
from selenium.webdriver.common.by import By
import time

class MainWrapper:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        hw = HandyWrapper(self.driver)
        self.driver.get(baseUrl)

        textField1 = hw.getElement('name')
        textField1.send_keys("Test")

        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']",locatorType='xpath')
        textField2.clear()

        print("<-------------- Element Presence Checking --------------->")

        e1 = hw.isElementPresent("name",By.ID)
        print("Element present : ",e1)
        e2 = hw.elementPresenceCheck("//input[@id='name']",By.XPATH)
        print("Element present : ",e2)
        hw.scrollToElement("mousehover",By.ID)
        e3 = hw.isElementPresent("mousehover",By.ID)
       # e3.click()
        #print("Element present : ",e3)


        print("<-------------- Switch Window --------------->")

        hw.scrollToElement("openwindow",By.ID)

        openNewWindow = hw.getElement("openwindow")
        openNewWindow.click()
        print("Element Clicked")

        ph = hw.switchToWondow()
        time.sleep(1)
        searchInNewWindow = hw.getElement("query","name")
        searchInNewWindow.send_keys("python")
        self.driver.close()
        hw.switchToWondow(ph)
        name = hw.getElement("name")
        name.send_keys("Test completed")
        time.sleep(2)

        print("<-------------- Switch Frame --------------->")

        #Switch to frame using id
        #self.driver.switch_to.frame("courses-iframe")

        #switch to frame using name
        #self.driver.switch_to.frame("iframe-name")

        #switch to frame using number
        self.driver.switch_to.frame(0)

        searchCourses = hw.getElement("search-courses")
        searchCourses.send_keys("python")
        time.sleep(2)

        #Switch back to the parent frame
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollBy(0,-1000)")
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys("Test Successfull")
        time.sleep(2)


        print("<-------------- Handaling Javascript Popup --------------->")

        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys("Ratnesh")
        self.driver.find_element(By.ID,"alertbtn").click()

        alrt1 = self.driver.switch_to.alert
        alrt1.accept()
        time.sleep(2)
        hw.getElement("confirmbtn").click()
        alrt_2 = self.driver.switch_to.alert
        alrt_2.dismiss()

        time.sleep(2)



    def __del__(self):
        self.driver.close()





test = MainWrapper()
test.test()