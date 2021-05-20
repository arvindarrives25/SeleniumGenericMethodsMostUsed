import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from testmethods.test_base import TestBase


class TestJQueryDropDown(TestBase):
    driver: webdriver.Chrome
    url1 = "https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/"
    click_dropdown = "//*[@id='justAnInputBox']"
    lst_drop_down = "//*[@class='comboTreeItemTitle']"

    """This is generic JQuery drop down selection method
    This method will select either all values or single or multiple values """
    @staticmethod
    def generic_drop_down_selection_method(dropdown_list, values):
        if values[0] == "All":
            try:
                for dp in dropdown_list:
                    dp.click()
            except ElementNotInteractableException as e:
                print(e)
        else:
            for val in range(len(values)):
                for dp in dropdown_list:
                    print(dp.text)
                    if dp.text == values[val]:
                        dp.click()
                        break

    """This test case will select either single, multiple or all values from dropdown"""
    def test_jquery_drop_down(self):
        self.driver.get(self.url1)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.click_dropdown).click()
        time.sleep(2)
        dropdown_list = self.driver.find_elements_by_xpath(self.lst_drop_down)
        values = ["choice 7", "choice 6 2 1"]
        TestJQueryDropDown.generic_drop_down_selection_method(dropdown_list, values)
        time.sleep(1)
