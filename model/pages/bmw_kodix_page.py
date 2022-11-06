from selene import have

from test.conftest import *


class KodixPage:
    browser = setup_browser

    def click_navigation_item(self):
        browser.element('[title="BMW с пробегом"]').click()
        return self

    def check_company_text(self):
        browser.wait.until(10)
        browser.element('[class="main-footer"]').should(
            have.text('Kodix Automotive'))
        return self
