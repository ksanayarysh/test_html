"""Functions for working with login page"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from test_html.selenium.models.page import BasePage
from test_html.selenium.models.locator import BaseLocators, LoginPageLocators


class LoginPage(BasePage):
    """Class for Login Page"""

    def user_name(self):
        """Getting user name web element"""
        return self.driver.find_element(*LoginPageLocators.USERNAME)

    def password(self):
        """Getting password  web element"""
        return self.driver.find_element(*LoginPageLocators.PASSWORD)

    def login_button(self):
        """Getting login button name web element"""
        return self.driver.find_element(*BaseLocators.PRIMARY_BUTTON)

    def set_username(self, username):
        """setting username"""
        try:
            self._clear_element_(self.user_name())
            self.user_name().send_keys(username)
        except NoSuchElementException:
            print("No user name")

    def set_password(self, password):
        """setting password"""
        try:
            self._clear_element_(self.password())
            self.password().send_keys(password)
        except NoSuchElementException:
            print("No password")

    def login(self):
        """press "log in" button"""
        try:
            self.login_button().click()
            WebDriverWait(self.driver, 10).until(EC.title_is, "Dashboard")
        except NoSuchElementException:
            print("Can't log in")
