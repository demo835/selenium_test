import unittest
import constants
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/mb_ro/addToPath/chromedriver')

    def test_search_in_python_org(self):
        # grab username and password from environment variables
        username = os.environ['USERNAME']
        password = os.environ['PASSWORD']

        driver = self.driver
        driver.get(constants.URL)
        time.sleep(5)
        user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, constants.USERNAME_HOLDER))
        )
        # self.assertIn("Python", driver.title)
        # user = driver.find_element_by_id(constants.USERNAME)
        # user = driver.find_element_by_xpath()
        user.send_keys(username)
        # user.send_keys(Keys.TAB)
        password_holder = driver.find_element_by_xpath(constants.PASSWORD_HOLDER)
        password_holder.send_keys(password)
        # user.click()
        # time.sleep(3)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        password_holder.send_keys(Keys.RETURN)
        time.sleep(5)
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()