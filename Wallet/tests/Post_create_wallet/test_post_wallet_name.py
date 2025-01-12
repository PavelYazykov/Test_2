import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods


@allure.epic('Post/api/v1/wallet/  Создание счета')
class TestCreateWallet:

    @allure.description('Создане счета проверка поля name - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'w', 2, 0, access_token
        )
        print(result.text)
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'w'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - 19 символов')
    def test_02(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wwwwwwwwwwqqqqqqqqq',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'wwwwwwwwwwqqqqqqqqq'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - 20 символов')
    def test_03(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wwwwwwwwwwqqqqqqqqqs',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'wwwwwwwwwwqqqqqqqqqs'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Цифры')
    def test_04(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            '12345',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == '12345'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Кириллица')
    def test_05(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'Счет',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'Счет'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Латиница')
    def test_06(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallets',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'wallets'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Пробел')
    def test_07(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'Латин ица',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'Латин ица'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Тире')
    def test_08(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'Латин-ица',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'Латин-ица'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Точка')
    def test_09(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'Латин.ица',
            2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            assert data['data']['name'] == 'Латин.ица'
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля name - Поле отсутствует')
    def test_10(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet_without_name(
            2, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля name - Пустое поле')
    def test_11(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            '',
            2, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля name - Null')
    def test_12(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            None,
            2, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля name - 21 символ')
    def test_13(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'NoneNoneNoneNoneNoneq',
            2, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля name - Спецсимволы')
    def test_14(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            '!@#$%%^&&*',
            2, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


