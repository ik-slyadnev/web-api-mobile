from appium.webdriver.common.appiumby import AppiumBy

from test.conftest import *


class MainCatalogPage():

    def address_button(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/button_service_not')).click()
        return self

    def location_selection(self):
        browser.element(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/tv_address')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/search')).send_keys('Moscow, Prospekt Mira, 95с1')
        return self

    def confirmation_buttons(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/rl_root')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_select')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/button_rules_ok')).click()
        return self
