import time

from selenium.webdriver.common.by import By


class TestOnlineShop:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    add_button_locator = (By.CLASS_NAME, 'btn-add-to-basket')

    def test_displayed_add_to_basket_button(self, browser):
        browser.get(self.link)
        add_button = browser.find_element(*self.add_button_locator)
        time.sleep(30)
        assert add_button.is_displayed() is True, 'Expected displayed "Add to basket" button'
