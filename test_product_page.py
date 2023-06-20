from .pages.product_page import ProductPage
import time
import pytest



@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" if i != 7 else pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" ,marks=pytest.mark.xfail)  for i in range(10)])#,pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" ,marks=pytest.mark.xfail) )
def test_guest_can_add_product_to_basket(browser,link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser,link)
    product_page.open()
    
    product_page.should_be_button_add_product_to_basket()
    product_page.should_add_product_to_basket()
    
    product_page.should_alert_be_and_calculate()
    
    product_page.check_add_name_product()
    
    
    
    
    
    