from appium.webdriver.common.appiumby import AppiumBy

from test.conftest import *


class MenuPage:
    def item_profile(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_profile')).click()
        return self

    def item_catalog(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_catalog')).click()
        return self

    def item_history(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_history')).click()
        return self

    def item_support(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        return self

    def tv_contact_call(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/tv_contact_call')).click()
        return self

    def loyalty_program(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/sl')).click()
        return self
