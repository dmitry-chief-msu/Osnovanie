import requests
from PIL import Image
from io import BytesIO

url = "https://dog.ceo/api/breeds/image/random"
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    print("1. Получаем URL картинки...")
    r1 = requests.get(url, headers=headers, timeout=10)
    r1.raise_for_status()
    data = r1.json()
    image_url = data["message"]
    print(f"2. Получен URL: {image_url}")

    print("3. Скачиваем картинку...")
    r2 = requests.get(image_url, headers=headers, timeout=20)
    r2.raise_for_status()
    print(f"3a. Статус скачивания: {r2.status_code}, размер: {len(r2.content)} байт")

    img_data = BytesIO(r2.content)
    img = Image.open(img_data)
    print(f"4. Картинка открыта. Формат: {img.format}, размер: {img.size}")
    print("5. Всё работает, Pillow в порядке.")
except Exception as e:
    print(f"Ошибка: {e}")
