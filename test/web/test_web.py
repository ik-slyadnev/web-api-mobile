import allure

from test.conftest import *
from model.pages.bmw_main_page import NavigationItem
from model.pages.bmw_vacancies_page import SearchVacancies
from model.pages.bmw_configurator_page import ConfiguratorModel
from model.pages.bmw_kodix_page import KodixPage

@pytest.mark.web
@allure.description('Click link navigation item')
def test_click_navigation_item(setup_browser):
    browser.open('ru/all-models')

    with allure.step('Viewing the Cars tab'):
        NavigationItem().click_navigation_item_all_models()

    with allure.step('View the Purchase tab'):
        NavigationItem().click_navigation_item_all_models()

    with allure.step('View the Owners tab'):
        NavigationItem().click_navigation_item_all_models()

    with allure.step('View tab BMW Russia'):
        NavigationItem().click_navigation_item_all_models()


@pytest.mark.web
@allure.description('Use search')
def test_search_vacancies(setup_browser):
    browser.open('ru/all-models')

    with allure.step('Clicking on the search button'):
        SearchVacancies().click_search()

    with allure.step('Entering text'):
        SearchVacancies().search_by_text()

    with allure.step('Validation of the entered text'):
        SearchVacancies().checking_the_found_text()

    with allure.step('Select text'):
        SearchVacancies().click_link()

    with allure.step('Text check'):
        SearchVacancies().checking_text_bmw()


@pytest.mark.web
@allure.description('Check models')
def test_bmw_models(setup_browser):
    browser.open('ru/index.html')

    with allure.step('Check configurator'):
        ConfiguratorModel().check_configurator()

    with allure.step('Check model BMW('):
        ConfiguratorModel().check_model_bmw()



@pytest.mark.web
@allure.description('Checking company Kodix')
def test_bmw_kodix(setup_browser):
    browser.open('ru/all-models')
    with allure.step('click navigation item'):
        KodixPage().click_navigation_item()

    with allure.step('Checking company text'):
        KodixPage().check_company_text()




@pytest.mark.web
@allure.description('Check location')
def test_bmw_check_all_models(setup_browser):
    browser.open('ru/index.html')

    with allure.step('View All Models'):
        NavigationItem().click_navigation_item_all_models()
        NavigationItem().bmw_check_all_models()

