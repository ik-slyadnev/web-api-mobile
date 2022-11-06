import allure

from model.api.schemas.model_scheme import *
from util.sessions import api


class MainApi:
    def create_item(self):
        response = api().post('create', json={
            "name": "Спортивные шорты",
            "section": "Верхняя одежда",
            "description": "Из новой коллекции!",
            "color": "RED",
            "size": 46,
            "price": 1999,
            "params": "dress"
        })

        with allure.step('status code is 200'):
            assert response.status_code == 200
        with allure.step('schema check'):
            assert S(create_item) == response.json()
        with allure.step('status check'):
            assert str(response.json()['status']) == 'ok'
        with allure.step('check name'):
            assert str(response.json()['result']['name']) == 'Спортивные шорты'
        with allure.step('check section'):
            assert str(response.json()['result']['section']) == 'Верхняя одежда'
        with allure.step('check description'):
            assert str(response.json()['result']['description']) == 'Из новой коллекции!'
        with allure.step('check color'):
            assert str(response.json()['result']['color']) == 'RED'
        with allure.step('check price'):
            assert str(response.json()['result']['price']) == '1999'
        with allure.step('check params'):
            assert str(response.json()['result']['params']) == 'dress'
        global item_id
        item_id = response.json()['result']['id']
        return self

    def get_item(self):
        response = api().get('get', json={
            "id": f'{item_id}'
        })

        with allure.step('status code is 200'):
            assert response.status_code == 200
        with allure.step('schema check'):
            assert S(get_item) == response.json()
        with allure.step('check status'):
            assert str(response.json()['status']) == 'ok'
        with allure.step('check id'):
            assert str(response.json()['result']['id']) == f'{item_id}'
        with allure.step('check name'):
            assert str(response.json()['result']['name']) == 'Спортивные шорты'
        with allure.step('check section'):
            assert str(response.json()['result']['section']) == 'Верхняя одежда'
        with allure.step('check description'):
            assert str(response.json()['result']['description']) == 'Из новой коллекции!'
        with allure.step('check color'):
            assert str(response.json()['result']['color']) == 'RED'
        with allure.step('check price'):
            assert str(response.json()['result']['price']) == '1999'

        return self

    def update_item(self):
        response = api().post('update/', json={
            "id": f"{item_id}",
            "name": "Легкое платье",
            "section": "Платья",
            "description": "Из старой коллекции!",
            "color": "GREEN",
            "size": 48,
            "price": 2999,
            "params": "dress",
        })

        with allure.step('status code is 200'):
            assert response.status_code == 200
        with allure.step('schema check'):
            assert S(update_item) == response.json()
        with allure.step('check status'):
            assert str(response.json()['status']) == 'ok'
        with allure.step('check result'):
            assert str(response.json()['result']) == 'Товар обновлен!'
        return self

    def info_bd(self):
        response = api().post('/select//', json={
            "sql_query": f"select * from items where last_id = {item_id};"
        })

        with allure.step('status code is 200'):
            assert response.status_code == 200
        with allure.step('schema check'):
            assert S(info_bd) == response.json()
        with allure.step('check status'):
            assert str(response.json()['status']) == 'ok'
        with allure.step('check title'):
            assert str(response.json()['result'][0]['title']) == 'Легкое платье'
        with allure.step('check price'):
            assert str(response.json()['result'][0]['price']) == '2999'
        with allure.step('check description'):
            assert str(response.json()['result'][0]['description']) == 'Из старой коллекции!'
        return self

    def delete_item(self):
        response = api().post('delete/', json={
            "id": f"{item_id}"
        })

        with allure.step('status code is 200'):
            assert response.status_code == 200
        with allure.step('schema check'):
            assert S(delete_item) == response.json()
        with allure.step('check status'):
            assert str(response.json()['status']) == 'ok'
        with allure.step('check result'):
            assert str(response.json()['result']) == f'Товар с ID {item_id} успешно удален'
        return self

