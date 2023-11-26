from datetime import datetime
import allure
from Pytest.lib.my_requests import MyRequests
import requests
from Pytest.lib.base_case import BaseCase
from Pytest.lib.assertions import Assertions

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    @allure.description("This test successfuly created user")
    def test_create_user_successfuly(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test created user with existing email")
    def test_create_user_with_existing_email(self):

        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        # print(response.status_code)
        # print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"           #если выводит символ 'b' то нужно втсавить кодировку!!!




