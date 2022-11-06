import allure
from util.sessions import api
from model.api.api_helpers import *
from test.conftest import *


@pytest.mark.api
@allure.description('Test create item')
def test_create_item():
    with allure.step('Create new item'):
        MainApi().create_item()


@pytest.mark.api
@allure.description('Test get item')
def test_get_item():
    with allure.step('Get new item'):
        MainApi().get_item()


@pytest.mark.api
@allure.description('Test update item')
def test_update_item():
    with allure.step('Update item'):
        MainApi().update_item()


@pytest.mark.api
@allure.description('Test information in the database')
def test_info_bd():
    with allure.step('Checking information in the database'):
        MainApi().info_bd()


@pytest.mark.api
@allure.description('Test delete item')
def test_delete_item():
    with allure.step('Delete item'):
        MainApi().delete_item()
