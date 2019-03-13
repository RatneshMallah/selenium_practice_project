__author__ = 'Ratnesh Mallah'

from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTest(unittest.TestCase):

    baseUrl = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome(executable_path="../../driver/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseUrl)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com","abcabc")
        result = self.lp.verifuLoginSuccessfully()
        assert result == True

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lp.login("testfail@email.com","abcabc")
        result = self.lp.verifyInvalidLogin()
        assert result == True

    def __del__(self):
        self.driver.close()
