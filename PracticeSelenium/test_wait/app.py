__author__ = 'Ratnesh Mallah'

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.handy_wrapper import HandyWrapper

import os

class ImplicitlyWait:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        self.driver.get(baseUrl)

        btn_login = self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]")
        btn_login.click()

        username = self.driver.find_element(By.ID,"user_email")
        username.send_keys("test@gmail.com")

        password = self.driver.find_element(By.ID,"user_password")
        password.send_keys("abcabc")

        submit = self.driver.find_element(By.NAME,"commit")
        submit.click()

    def __del__(self):
        self.driver.close()



class ExplicitlyWait:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        self.driver.get(baseUrl)
        hw = HandyWrapper(self.driver)

        btn_login = self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]")
        btn_login.click()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        username = wait.until(EC.visibility_of_element_located((By.ID,"user_email")))
        hw.takeScreenShot(self.driver)
       # username = self.driver.find_element(By.ID,"user_email")
        username.send_keys("test@gmail.com")

        password = self.driver.find_element(By.ID,"user_password")
        password.send_keys("abcabc")

        submit = self.driver.find_element(By.NAME,"commit")
        submit.click()


        hw.takeScreenShot(self.driver)


    def __del__(self):
        self.driver.close()



#test = ImplicitlyWait()
test = ExplicitlyWait()
test.test()

