from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser,link)
    page.open()
    time.sleep(5)
    page.go_to_login_page()
    time.sleep(5)
    
    login_page = LoginPage(browser,browser.current_url)
    time.sleep(5)
    
    login_page.should_be_login_page()
    
    
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser,link)
    page.open()
    
    page.go_to_basket_page()
    time.sleep(5)
    
    
    page = BasketPage(browser,browser.current_url)
    page.zero_products_in_basket()
    page.message_about_basket_empty()

    
    
    
       
    
    
    