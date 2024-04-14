from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    BASKET_PAGE_URL = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'

    def __init__(self, browser, url=BASKET_PAGE_URL):
        super().__init__(browser, url)

    def should_be_text_message_for_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_MESSAGE_EMPY_BASKET), \
            "Text message is not presented."

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"



