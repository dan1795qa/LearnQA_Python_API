import allure

from Project.lib.my_requests import MyRequests
from Project.lib.base_case import BaseCase
from Project.lib.assertions import Assertions



@allure.epic("All path negative tests(edit username, email, firstName)")
class TestNegativeUserEdit(BaseCase):

    @allure.description("This test edit data no auth user")
    def test_edit_data_no_auth_user(self):
        """"REGISTER"""""
        data2 = self.prepare_registration_data()
        print(data2)
        response2 = MyRequests.post("/user/", data=data2)
        print(response2.json())
        user_id_from_auth_method = self.get_json_value(response2, "id")
        print(user_id_from_auth_method)

        """"EDIT"""
        new_name = "Changed_Name"
        response3 = MyRequests.put(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": "token"},
                                   cookies={"auth_sid": "auth_sid"},
                                   data={"username": new_name}
                                   )
        print(response3.text)

        Assertions.assert_code_status(response3, 400)


    @allure.description("This test edit data auth another user")
    def test_edit_data_auth_another_user(self):
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

        """"EDIT"""
        new_name = "Changed_Name"
        response3 = MyRequests.put(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"username": new_name,
                                         "password": '1234'}
                                   )
        print(response3.text)
        Assertions.assert_code_status(response3, 400)



    @allure.description("This test edit to an invalid email (without @)")
    def test_edit_an_invalid_email(self):
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

        """"EDIT"""
        wrong_email = email.replace('@', '')
        print(wrong_email)
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"email": wrong_email}
                                   )
        print(response3.text)
        Assertions.assert_code_status(response3, 400)


    @allure.description("This test edit to an one symbol 'firstName'")
    def test_edit_an_one_symbol_firstName(self):
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

        """"EDIT"""
        data = self.prepare_registration_data()
        data["firstName"] = self.generate_string(1)
        print(data)

        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data=data
                                   )
        print(response3.text)
        Assertions.assert_code_status(response3, 400)