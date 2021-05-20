import time
from selenium import webdriver
from testmethods.test_base import TestBase


class TestDatePicker(TestBase):
    driver: webdriver.Chrome

    """This method will select a specific date"""
    def test_date_picker_first_example(self):
        self.driver.get("https://www.redbus.in/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='onward_cal']").click()
        time.sleep(2)

        while True:
            month = self.driver.find_element_by_xpath("//*[@class='monthTitle']").text
            mon = month.split(" ")[0]
            yr = month.split(" ")[1]
            if mon == "Aug" and yr == "2021":
                break
            else:
                self.driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[3]").click()
                time.sleep(2)

        days = len(self.driver.find_elements_by_xpath("//*[@class ='rb-monthTable first last']/tbody/tr"))

        for day in range(3, days):
            act_day = self.driver.find_element_by_xpath(
                "//*[@id='rb-calendar_onward_cal']/table/tbody/tr[5]/td[" + str(day) + "]")
            if act_day.text == "15":
                act_day.click()
                break
        time.sleep(2)

    """This method will select a specific date, we can also take date from user and pass in to the function"""
    def test_date_picker_second_example(self):
        self.driver.get("https://www.goibibo.com/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='departureCalendar']").click()
        time.sleep(2)

        while True:
            self.driver.find_element_by_xpath("//*[@aria-label='Next Month']").click()
            time.sleep(2)
            month = self.driver.find_element_by_xpath("//*[@class='DayPicker-Caption']/div").text
            print(month.split(" "))
            mon = month.split(" ")[0]
            yr = month.split(" ")[1]
            if mon == "August" and yr == "2021":
                break
        days = self.driver.find_elements_by_xpath("//*[@class='calDate']")
        for day in days:
            if day.text == "15":
                day.click()
                break
        time.sleep(2)



