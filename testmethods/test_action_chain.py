import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from testmethods.test_base import TestBase
from selenium import webdriver


class TestActionChain(TestBase):
    driver: webdriver.Chrome
    log = TestBase.get_logger()

    """This is generic  mouse hover method, which will hover mouse
    pointer over webElement and stays there"""
    def generic_method_mouse_hover(self, ele1):
        act = ActionChains(self.driver)
        act.move_to_element(ele1).perform()

    """This is generic  mouse right click over an element"""
    def generic_method_right_click(self, ele):
        act = ActionChains(self.driver)
        act.context_click(ele).perform()

    """This is generic method for drag and drop"""
    def drag_and_drop(self, source, target):
        act = ActionChains(self.driver)
        act.drag_and_drop(source, target).perform()

    """This method will fetch all the texts from a list and finally put
    them into other list"""
    @staticmethod
    def create_list_of_texts(ele):
        list1 = []
        for x in ele:
            list1.append(x.text)
        return list1

    """This test case will hover over main menu, submenu1 will visible,
    After that mouse pointer will move & hover over submenu1, submenu2 will visible
    and finally will click submenu2 and verify"""
    def test_navigation_bar_multi_level(self):
        self.log.info("launching spice jet website")
        self.driver.get("https://www.spicejet.com/")
        self.log.info("Maximizing windows")
        self.driver.maximize_window()
        time.sleep(2)
        main_menu = self.driver.find_element(By.ID, "ctl00_HyperLinkLogin")
        sub_menu1 = self.driver.find_element(By.XPATH, "//*[text()='SpiceClub Members']")
        sub_menu2 = self.driver.find_element(By.XPATH, "(//a[text()='Member Login'])[2]")
        self.generic_method_mouse_hover(main_menu)
        self.log.info("Hovering over LOGIN/SIGNUP")
        time.sleep(2)
        self.generic_method_mouse_hover(sub_menu1)
        self.log.info("Hovering over SpiceClub Members")
        time.sleep(2)
        sub_menu2.click()
        self.log.info("Clicking Member Login")
        time.sleep(2)
        actual_url = self.driver.current_url
        expected_url = "https://book.spicejet.com/Login.aspx"
        self.log.info("Comparing expected url with actual url")
        if actual_url == expected_url:
            self.log.info("Expected url equals to actual url, hence Test Case Passed")
            assert True
        else:
            self.log.error("Expected url not equals to actual url, hence Test case Failed")
            assert False

    def test_right_click_and_fetch_text(self):
        self.log.info("launching jquery site")
        self.driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        self.log.info("Maximizing windows")
        self.driver.maximize_window()
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, "//span[text()='right click me']")
        self.log.info("Right click on the web element ")
        self.generic_method_right_click(ele)
        time.sleep(2)
        my_items = self.driver.find_elements(By.XPATH, "/html/body/ul/li/span")
        expected_items = ["Edit", "Cut", "Copy", "Paste", "Delete", "Quit"]
        actual_items = TestActionChain.create_list_of_texts(my_items)
        self.log.info("Comparing expecting  with actual list texts")
        if actual_items == expected_items:
            self.log.info("Expected list equals to actual list, hence Test Case Passed")
            assert True
        else:
            self.log.info("Expected list not equals to actual list, hence Test Case Failed")
            assert False

    def test_drag_drop(self):
        self.log.info("launching jquery site")
        self.driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
        self.log.info("Maximizing windows")
        self.driver.maximize_window()
        time.sleep(2)
        source1 = self.driver.find_element(By.ID, "draggable")
        target1 = self.driver.find_element(By.ID, "droppable")
        self.log.info("Calling method drag_and_drop(), to perform drag and drop")
        self.drag_and_drop(source1, target1)
        time.sleep(2)
















