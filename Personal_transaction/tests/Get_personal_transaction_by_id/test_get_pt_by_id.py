import allure
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume
transaction_type_tbw = PersonalTransactionVariables.transaction_type_tbw


@allure.epic('GET /api/v1/personal_transaction/{personal_transaction_id}/ Получение cписка транзакций по id')
class TestGetById:

    @allure.description('Получение транзакции по существующему id (авторизованный пользователь)')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(personal_transaction_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result)
        PersonalTransactionMethods.check_required_fields_get(data)

    @allure.description('Получение транзакции по существующему id (неавторизованный пользователь)')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(personal_transaction_id, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 401)

    @allure.description('Несуществующий id')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 403)

    @allure.description('id = вещественное число (1,5)')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(1.5, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('id = 0')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('id = отрицательное значнеие')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(-1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('id = string')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('id - Поле отсутствует')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id_without_pt_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('pt_id = Пустое поле')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('pt_id = Null')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение информации о транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение информации о транзакции другого пользователя')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """авторизация второго пользователя"""
        result_auth = AuthMethods.login('100011', AuthVariables.auth_payloads_3)
        access_token_2 = result_auth.json().get('access_token')

        """Получение информации о транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(personal_transaction_id, access_token_2)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 403)



