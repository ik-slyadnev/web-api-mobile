import time

from appium.webdriver.common.appiumby import AppiumBy

from test.conftest import *


class DeletePage:

    def enter_buttons_delete(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn')).click()
        browser.element(
            (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        time.sleep(2)
        return self
