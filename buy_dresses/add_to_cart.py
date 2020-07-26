from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddToCart:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_box = (By.ID, 'quantity_wanted')
        self.size_select = (By.ID, 'group_1')
        self.add_to_cart_button = (By.XPATH, '//*[@id="add_to_cart"]/button')

    def enter_quantity(self, quantity):
        self.driver.find_element(*self.quantity_box).clear()
        self.driver.find_element(*self.quantity_box).send_keys(quantity)

    def enter_size(self, size):
        Select(self.driver.find_element(*self.size_select)).select_by_value(size)

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()