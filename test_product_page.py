from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time
import pytest


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        
        
        page = BasePage(browser,link)
        page.open()
        
        page.go_to_login_page()
        page = LoginPage(browser,browser.current_url)
        page.register_new_user()
        page = BasePage(browser,browser.current_url)
        page.should_be_authorized_user()
       
        
    
    
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" if i != 7 else pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" ,marks=pytest.mark.xfail)  for i in range(10)])
    def test_user_can_add_product_to_basket(self,browser,link):
        product_page = ProductPage(browser,link)
        product_page.open()    
        product_page.should_be_button_add_product_to_basket()
        product_page.should_add_product_to_basket()
        product_page.should_alert_be_and_calculate()
        product_page.check_add_name_product()
        product_page.compare_prise_product_and_prise_in_basket()
         
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        product_page = ProductPage(browser,link)
        product_page.open()
        product_page.should_not_be_success_message()    
        
        
        
    
@pytest.mark.parametrize('link', [pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}",marks=pytest.mark.xfail) for i in range(1) ])    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    product_page = ProductPage(browser,link)  
    product_page.open()
    product_page.should_add_product_to_basket()
    product_page.should_not_be_success_message()
    
    
@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(1) ]) 
def test_guest_cant_see_success_message(browser,link):
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.should_not_be_success_message()
    
    
@pytest.mark.parametrize('link', [pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}",marks=pytest.mark.xfail) for i in range(1) ]) 
def test_message_disappeared_after_adding_product_to_basket(browser,link):     
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.should_add_product_to_basket()
    product_page.should_not_ne_success_massage_all_time()
    
def test_guest_should_see_login_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page() 
    page.should_be_login_link()      
    
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser,link)
    page.open()
    page.go_to_basket_page()
    
    page = BasketPage(browser,browser.current_url)
    page.zero_products_in_basket()
    page.message_about_basket_empty()
    
    
@pytest.mark.need_review    
@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" if i != 7 else pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" ,marks=pytest.mark.xfail)  for i in range(10)])
def test_guest_can_add_product_to_basket(browser,link):
    product_page = ProductPage(browser,link)
    product_page.open()    
    product_page.should_be_button_add_product_to_basket()
    product_page.should_add_product_to_basket()
    product_page.should_alert_be_and_calculate()
    product_page.check_add_name_product()
    product_page.compare_prise_product_and_prise_in_basket()
    
        
        
    
    
    
    
    
    