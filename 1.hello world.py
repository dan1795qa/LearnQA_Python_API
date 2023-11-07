import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.status_code)
print(response.text)
