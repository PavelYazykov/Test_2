
import pytest
from common_methods.auth import Auth
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.fixture()
def auth_fixture():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    return access_token


@pytest.fixture()
def create_moneybox_and_delete():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 2, amount, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['id']
    yield moneybox_id, access_token
    MoneyboxMethods.delete_moneybox(moneybox_id, access_token)


@pytest.fixture()
def create_moneybox():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['id']
    return moneybox_id, access_token

