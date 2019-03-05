__author__ = 'Ratnesh Mallah'

from selenium.webdriver.common.by import By
import time

class HandyWrapper:

    def __init__(self,driver):
        self.driver = driver


    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css_selector':
            return By.CSS_SELECTOR
        elif locatorType == 'link_text':
            return  By.LINK_TEXT
        elif locatorType == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator type is not supported")
        return False


    def getElement(self,locator,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element found!")
        except:
            print("Element not found!")
        return element


    def isElementPresent(self,locator,byType):
        try:
            element = self.driver.find_element(byType,locator)
            if element is not None:
                return True
            else:
                return False
        except:
            return False


    def elementPresenceCheck(self,locator,byType):
        try:
            elementList = self.driver.find_elements(byType,locator)
            if len(elementList) > 0:
                return True
            else:
                return False
        except:
            return False

    def waitForElement(self,locator,locatorType='id',
                       timeout=10,poll_frequency=0.5):
        pass


    def scrollToElement(self,locator,locateBy):
        try:
            element = self.driver.find_element(locateBy,locator)
            self.driver.execute_script('arguments[0].scrollIntoView(true);',element)
            self.driver.execute_script('window.scrollBy(0,-100);')
        except:
            print("You have given wrong element details")


    def switchToWondow(self,parentHandle=None):
        if parentHandle is None:
            parentHandle = self.driver.current_window_handle
            print("first handle : ",parentHandle)

            allWindowHandles = self.driver.window_handles
            for handle in allWindowHandles:
                print("handles ",handle)
                if handle not in parentHandle:
                    self.driver.switch_to.window(handle)
                    print("window_switched_to : ",handle)
                    break
        else:
            self.driver.switch_to.window(parentHandle)
            print("window_switched_to : ",parentHandle)
        return parentHandle

    def takeScreenShot(self,driver):
        filepath = "C:\\Users\\720555\\PycharmProjects\\PracticeSelenium\\test_wait\\Screenshots\\"
        filename = str(round(time.time()*1000))+'.png'
        sf = filepath+filename
        try:
            driver.save_screenshot(sf)
            print("screenshot saved into : ",sf)
        except:
            print("file directory not found")