import json
import allure
from common_methods.checking import Checking
from common_methods.auth import Auth
from Auth.methods.auth_methods import AuthMethods
from Auth.methods.payloads import AuthLogin
from common_methods.variables import AuthVariables
payloads = AuthVariables.auth_payloads


@allure.epic('Post_reset_password/refresh Обновление рефреш токена')
class TestRefresh:

    @allure.description('Существующий refresh_token')
    def test_01(self):

        """Авторизация"""
        auth_result = Auth.auth()

        """Получение refresh_token"""
        refresh_token = AuthMethods.get_refresh_token(auth_result)

        """Запрос на обновление"""
        result = AuthMethods.refresh(
            refresh_token, payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия робязательных полей"""
        with allure.step('Проверка наличия робязательных полей'):
            AuthLogin(**result.json())

    @allure.description('Несуществующий refresh_token')
    def test_02(self):

        """Авторизация"""
        auth_result = Auth.auth()

        """Получение refresh_token"""
        refresh_token = AuthMethods.get_refresh_token(auth_result)

        """Запрос на обновление"""
        result = AuthMethods.refresh(
            refresh_token + 'x', 'y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

    @allure.description('Пустое поле')
    def test_03(self):
        result = AuthMethods.refresh(
            '', payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

    @allure.description('Поле отсутствует')
    def test_04(self):
        result = AuthMethods.refresh_without_refresh(
            payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

    @allure.description('Null')
    def test_05(self):
        result = AuthMethods.refresh(
            None, payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)
