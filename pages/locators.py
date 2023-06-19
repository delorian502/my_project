from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    should_be_login_url = (By.CSS_SELECTOR, "#login_link")
    
    should_be_login_form = (By.CSS_SELECTOR, "#login_form")
    
    should_be_register_form = (By.CSS_SELECTOR, "#register_form")      
    