from appium.webdriver.common.appiumby import AppiumBy

from test.conftest import *


class StartPage():

    def click_button(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        return self

