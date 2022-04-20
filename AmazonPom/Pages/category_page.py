import sys
sys.path.insert(0, '/home/ozan-kizilkaya/Desktop/Selenium-master')
from selenium.webdriver.common.by import By
from AmazonPom.base_page.base_page import BasePage


class CategoryPage(BasePage):
    """Select the third product from the category page"""

    NEXT_PAGE = (By.CSS_SELECTOR, "[class='a-last']")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
    IS_PAGE_TWO = (By.CSS_SELECTOR, ".a-section.a-spacing-small.a-spacing-top-small")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def next_page(self):
        """Go to the second category page"""
        self.wait_for_element(self.NEXT_PAGE).click()

    def select_third_product(self):
        """Choose the third product from the start"""
        self.wait_for_elements(self.PRODUCT_PAGE)[2].click()
