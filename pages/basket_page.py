from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_product(self):
        assert self.is_not_element_present(
            *BasketPageLocators.NOT_EMPTY_BASKET), "The basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"


