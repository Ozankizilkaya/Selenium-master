import sys
sys.path.insert(0, '/home/ozan-kizilkaya/Desktop/Selenium-master')
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from AmazonPom.base_page.base_page import BasePage


class Wishlist(BasePage):
    """Delete the product in wishlist"""

    HOVER_WISHLIST = (By.ID, "nav-link-accountList-nav-line-1")
    WISHLIST_BTN = (By.CLASS_NAME, "nav-panel")
    DELETE_BTN = (By.CSS_SELECTOR, "[class='a-link-normal a-declarative g-visible-js']")
    DELETE_BTN_2 = (By.NAME, "submit.deleteItem")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".a-size-base")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def delete_wishlist(self):
        """To delete the product in wishlist and confirm that it has been deleted"""
        self.hover(self.HOVER_WISHLIST)
        self.wait_for_element(self.WISHLIST_BTN).click()
        try:
            self.wait_for_element(self.DELETE_BTN).click()
        except TimeoutException:
            self.wait_for_element(self.DELETE_BTN_2).click()
        assert self.wait_for_element(self.PRODUCT_TITLE)
