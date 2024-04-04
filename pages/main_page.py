from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    # так как ссылка постоянная для каждого объекта и по сути является атрибутом класса, создаем константу
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

    """
    ссылка имеет значение дефолт на случай, если страница отроется как стартовая в тест-кейсе.
    если ссылка передается явно в конструктор,
    значит осуществился переход на страницу с другой страницы и это часть тест кейса
    """
    def __init__(self, browser, url=MAIN_PAGE_URL):
        super().__init__(browser, url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

