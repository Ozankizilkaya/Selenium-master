import sys

sys.path.insert(0, '/home/ozan-kizilkaya/Desktop/Selenium-master')
from selenium import webdriver
from Mediamarkt.Pages.login_page import LoginPage
from Mediamarkt.Pages.home_page import HomePage
from Mediamarkt.Pages.category_page import CategoryPage
from Mediamarkt.Pages.product_page import ProductPage
from Mediamarkt.Pages.wishlist import Wishlist
import unittest


class TestMediaMarkt(unittest.TestCase):
    """Test case is:
    1. Go to Mediamarkt
    2. Click random category
    3. Choose random product
    4. Add product to wishlist
    7. Go to wishlist
    8. Add to card prdouct on whislist
    8. Delete items from card
    9. Tear down
    """

    @classmethod
    def setUpClass(self):

        self.website = "https://mediamarkt.pl/"
        self.driver = webdriver.Chrome("/home/ozan-kizilkaya/Desktop/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.HomePage = HomePage(self.driver)
        self.CategoryPage = CategoryPage(self.driver)
        self.ProductPage = ProductPage(self.driver)
        self.Wishlist = Wishlist(self.driver)

    def test_MediaMarkt(self):

        self.HomePage.search()
        self.CategoryPage.next_page()
        self.CategoryPage.select_third_product()
        self.ProductPage.add_to_list()
        self.Wishlist.delete_wishlist()

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #unittest.main()
    deneme=TestMediaMarkt()
    deneme.setUpClass()
    deneme.test_MediaMarkt()

