from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *

class BasketPage(BasePage):
    
    
    
    def zero_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS), "should be zero products in basket"
        
    def message_about_basket_empty(self):
        text =  self.browser.find_element(*BasketPageLocators.ZERO_PRODUCTS)
        
        
        assert text , "should be message about zero products in basket"
    



