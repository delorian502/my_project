from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_button_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.should_be_button_add_product_to_basket_form), 'button element is not present'
        
    def should_add_product_to_basket(self):
        self.element_click(*ProductPageLocators.should_be_button_add_product_to_basket_form), "button element don't click"
        
        
    def should_alert_be_and_calculate(self):
        self.solve_quiz_and_get_code()
        
    def check_add_name_product(self):
        
        t1 = self.browser.find_element(*ProductPageLocators.name_text_in_page).text
        t2 = self.browser.find_element(*ProductPageLocators.name_text_after_add_green_aria).text
        
        assert t2 in t1 , f"text {t1} and {t2} don't equals"
        
    def compare_prise_product_and_prise_in_basket(self):
        prise_in_page_product = self.browser.find_element(*ProductPageLocators.price_product)     
        prise_in_basket = self.browser.find_element(*ProductPageLocators.price_in_basket)    
        assert prise_in_page_product in prise_in_basket , f"prise product {prise_in_page_product} and prise in basket {prise_in_basket} don't equal"
              
        
    