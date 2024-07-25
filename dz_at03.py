#Напишите функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки.
# https://api.thecatapi.com/v1/images/search

import requests

def get_random_cat_image():
    """Возвращает URL случайного изображения кошки."""
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяет, не произошла ли ошибка
        data = response.json()  # Преобразует ответ в формат JSON
        if data:
            return data[0]['url']
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

# Пример использования функции
cat_image_url = get_random_cat_image()
if cat_image_url:
    print(f"Случайное изображение кошки: {cat_image_url}")
else:
    print("Не удалось получить изображение кошки.")
