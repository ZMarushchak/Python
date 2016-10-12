import unittest
from selenium import webdriver
import os
import sys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xmlrunner

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class test(unittest.TestCase):

    def test_hello_present(self):
        while True:
            try:
                self.chrome = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                               desired_capabilities=DesiredCapabilities.CHROME)
                self.firefox = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                                desired_capabilities=DesiredCapabilities.FIREFOX)
                break
            except:
                pass
        # print "CURRENT DIR::::%s" % CURRENT_DIR
        # print "PRINTED:%s" % out
        self.firefox.get('http://app:5000')
        bodyfox = self.firefox.find_element_by_css_selector('body')
        self.chrome.get('http://app:5000')
        bodychrome = self.chrome.find_element_by_css_selector('body')
        self.assertIn('world', bodyfox.text)
        self.assertIn('world', bodychrome.text)
        time.sleep(2)

    def test_hell_present0(self):
        while True:
            try:
                self.chrome = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                               desired_capabilities=DesiredCapabilities.CHROME)
                self.firefox = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                                desired_capabilities=DesiredCapabilities.FIREFOX)
                break
            except:
                pass
                # print "CURRENT DIR::::%s" % CURRENT_DIR
                # print "PRINTED:%s" % out

        self.firefox.get('http://app:5000')
        bodyfox = self.firefox.find_element_by_css_selector('body')
        self.chrome.get('http://app:5000')
        bodychrome = self.chrome.find_element_by_css_selector('body')
        self.assertIn('world', bodyfox.text)
        self.assertIn('world', bodychrome.text)
        time.sleep(2)

    def test_helo_present1(self):
        while True:
            try:
                self.chrome = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.CHROME)
                self.firefox = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                            desired_capabilities=DesiredCapabilities.FIREFOX)
                break
            except:
                pass
            # print "CURRENT DIR::::%s" % CURRENT_DIR
            # print "PRINTED:%s" % out


        self.firefox.get('http://app:5000')
        bodyfox = self.firefox.find_element_by_css_selector('body')
        self.chrome.get('http://app:5000')
        bodychrome = self.chrome.find_element_by_css_selector('body')
        self.assertIn('world', bodyfox.text)
        self.assertIn('world', bodychrome.text)
        time.sleep(2)

    def test_hllo_present2(self):
        while True:
            try:
               self.chrome = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.CHROME)
               self.firefox = webdriver.Remote(command_executor='http://hub:4444/wd/hub',
                                            desired_capabilities=DesiredCapabilities.FIREFOX)
               break
            except:
                pass
            # print "CURRENT DIR::::%s" % CURRENT_DIR
            # print "PRINTED:%s" % out


        self.firefox.get('http://app:5000')
        bodyfox = self.firefox.find_element_by_css_selector('body')
        self.chrome.get('http://app:5000')
        bodychrome = self.chrome.find_element_by_css_selector('body')
        self.assertIn('world', bodyfox.text)
        self.assertIn('world', bodychrome.text)
        time.sleep(2)

if __name__ == '__main__':
    with open('/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)




# suite = unittest.TestLoader().loadTestsFromTestCase(test)
# runner = unittest.TextTestRunner(verbosity=2).run(suite)
# ret = not runner.wasSuccessful()
# sys.exit(ret)

