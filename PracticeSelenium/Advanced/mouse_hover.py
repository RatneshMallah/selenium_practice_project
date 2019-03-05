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
        baseUrl = "https://learn.letskodeit.com/p/practice"
        self.driver.get(baseUrl)

        hoverBtn = self.driver.find_element_by_id("mousehover")
        self.driver.execute_script("arguments[0].scrollIntoView(true);",hoverBtn)
        self.driver.execute_script("window.scrollBy(0,-100);")
        time.sleep(2)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(hoverBtn).perform()
            print("moved on hover element")

            topBtn = self.driver.find_element(By.XPATH,"//div[@class='mouse-hover-content']//a[text()='Top']")
            #topBtn.click()
            #we can do other thing also
            time.sleep(2)
            action.move_to_element(topBtn).click().perform()

        except:
            print("Faild to click inside hover btn element")



    def __del__(self):
        self.driver.close()


test = MouseHover()
test.test()