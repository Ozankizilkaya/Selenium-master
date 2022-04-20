import sys
sys.path.insert(0, '/home/ozan-kizilkaya/Desktop/Selenium-master')
from selenium.webdriver.common.by import By
from Mediamarkt.base_page.base_page import BasePage

from selenium import webdriver
class HomePage(BasePage):
    """Search from the search button"""

    HOMEPAGE_CONTROL = (By.ID, "13808184")
    MENU_CONTROL=(By.CLASS_NAME, "menu-main-list")
    MENU_SELECTOR=(By.CSS_SELECTOR,"data-v-5604dec2")
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def search(self):
        """Search for word samsung"""
        assert self.wait_for_element(self.HOMEPAGE_CONTROL), True
        #self.wait_for_element(self.PRODUCT_CONTROL).click()
        self.wait_for_elements(self.MENU_SELECTOR).click()
