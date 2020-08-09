from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DressesPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.casual_dresses = (By.LINK_TEXT, 'Casual Dresses')
        self.order = (By.ID, 'selectProductSort')
        self.list_view = (By.ID, 'list')
        self.add_printed_orange_dress = (By.XPATH, '//*[@data-id-product="3"]')

    def subcategories_casual_dresses(self):
        self.driver.find_element(*self.casual_dresses).click()

    def view_list(self):
        self.driver.find_element(*self.list_view).click()

    def add_printed_orange_dress_to_cart(self):
        self.driver.find_element(*self.add_printed_orange_dress).click()