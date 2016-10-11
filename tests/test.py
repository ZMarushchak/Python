import unittest
from selenium import webdriver
import os
import sys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class test(unittest.TestCase):

    def test(self):
        while True:
            try:
                self.chrome = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)
                self.firefox = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.FIREFOX)
                break
            except:
                pass
        #print "CURRENT DIR::::%s" % CURRENT_DIR
        # print "PRINTED:%s" % out
        self.firefox.get('http://app:5000')
        body = self.firefox.find_element_by_css_selector('body')
        return self.assertIn('hello', body.text)

suite = unittest.TestLoader().loadTestsFromTestCase(test)
runner = unittest.TextTestRunner(verbosity=2).run(suite)
ret = not runner.wasSuccessful()
sys.exit(ret)

