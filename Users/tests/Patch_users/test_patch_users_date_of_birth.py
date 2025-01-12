import allure
from common_methods.checking import Checking
from common_methods.variables import CommonVariables, AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@allure.epic('Patch/users/me Проверка поля data_of_birth')
class TestPatchUsersEmail:

    @allure.description('date of birth - Валидная дата')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля date_of_birth"""
        data = Checking.get_data(result)
        assert data['date_of_birth'] == AuthVariables.date_of_birth

    @allure.description('date of birth - Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone_date_of_birth(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('date of birth - Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля date_of_birth"""
        data = Checking.get_data(result)
        assert data['date_of_birth'] is None

    @allure.description('date of birth - Пустое поле')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля date_of_birth"""
        data = Checking.get_data(result)
        assert data['date_of_birth'] is None

    @allure.description('date of birth - Дата в будущем')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '2030-10-10', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('date of birth - Неверный порядок формата даты (дд-мм-гггг)')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '10-10-2010', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('date of birth - Неверный разделитель в формате даты (гггг.мм.дд)')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '2010.10.10', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('date of birth - Недопустимые символы')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, 'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('date of birth - Неверный тип данных (integer)')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, 2020-10-10, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
