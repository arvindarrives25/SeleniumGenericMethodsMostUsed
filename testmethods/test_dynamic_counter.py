import time
from selenium import webdriver
from testmethods.test_base import TestBase


class TestDynamicCounter(TestBase):
    log = TestBase.get_logger()
    driver: webdriver.Chrome
    url1 = "https://www.worldometers.info/world-population/"
    current_population = "//*[@id='maincounter-wrap']/div/span"
    today_and_year_population = "//*[@class='col-sm-6 col-counters']/div/parent::div//span[@class='rts-counter']"

    """This method will got to the world population meter site and fetch the dynamic data of Today's and This year's
    Birth, Death and Growth data, I have used a while loop which will be True until 20 seconds and break"""

    def test_dynamic_counter(self):
        self.driver.get(self.url1)
        self.driver.maximize_window()
        time.sleep(2)
        timeout = 20  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            current_pop = self.driver.find_element_by_xpath(self.current_population)
            print("Current Population: ")
            print(current_pop.text)
            today_and_year_pop = self.driver.find_elements_by_xpath(self.today_and_year_population)
            print("Today's and This year Birth, Death and Growth")
            for pop in today_and_year_pop:
                print(pop.text)
                time.sleep(2)
            test = 0
            if test == 5:
                break
            test -= 1
            time.sleep(2)
