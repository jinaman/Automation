from selenium import webdriver
import unittest
from main_page import MainPage
from dresses_page import DressesPage
from casual_dresses import CasualDresses
from add_to_cart import AddToCart
from product_added import ProductAdded
from selenium.webdriver.chrome.options import Options
import xmlrunner


class BuyCases(unittest.TestCase):
    """Just an excercise to learn.."""
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.pageMain = MainPage(self.driver)
        self.pageDresses = DressesPage(self.driver)
        self.dressesCasual = CasualDresses(self.driver)
        self.add_to_cart = AddToCart(self.driver)
        self.added_product = ProductAdded(self.driver)

    #@unittest.skip('no quiero que corra el test1')
    def test_caso_1(self):
        self.pageMain.click_dresses()
        self.pageDresses.subcategories_casual_dresses()
        self.dressesCasual.click_dress()
        self.add_to_cart.enter_quantity('5')
        self.add_to_cart.enter_size('L')
        self.add_to_cart.click_add_to_cart()
        self.assertEqual(self.added_product.return_quantity_added(), '5')
        self.driver.get_screenshot_as_file('addtocart_screenshot.png')
        print('El precio de los producto es: '+self.added_product.return_price_products())
        print('El costo del envío es de: '+self.added_product.return_shipping_price())
        print('El precio total es de: '+self.added_product.return_total_price())
        print('El producto que usted desea comprar se denomina: '+self.added_product.return_product_name())
        print('fin caso 1')

    #@unittest.skip('no quiero que corra el test2')
    def test_casp_2(self):
        self.pageMain.click_dresses()
        self.pageDresses.view_list()
        self.pageDresses.add_printed_orange_dress_to_cart()
        print('El precio de los producto es: '+self.added_product.return_price_products())
        print('El costo del envío es de: '+self.added_product.return_shipping_price())
        print('El precio total es de: '+self.added_product.return_total_price())
        print('El producto que usted desea comprar se denomina: '+self.added_product.return_product_name())
        print('fin caso 2')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output == 'output'),
        failfast=False, buffer=False, catchbreak=False)