__author__ = 'Ratnesh Mallah'

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _passwd_field = "user_password"
    _login_button = "commit"

    # def getLoginLink(self):
    #    return self.self.driver.find_element(By.LINK_TEXT,self._login_link)
    #
    # def getEmailField(self):
    #    return self.driver.find_element(By.ID,self._email_field)
    #
    # def getPasswdField(self):
    #    return self.driver.find_element(By.ID,self._passwd_field)
    #
    # def getLoginButton(self):
    #    return self.driver.find_element(By.NAME,self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatortype="link_text")

    def enterEmail(self,username):
        self.sendKeys(username,self._email_field,locatortype="id")

    def enterPasswd(self,passwd):
        self.sendKeys(passwd,self._passwd_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatortype="name")

    def login(self,username="",password=""):

        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPasswd(password)
        self.clickLoginButton()

    def verifuLoginSuccessfully(self):
        result = self.isElementPresent("//span[text()='Test User']",locatorType="xpath")
        return result

    def verifyInvalidLogin(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",locatorType="xpath")
        return result