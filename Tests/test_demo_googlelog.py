import time
import logging
import Logging.CustomLoggerUtil as Cl
#import selenium
#from selenium import webdriver

class TestGoolgeLog:
    logObj = Cl.customLogger()
    def testLogging(self):
        self.logObj.info("Hello I am Info")
        self.logObj.error("Hello I am Error")



classobject = TestGoolgeLog()
classobject.testLogging()










