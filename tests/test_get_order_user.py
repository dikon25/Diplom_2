import allure
import requests

from data import Message
from helpers import *


class TestOrderList:
    @allure.step('Получение заказов конкретного авторизированного пользователя')
    def test_get_order_list_auth_user(self):
        token = get_token()
        list = get_order_list(token)
        assert list.status_code == 200
        assert list.json()['success'] is True



    @allure.step('Получение заказов неавторизированного пользователя ')
    def test_get_order_list_unauth_user(self):
        token = ''
        list = get_order_list(token)
        assert list.status_code == 401
        assert list.json()['success'] is False
        assert list.json()['message'] == Message.NOTAUTORIZ