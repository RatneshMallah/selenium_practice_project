__author__ = 'Ratnesh Mallah'

from utilities.handy_wrapper import HandyWrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test(self):
        baseUrl = "https://www.expedia.com"
        hw = HandyWrapper(self.driver)
        self.driver.get(baseUrl)

        textField1 = hw.getElement('package-departing-hp-package')
        textField1.click()

        time.sleep(2)

        #textField2 = hw.getElement("package-returning-hp-package")
       # textField2.click()

        calMonth = self.driver.find_element(By.XPATH,"//*[@class='datepicker-cal-month'][position()=1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME,"button")

        for date in allValidDates:
            if date.text == '31':
                date.click()
                break

        time.sleep(5)


    def __del__(self):
        self.driver.close()


test = CalendarSelection()
test.test()