from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser)
    page.open()
    page.should_be_login_link()

