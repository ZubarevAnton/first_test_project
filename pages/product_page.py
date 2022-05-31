from selenium.webdriver.common.by import By

from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from math import log, sin
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_basket_message_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_TITLE).text
        basket_title = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_TITLE).text
        assert product_title == basket_title, "Incorrect product title"

    def check_basket_message_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        assert product_price == basket_price, "Incorrect product price"



