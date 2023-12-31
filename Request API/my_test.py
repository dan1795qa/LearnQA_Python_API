import pytest
import requests

""""ex10"""
def test_ex10():
    phrase = input("Set a phrase: ")

    assert len(phrase) <= 15, f"count symbols more than 15!!!"


''''ex11'''
def test_ex11():

    response12 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    response11_cookies = response12.cookies
    print('\n' + f"{response11_cookies}")

    assert response11_cookies.get('HomeWork') == 'hw_value', f"No find cookies 'Homework'"

''''ex12'''
def test_ex12():

    response12 = requests.get("https://playground.learnqa.ru/api/homework_header")
    response12_headers = response12.headers
    response12_text = response12.text
    response12_json = response12.json()
    response_expected = {'success': '!'}

    print('\n' + f"Headers response: {response12_headers}")
    print(f"Response server: {response12_text}")
    print(response12_json)

    assert response12_json == response_expected, f"Failed"


''''ex13'''
exclude_params = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

@pytest.mark.parametrize('value', exclude_params)
# @pytest.mark.parametrize('expected_value', expected_value)
def test_ex13(value):

    expected_value = [
        {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]

    headers = {"User-Agent": value}
    response13 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=headers)
    response13_json = response13.json()
    print(response13_json)

    response13_platform = response13_json.get('platform')
    assert response13_platform == expected_value[0].get('platform'), f"Parameter 'platform': {response13_platform} - wrong!!! Expected value is '{expected_value[0].get('platform')}'"

    response13_browser = response13_json.get('browser')
    assert response13_browser == expected_value[0].get('browser'), f"Parameter 'browser': {response13_browser} - wrong!!! Expected value is '{expected_value[0].get('browser')}'"

    response13_device = response13_json.get('device')
    assert response13_device == expected_value[0].get('device'), f"Parameter 'device': {response13_device} - wrong!!! Expected value is '{expected_value[0].get('device')}'"

    print('-' * 50)
    expected_value = expected_value.pop(0)


