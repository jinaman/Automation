from selenium.webdriver.common.by import By


class CasualDresses:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.dress = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')

    def click_dress(self):
        self.driver.find_element(*self.dress).click()