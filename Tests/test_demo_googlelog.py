import time
import logging
import Logging.CustomLoggerUtil as Cl
from Logging.AdvCustomLog import Log
#import selenium
#from selenium import webdriver

class TestGoolgeLog:
    logObj = Cl.customLogger()
    def testLogging(self):
        self.logObj.info("Hello I am Info")
        self.logObj.error("Hello I am Error")
        Log.write_error_to_log(self, "Hello I am Advanced Log error")
        Log.write_info_to_log(self, "Hello I am Advanced Log Info")


classobject = TestGoolgeLog()
classobject.testLogging()










