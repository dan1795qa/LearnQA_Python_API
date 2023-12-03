import allure

from Project.lib.my_requests import MyRequests
from Project.lib.base_case import BaseCase
from Project.lib.assertions import Assertions



@allure.epic("All tests to method 'DELETE'")
class TestUserDelete(BaseCase):

    @allure.description("This test delete user(ID 2)")
    def test_delete_user_id_2(self):
        """"LOGIN"""""
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        print(auth_sid)
        token = self.get_header(response1, "x-csrf-token")
        print(token)

        """"DELETE"""""
        id = '2'
        response2 = MyRequests.delete(f"/user/{id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        print(response2.text)
        Assertions.assert_code_status(response2, 400)



    @allure.description("This test delete created user")
    def test_delete_created_user(self):
        """"REGISTER"""""
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")
        print(user_id)

        """"LOGIN"""
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        print(auth_sid)
        token = self.get_header(response2, "x-csrf-token")
        print(token)

        """"DELETE"""""

        response2 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        print(response2.text)
        Assertions.assert_code_status(response2, 200)

        """"CHECKS GET DATA DELETED USER"""""
        response = MyRequests.get(f"/user/{user_id}")
        print(response.content)

        # Assertions.assert_json_has_key(response, "username")
        # Assertions.assert_json_has_not_key(response, "email")
        # Assertions.assert_json_has_not_key(response, "firstName")
        # Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("This test delete user under auth another user")
    def test_delete_user_under_auth_another_user(self):
        """"REGISTER"""""
        data2 = self.prepare_registration_data()
        print(data2)
        response2 = MyRequests.post("/user/", data=data2)
        print(response2.json())
        user_id_from_auth_method = self.get_json_value(response2, "id")

        print(user_id_from_auth_method)

        """"LOGIN"""
        data1 = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data1)
        print(response1.json())
        auth_sid = self.get_cookie(response1, "auth_sid")
        print(auth_sid)
        token = self.get_header(response1, "x-csrf-token")
        print(token)

        """"DELETE"""""

        response3 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        print(response3.text)
        Assertions.assert_code_status(response2, 200)

        response4 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        """"CHECKS GET DATA DELETED USER"""""
        response = MyRequests.get(f"/user/{user_id_from_auth_method}")
        print(user_id_from_auth_method)
        print(response.content)

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")