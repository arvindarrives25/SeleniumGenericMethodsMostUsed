import time
from selenium import webdriver
from testmethods.test_base import TestBase


class TestCarousel(TestBase):
    driver: webdriver.Chrome
    url1 = "https://www.noon.com/uae-en/"
    locator1 = "//*[@class='sc-eGCarw jqTxQZ']/div[2]"
    locator2 = "//*[@data-qa='product-name']/div"
    attribute = "class"
    break_text = "swiper-button-disabled"

    """This method will go to carousel section, click till the end fetch all the visible 
    Title of the items, we can make generic method or alter it according to our use
    This is just an example"""
    def test_carousel_example(self):
        self.driver.get(self.url1)
        self.driver.maximize_window()
        time.sleep(2)
        while True:
            elm = self.driver.find_element_by_xpath(self.locator1)
            prices = self.driver.find_elements_by_xpath(self.locator2)
            for price in prices:
                print(price.text)
            elm.click()
            time.sleep(2)
            if self.break_text in elm.get_attribute(self.attribute):
                break
            time.sleep(2)
