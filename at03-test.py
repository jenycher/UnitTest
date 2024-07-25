# test_at03_mocking.py
#мокинг - имитировать поведение реальных объектов

import pytest
from at03_mocking import get_weather


def test_get_weather(mocker):
    # Мокинг requests.get
    mock_get = mocker.patch('requests.get')
    # Настраиваем возвращаемое значение для мок-объекта
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

    #api_key = 'a74e12a2e27f8a0e5a2eb9cb055a82b0'
    api_key="test-key" # так тоже это работает
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'test_api_key'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == None