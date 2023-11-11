import requests

headers = {"some_headers": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

print(response.text)    # ЗАГОЛОВКИ ЗАПРОСА
print(response.headers)    # ЗАГОЛОВКИ ОТВЕТА