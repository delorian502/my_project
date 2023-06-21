from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    should_be_login_url = (By.CSS_SELECTOR, "#login_link")
    
    should_be_login_form = (By.CSS_SELECTOR, "#login_form")
    
    should_be_register_form = (By.CSS_SELECTOR, "#register_form")     
    
class ProductPageLocators():
    should_be_button_add_product_to_basket_form = (By.CSS_SELECTOR,"#add_to_basket_form .btn")
    
    name_text_in_page = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    name_text_after_add_green_aria = (By.CSS_SELECTOR, ".alertinner strong")
    
    price_product = (By.CSS_SELECTOR,"p.price_color")
    price_in_basket = (By.CSS_SELECTOR, ".alertinner p strong" )
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")    
         
    