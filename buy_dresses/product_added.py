from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductAdded:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_added = (By.ID, 'layer_cart_product_quantity')
        self.price_products = (By.CLASS_NAME, 'ajax_block_products_total')
        self.shipping_price = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[2]/span')
        self.total_price = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[3]/span')
        self.product_name = (By.ID, 'layer_cart_product_title')

    def return_quantity_added(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.quantity_added)).text

    def return_price_products(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.price_products)).text

    def return_shipping_price(self):
        return self.driver.find_element(*self.shipping_price).text

    def return_total_price(self):
        return self.driver.find_element(*self.total_price).text

    def return_product_name(self):
        return self.driver.find_element(*self.product_name).text

