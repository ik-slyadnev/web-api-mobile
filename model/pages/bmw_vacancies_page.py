from selene.support.conditions import have

from test.conftest import *


class SearchVacancies:
    browser = setup_browser

    def click_search(self):
        browser.element('[id="id-search_desktop"]').click()
        return self

    def search_by_text(self):
        browser.element('[name="search"]').send_keys('вакансия').press_enter()
        return self

    def checking_the_found_text(self):
        browser.element('[class="aems-sr-results"]').should(
            have.text('Вакансии - Карьера в компании BMW Group Россия | BMW'))
        return self

    def click_link(self):
        browser.element('//a[text()=" - Карьера в компании BMW Group Россия | BMW"]').click()
        return self

    def checking_text_bmw(self):
        browser.element('[class="main "]').should(
            have.text('BMW Group Russia'))
        return self
