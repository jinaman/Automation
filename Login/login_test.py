from selenium import webdriver
import unittest
from principal_page import PaginaPrincipal
from authen_page import AuthenPage
from selenium.webdriver.chrome.options import Options


class LoginCases(unittest.TestCase):
    """Exercise test login"""
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('start-maximized')
        self.driver = webdriver.Chrome('Chromedriver.exe', options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.principal_page = PaginaPrincipal(self.driver)
        self.authentication_page = AuthenPage(self.driver)

    def test_login_caso_1(self):
        self.principal_page.login()
        self.authentication_page.input_email('namanjuanignacio@gmail')
        self.authentication_page.input_password('lalala')
        self.authentication_page.sign_in()
        self.assertEqual(self.authentication_page.return_invalid_email_text(), 'Invalid email address.')

    def test_login_caso_2(self):  #hey
        self.principal_page.login()
        self.authentication_page.input_email('namanjuanignacio@gmail.com')
        self.authentication_page.input_password('lalala')
        self.authentication_page.sign_in()
        self.assertTrue(self.authentication_page.return_authentication_failed_text() == 'Authentication failed.')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()