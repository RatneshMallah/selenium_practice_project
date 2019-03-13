__author__ = 'Ratnesh Mallah'

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as cl



class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)

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
            self.log.info("Locator type "+locatorType+" not correct/suported")
        return False


    def getElement(self,locator,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element found with locator "+locator+" and LocatorType "+locatorType)
        except:
            self.log.error("Element not found with locator "+locator+" and LocatorType "+locatorType)
        return element


    def isElementPresent(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element is present with locator "+locator+" and locatorType "+locatorType)
                return True
            else:
                self.log.error("Element is not present with locator "+locator+" and locatorType "+locatorType)
                return False
        except:
            self.log.error("Element is not present with locator "+locator+" and locatorType "+locatorType)
            return False


    def elementPresenceCheck(self,locator,byType):
        try:
            elementList = self.driver.find_elements(byType,locator)
            if len(elementList) > 0:
                self.log.info("elements are present with locator "+locator+" and locatorType "+byType)
                return True
            else:
                self.log.error("elements are not present with locator "+locator," and locatorType "+byType)
                return False
        except:
            return False


    def elementClick(self,locator, locatortype="id"):
         try:
            element = self.getElement(locator,locatortype)
            element.click()
            self.log.info("sent data on element with locator: "+locator+" locatorType : "+locatortype)
         except:
            self.log.error("Cannot send data into the element with locator: "+locator+" locatorType : "+locatortype)



    def sendKeys(self,data,locator, locatortype="id"):
         try:
            element = self.getElement(locator,locatortype)
            element.clear()
            element.send_keys(data)
            self.log.info("keys sent to element with locator: "+locator+" locatorType : "+locatortype)
         except:
             self.log.error("Cannot send keys to the element with locator: "+locator+" locatorType : "+locatortype)



    def waitForElement(self,locator,locatorType='id',
                       timeout=10,poll_frequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver,10,poll_frequency=.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,"stopFilter_stop-0")))
            self.log.info("waiting for element "+element)
        except:
            self.log.error(element+" Not found ")

        return element


    def scrollToElement(self,locator,locateBy):
        try:
            element = self.driver.find_element(locateBy,locator)
            self.driver.execute_script('arguments[0].scrollIntoView(true);',element)
            self.driver.execute_script('window.scrollBy(0,-100);')
            self.log.info("scrolled page to "+element)
        except:
            self.log.error("You have given wrong element details for scrolling")


    def switchToWondow(self,parentHandle=None):
        if parentHandle is None:
            parentHandle = self.driver.current_window_handle
            self.log.info("first handle : "+parentHandle)

            allWindowHandles = self.driver.window_handles
            for handle in allWindowHandles:
                print("handles ",handle)
                if handle not in parentHandle:
                    self.driver.switch_to.window(handle)
                    self.log.info("window_switched_to : "+handle)
                    break
        else:
            self.driver.switch_to.window(parentHandle)
            self.log.info("window_switched_to : "+parentHandle)
        return parentHandle




    def takeScreenShot(self,driver):
        filepath = "C:\\Users\\720555\\PycharmProjects\\PracticeSelenium\\test_wait\\Screenshots\\"
        filename = str(round(time.time()*1000))+'.png'
        sf = filepath+filename
        try:
            driver.save_screenshot(sf)
            self.log.info("screenshot saved into : "+sf)
        except:
            self.log.error("file directory not found")