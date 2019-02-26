import unittest
import constants
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/mb_ro/addToPath/chromedriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(constants.URL)
        time.sleep(5)
        user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, constants.USERNAME))
    )
        # self.assertIn("Python", driver.title)
        # user = driver.find_element_by_id(constants.USERNAME)
        # user = driver.find_element_by_xpath()
        user.send_keys("SYSTEMI")
        # user.send_keys(Keys.TAB)
        password_holder = driver.find_element_by_xpath(constants.PASSWORD_HOLDER)
        password_holder.send_keys(constants.PASSWORD)
        # user.click()
        # time.sleep(3)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        password_holder.send_keys(Keys.RETURN)
        time.sleep(5)
        # assert "No results found." not in driver.page_source
        # wait = WebDriverWait(driver, 10)


    def tearDown(self):
        # wait = WebDriverWait(driver, 10)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()