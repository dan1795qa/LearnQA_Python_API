import requests

headers = {"some_headers": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers",)

print(response.text)    # ОТВЕТ СЕРВЕРА
print(response.headers)    # ЗАГОЛОВКИ ОТВЕТА СЕРВЕРА НА ЭТОТ ЗАПРОС