import time
from selenium import webdriver

from testmethods.test_base import TestBase


class TestCheckBoxes(TestBase):
    driver: webdriver.Chrome
    """This method will select all the given checkboxes"""
    def test_checkbox_select_all(self):
        self.driver.get("https://itera-qa.azurewebsites.net/home/automation")
        self.driver.maximize_window()
        time.sleep(2)
        checkboxes = self.driver.find_elements_by_xpath("//*[@type='checkbox' and contains(@id, 'day')]")
        for checkbox in checkboxes:
            checkbox.click()
        time.sleep(5)

    """This method will select last 2 checkboxes and it can be customised according to our requirement"""
    def test_checkbox_last_two(self):
        self.driver.get("https://itera-qa.azurewebsites.net/home/automation")
        self.driver.maximize_window()
        time.sleep(2)
        checkboxes = self.driver.find_elements_by_xpath("//*[@type='checkbox' and contains(@id, 'day')]")
        for checkbox in checkboxes:
            if checkbox == checkboxes[-1] or checkbox == checkboxes[-2]:
                checkbox.click()
        time.sleep(5)

