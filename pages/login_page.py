from .base_page import BasePage
from .locators import LoginPageLocators
from mimesis import Person
import time


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"

    def __init__(self, browser, url=LOGIN_PAGE_URL):
        super().__init__(browser, url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Current URL is not correct. It does not contain the handle " \
                                                    "'login'. "

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form does not exist."

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form does not exist."

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()
