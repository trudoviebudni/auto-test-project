from .base_page import BasePage
from .locators import ProductPageLocators


# страница с товаром
class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    # проверка, что появляется сообщение об успешном добавлении товара в корзину
    def should_be_add_message(self):
        success_message = "has been added to your basket."
        assert success_message in self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_BASKET).text, \
            "The success message for adding the item to the basket is not displayed."

    # проверка, что название товара в алерте соответствует названию товара на странице
    def check_name_in_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_product_name, f"The product name '{product_name}' does not match the name in the " \
                                                   f"alert '{alert_product_name}' "

    # проверяем, что тотал в корзине совпадает со стоимостью товара
    def check_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text
        assert product_price == basket_total, f"The product price '{product_price}' does not match the basket total " \
                                              f"in the alert '{basket_total}' "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_BASKET), \
            "The success message for adding the item to the basket is displayed, but should not be."

