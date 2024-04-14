from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn[href='/en-gb/basket/']")


class MainPageLocators:
    pass


class LoginPageLocators:
    # login form
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "div.login_form button[name='login_submit']")
    # register form
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "div.register_form button[name='registration_submit']")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "div.product_main button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p strong")


class BasketPageLocators:
    TEXT_MESSAGE_EMPY_BASKET = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
