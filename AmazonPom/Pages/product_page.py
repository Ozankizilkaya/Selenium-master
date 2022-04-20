import sys
sys.path.insert(0, '/home/ozan-kizilkaya/Desktop/Selenium-master')
from selenium.webdriver.common.by import By
from AmazonPom.base_page.base_page import BasePage


class ProductPage(BasePage):
    """ Add to wishlist """

    ADD_TO_LIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    CLOSE_BTN = (By.CSS_SELECTOR, ".a-button-close.a-declarative")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def add_to_list(self):
        """To close the page that appears after pressing the wishlist button """
        self.wait_for_element(self.ADD_TO_LIST_BTN).click()
        self.wait_for_element(self.CLOSE_BTN).click()
