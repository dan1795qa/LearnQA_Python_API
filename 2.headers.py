import requests

headers = {"some_headers": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

print(response.text)    # ответ сервера (какие заголовки он получил)
print(response.headers)    # ответ сервера на запрос