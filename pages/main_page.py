from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # так как ссылка постоянная для каждого объекта и по сути является атрибутом класса, создаем константу
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

    # передаем ссылку в конструктор BasePage
    def __init__(self, browser):
        super().__init__(browser, MainPage.MAIN_PAGE_URL)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

