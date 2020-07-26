from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DressesPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.casual_dresses = (By.XPATH, '//*[@id="subcategories"]/ul/li[1]/div[1]/a/img')
        self.order = (By.ID, 'selectProductSort')
        self.list_view = (By.CLASS_NAME, 'icon-th-list')
        self.add_printed_orange_dress = (By.XPATH, '//*[@data-id-product="3"]')  #Lo hice yo (puede estar muy mal)

    def subcategories_dresses(self):
        self.driver.find_element(*self.casual_dresses).click()

    def select_by_value(self, value):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_value(value)

    def view_list(self):
        self.driver.find_element(*self.list_view).click()

    def add_printed_orange_dress_to_cart(self):
        self.driver.find_elements(*self.add_printed_orange_dress)[0].click()