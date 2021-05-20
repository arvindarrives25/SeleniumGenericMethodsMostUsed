import time
from selenium import webdriver

from testmethods.test_base import TestBase


class TestTable(TestBase):
    driver: webdriver.Chrome
    """This method will select all the given table"""
    def test_static_table_all_values(self):
        self.driver.get("https://www.w3schools.com/html/html_tables.asp")
        self.driver.maximize_window()
        time.sleep(2)
        rows = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        columns = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th"))

        print("Company" + "                  " + "Contact" + "                      " + "Country")
        for r in range(2, rows + 1):
            for c in range(1, columns + 1):
                my_data = self.driver.find_element_by_xpath(
                    "//*[@id='customers']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]")
                print(my_data.text, end='                           ')
            print()

    """This method will select all the values from single column"""
    def test_static_table_single_column_values(self):
        self.driver.get("https://www.w3schools.com/html/html_tables.asp")
        self.driver.maximize_window()
        time.sleep(2)
        rows = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        # columns = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th"))
        print("Countries Names are : ")
        for r in range(2, rows + 1):
            my_data = self.driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td[3]")
            print(my_data.text)

    """This method will log into demo site and find the all the names in page 1, 2, 3
    Also it will click to navigate to the next page. This is just up to 3 pages but you can
    fetch any values from all the pages and validate"""
    def test_dynamic_table_all_values(self):
        self.driver.get("https://demo.opencart.com/admin/")
        self.driver.maximize_window()
        time.sleep(2)
        user_name = self.driver.find_element_by_xpath("//*[@id='input-username']")
        user_name.clear()
        user_name.send_keys("demo")
        password = self.driver.find_element_by_xpath("//*[@id='input-password']")
        password.clear()
        password.send_keys("demo")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[@id='menu-sale']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[@id='menu-sale']/ul/li[1]").click()
        time.sleep(2)

        rows = self.driver.find_elements_by_xpath("//*[@class='table table-bordered table-hover']/tbody/tr")
        print(len(rows))

        for x in range(2, 5):
            active_page = self.driver.find_element_by_xpath("//ul[@class='pagination']/li/span")
            print(active_page.text)
            active_page.click()
            next_page = self.driver.find_element_by_xpath("//ul[@class='pagination']/li/a[text()='"+str(x)+"']")

            time.sleep(2)

            for r in range(1, len(rows) + 1):
                names = self.driver.find_element_by_xpath(
                    "//*[@class='table table-bordered table-hover']/tbody/tr["+str(r)+"]/td[3]")
                print(names.text)
            next_page.click()
            time.sleep(2)
