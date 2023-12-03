from datetime import datetime
import allure
from Project.lib.my_requests import MyRequests
import requests
from Project.lib.base_case import BaseCase
from Project.lib.assertions import Assertions


@allure.epic("Auth/no auth cases")
class TestUserGet(BaseCase):

    """"Тест для неавторизрванного пользователя"""""
    @allure.description("This test no auth user")
    def test_get_user_details_not_auth(self):

        response = MyRequests.get("/user/2")
        print(response.json())
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")


    """"Тест для авторизрванного пользователя"""
    @allure.description("This test auth user")
    def test_get_user_details_auth_as_same_user(self):

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        print(response1.json())
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        print(response2.json())
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)



    """"Тест авторизрванного пользователя для получения данных другого пользователя"""

    @allure.description("This test get details another user")
    def test_get_another_user_details_auth_as_same_user(self):

        data1 = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data1)
        print(response1.json())

        data2 = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=data2)
        print(response2.json())
        user_id_from_auth_method = self.get_json_value(response2, "id")
        print(user_id_from_auth_method)

        response3 = MyRequests.get(f"/user/{user_id_from_auth_method}")
        print(response3.json())
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_key(response3, "email")
        Assertions.assert_json_has_not_key(response3, "firstName")
        Assertions.assert_json_has_not_key(response3, "lastName")

