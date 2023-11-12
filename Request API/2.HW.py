import json
import time

import requests

""""ex5"""
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
result = json.loads(json_text)
print(type(result))
print(result)

print("-"*100)

""""ex6"""
response_6 = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(len(response_6.history))
print(response_6.url)

print("-"*100)

""""ex7"""
methods = [{"method": "GET"}, {"method": "POST"}, {"method": "DELETE"}, {"method": "PUT"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method in methods:
    print(f"Для параметра {method}")
    print("Для метода GET")
    response_7 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    if response_7.text == '{"success":"!"}':
        print("success")
    # print(response_7.text)
    print("Для метода POST")
    response_7 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    if response_7.text == '{"success":"!"}':
        print("success")
    # print(response_7.text)
    print("Для метода PUT")
    response_7 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    if response_7.text == '{"success":"!"}':
        print("success")
    # print(response_7.text)
    print("Для метода DELETE")
    response_7 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    if response_7.text == '{"success":"!"}':
        print("success")
    # print(response_7.text)
    print("_"*10)

print("-"*100)

""""ex8"""
print('1) Создана задача')
response_8 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", )
print(json.loads(response_8.text))
token = json.loads(response_8.text)

print('2) Задача выполняется')
response_8 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response_8.text)

print('3) Время ожидания')
print(f"Необходимо ждать: {token['seconds']} секунд")
time.sleep(token['seconds'])

print('4) Задача выполнена')
response_8 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response_8.text)