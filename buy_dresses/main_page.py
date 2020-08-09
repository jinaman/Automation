from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.dresses_link = (By.XPATH, '//*[@title="Dresses"]')

    def click_dresses(self):
        self.driver.find_elements(*self.dresses_link)[1].click()
