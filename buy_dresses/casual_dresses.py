from selenium.webdriver.common.by import By


class CasualDresses:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.dress = (By.LINK_TEXT, 'Printed Dress')

    def click_dress(self):
        self.driver.find_element(*self.dress).click()