from .base_page import BasePage
from .locators import LoginPageLocators

from selenium.webdriver.common.by import By
import time 
from random import randrange




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        
        login_url = self.browser.current_url
        
        assert self.is_element_present(*LoginPageLocators.should_be_login_url), "login url is not presented"

    def should_be_login_form(self):
        
        assert self.is_element_present(*LoginPageLocators.should_be_login_form), "login form is not presented"

    def should_be_register_form(self):
        
        assert self.is_element_present(*LoginPageLocators.should_be_register_form), "register form is not presented"
        
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        
        password = randrange(1000000000, 10000000000)
        
        area_email = self.browser.find_element(*LoginPageLocators.should_be_email_input_in_register_form)
        area_email.send_keys(email)
        area_password_main = self.browser.find_element(*LoginPageLocators.should_be_password_first_input_in_password_form)
        area_password_main.send_keys(password)
        
        area_password_repeat = self.browser.find_element(*LoginPageLocators.should_be_password_second_input_in_password_form)
        area_password_repeat.send_keys(password)
        
        button_register = self.browser.find_element(*LoginPageLocators.should_be_button_register_account_and_login)
        button_register.click()
        
       
        
            