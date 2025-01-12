import allure
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 156


@allure.epic('Delete/api/v1/subcategory/ - Удаление подкатегории - Проверка поля subcategory_id')
class TestDeleteSubcategoryCheckScId:

    @allure.description('Проверка поля subcategory_id - Cуществующая подкатегория')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
        Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля subcategory_id - несуществующая подкатегория')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(100, access_token)
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Проверка поля subcategory_id - Значение category_id = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(0, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Проверка поля subcategory_id - Значение category_id = отрицательное число')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(0, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Проверка поля subcategory_id - Значение category_id = пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory('', access_token)
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Проверка поля subcategory_id - Значение category_id = Null')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(None, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Проверка поля subcategory_id - Значение category_id = string')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory('string', access_token)
        Checking.check_statuscode(result_delete, 422)
