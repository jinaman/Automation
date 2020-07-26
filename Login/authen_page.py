from selenium.webdriver.common.by import By


class AuthenPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.email_box = (By.ID, 'email')
        self.password_box = (By.ID, 'passwd')
        self.sign_in_button = (By.XPATH, '//*[@id="SubmitLogin"]/span/i')
        self.alert_invalid_email = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')
        self.alert_authentication_failed = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')

    def input_email(self, email):
        self.driver.find_element(*self.email_box).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(*self.password_box).send_keys(password)

    def sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()

    def return_invalid_email_text(self):
        return self.driver.find_element(*self.alert_invalid_email).text

    def return_authentication_failed_text(self):
        return self.driver.find_element(*self.alert_authentication_failed).text