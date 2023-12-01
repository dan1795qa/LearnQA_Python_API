import random
import string
from datetime import datetime

import allure
import pytest
from Project.lib.my_requests import MyRequests
from Project.lib.base_case import BaseCase
from Project.lib.assertions import Assertions

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


    def test_create_user_with_incorrect_email(self):

        wrong_email = 'vinkotovexample.com'
        data = self.prepare_registration_data(wrong_email)
        print(data)

        response = MyRequests.post("/user/", data=data)
        print("\n" + response.text)
        Assertions.assert_code_status(response, 400)
        assert response.text == "Invalid email format", f"Unexpected response content body"



    # @pytest.mark.parametrize('data', parameters)
    # def test_create_user_without_anyone_parameter(self, data):
    #
    #     data = self.prepare_registration_data1()
    #     print(data)
    #
    #     response = MyRequests.post("/user/", data=data)
    #     print("\n" + response.text)
    #     Assertions.assert_code_status(response, 200)
    #     assert response.text == "Invalid email format", f"Unexpected response content body"


    def test_create_user_with_one_symbol_user_name(self, length=1):
        data = self.prepare_registration_data()
        data["firstName"] = self.generate_string(1)
        print(data)

        response = MyRequests.post("/user/", data=data)
        print("\n" + response.text)
        Assertions.assert_code_status(response, 400)
        # Assertions.assert_json_has_key(response, "id")
        assert response.text == "The value of 'firstName' field is too short", f"Unexpected response content body"


    def test_create_user_with_more_250_symbol_user_name(self):

        data = self.prepare_registration_data()
        data["firstName"] = self.generate_string(250)
        print(data)

        response = MyRequests.post("/user/", data=data)
        print("\n" + response.text)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")










