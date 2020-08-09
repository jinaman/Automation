from selenium.webdriver.common.by import By


class PaginaPrincipal:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.login_button = (By.LINK_TEXT, 'Sign in')

    def login(self):
        self.driver.find_element(*self.login_button).click()