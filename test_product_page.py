import pytest
import faker
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestUsersAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        password = str(time.time())

        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_autorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_basket_message_title()
        page.check_basket_message_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('promo_code', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail),
                                        '8', '9'])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}")
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.check_basket_message_title()
    page.check_basket_message_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_diseppeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_product()
    basket_page.should_be_empty_basket_message()
