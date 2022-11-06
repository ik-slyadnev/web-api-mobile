import time
from selene import have
from selene.support.shared import browser
from test.conftest import *


class NavigationItem:
    browser = setup_browser

    def click_navigation_item_all_models(self):
        browser.element('[title="Автомобили"]').click()
        time.sleep(1)
        return self

    def click_navigation_item_buy(self):
        browser.element('[title="Покупка"]').click()
        time.sleep(1)
        return self

    def click_navigation_item_owners(self):
        browser.element('[title="Владельцам"]').click()
        time.sleep(1)
        return self

    def click_navigation_item_BMW_Russia(self):
        browser.element('[title="BMW Россия"]').click()
        time.sleep(1)
        return self

    def bmw_check_all_models(self):
        browser.element('[data-series="X"]').click()
        time.sleep(1)
        browser.element('[data-series="M"]').click()
        time.sleep(1)
        browser.element('[data-series="8"]').click()
        time.sleep(1)
        browser.element('[data-series="7"]').click()
        time.sleep(1)
        browser.element('[data-series="6"]').click()
        time.sleep(1)
        browser.element('[data-series="5"]').click()
        time.sleep(1)
        browser.element('[data-series="4"]').click()
        time.sleep(1)
        browser.element('[data-series="3"]').click()
        time.sleep(1)
        browser.element('[data-series="2"]').click()
        time.sleep(1)
        browser.element('[data-series="Z"]').click()
        time.sleep(1)
        browser.element('[data-series="BMW Концепты"]').click()
        return self
