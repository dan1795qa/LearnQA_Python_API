import requests

response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)


response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)    # True - default(200) False - 301
# print(response.status_code)

first_response = response.history[0]
second_response = response
print(first_response.status_code)
print(first_response.url)
print(second_response.status_code)
print(second_response.url)
