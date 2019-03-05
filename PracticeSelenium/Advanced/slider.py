__author__ = 'Ratnesh Mallah'

from utilities.handy_wrapper import HandyWrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHover:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        self.driver.get(baseUrl)
        self.driver.switch_to.frame(0)

        element = self.driver.find_element(By.XPATH,"//div[@id='slider']//span")
        action = ActionChains(self.driver)

        action.drag_and_drop_by_offset(element,100,0).perform()
        time.sleep(3)


    def __del__(self):
        self.driver.close()


test = MouseHover()
test.test()