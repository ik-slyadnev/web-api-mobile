import allure

from model.pages.vkusvill_start_page import StartPage
from model.pages.vkusvill_menu_page import MenuPage
from model.pages.vkusvill_catalog_page import MainCatalogPage
from model.pages.vkusvill_delete_page import DeletePage
from test.conftest import *
from util.attach import add_mob_video


@pytest.fixture(scope='function', autouse=True)
def create_driver():
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    return browser


@pytest.mark.mobile
@allure.description('Swipe menu items')
def test_swipe_menu():
    with allure.step('Click on the button'):
        StartPage().click_button()
    with allure.step('Swipe items'):
        MenuPage().item_profile().item_catalog().item_history().item_support()
    add_mob_video(browser)
    browser.quit()


@pytest.mark.mobile
@allure.description('Location view')
def test_loacation():
    with allure.step('Click on the button'):
        StartPage().click_button()
    with allure.step('Select catalog'):
        MenuPage().item_catalog()
    with allure.step('Enter address'):
        MainCatalogPage().address_button().location_selection().confirmation_buttons()
    add_mob_video(browser)
    browser.quit()


@pytest.mark.mobile
@allure.description('Delete catalog')
def test_delete():
    with allure.step('Click on the button'):
        StartPage().click_button()
    with allure.step('Swipe items'):
        MenuPage().item_profile()
    with allure.step('Deletion confirmation'):
        DeletePage().enter_buttons_delete()
    add_mob_video(browser)
    browser.quit()


@pytest.mark.mobile
@allure.description('Check contacts')
def test_contacts():
    with allure.step('Click on the button'):
        StartPage().click_button()
    with allure.step('Select support and viewing disputes'):
        MenuPage().item_support().tv_contact_call()
    add_mob_video(browser)
    browser.quit()


@pytest.mark.mobile
@allure.description('Loyalty program')
def test_loyalty_program():
    with allure.step('Click on the button'):
        StartPage().click_button()
    with allure.step('Select support and viewing loyalty'):
        MenuPage().item_support().loyalty_program()
    add_mob_video(browser)
    browser.quit()
