from .base_page import BasePage
from .locators import LoginPageLocators

from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        
        assert self.is_element_present(*LoginPageLocators.should_be_login_url), "login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.should_be_login_form), "login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.should_be_register_form), "register form is not presented"