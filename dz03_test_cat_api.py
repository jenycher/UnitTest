# test_cat_api.py

import pytest
from dz_at03 import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    # Мокируем requests.get для успешного ответа
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/MTY0MjEyNA.jpg'}
    ]

    cat_image_url = get_random_cat_image()
    assert cat_image_url == 'https://cdn2.thecatapi.com/images/MTY0MjEyNA.jpg'

def test_get_random_cat_image_failure(mocker):
    # Мокируем requests.get для неуспешного ответа
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = []

    cat_image_url = get_random_cat_image()
    assert cat_image_url is None
