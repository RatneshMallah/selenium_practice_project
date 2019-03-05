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
        baseUrl = "https://jqueryui.com/droppable/"
        self.driver.get(baseUrl)
        time.sleep(1)
        self.driver.switch_to.frame(0)
        time.sleep(1)
        draggable = self.driver.find_element_by_id("draggable")
        droppable = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        time.sleep(1)
        #oneway
        #action.drag_and_drop(draggable,draggable).perform()

        #secondway
        action.click_and_hold(draggable).move_to_element(droppable).release().perform()

        time.sleep(3)



    def __del__(self):
        self.driver.close()


test = MouseHover()
test.test()