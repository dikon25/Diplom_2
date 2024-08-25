import allure
import requests

from data import Endpoint, Message
from conftest import create_user
from helpers import *


class TestAuthUser:
    @allure.step('Логин под существующим пользователем')
    def test_auth_courier(self, create_user):
        login_pass = create_user
        r = requests.post(Endpoint.AUTH_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        })
        assert r.status_code == 200
        assert r.json()['success'] is True


    @allure.step('Логин с неверным логином и паролем.')
    def test_auth_not_existing_courier(self):
        r = requests.post(Endpoint.AUTH_USER, data={
            'email': 'Ivan@123',
            'password': '1234565'
        })
        assert r.status_code == 401
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.INCORRECT_DATA