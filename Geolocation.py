from tkinter import Tk, Entry, Label, Button, messagebox
from deep_translator import GoogleTranslator
from opencage.geocoder import OpenCageGeocode
import os
import requests
import webbrowser



# Инициализируем переводчик один раз
translator = GoogleTranslator(source='ru', target='en')

# Получаем ключ из переменной окружения; если нет — используем заглушку (но покажем предупреждение)
API_KEY = os.getenv("OPENCAGE_API_KEY", "db71ebb348bb40a8a2f187e461a60bce")

def get_weather(lat,lon):
    try:
        response = requests.get(f'https://api.open-meteo.com/v1/forecast'
                                f'?latitude={lat}&longitude={lon}'
                                f'&current_weather=true')
        weather_data = response.json()
        current_weather = weather_data['current_weather']
        return current_weather
    except Exception as err:
        return f'Ошибка при получении погоды {err}'

def show_weather():
    current_weather = get_weather(lat, lon)
    weather_window=Toplevel(root)
    weather_window.title('Текущая погода')
    if isinstance(current_weather, tuple):
        label = Label(weather_window, text=current_weather)
    else:
        label = Label(weather_window, text=current_weather)
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']


def translate_city(city: str) -> str:
    try:
        return translator.translate(city)
    except Exception as e:
        return f"[ошибка перевода]: {e}"

def get_coordinates(city: str):
    global lat, lon
    try:
        geolocator = OpenCageGeocode(API_KEY)
        results = geolocator.geocode(city, limit=1)
        if results:
            r = results[0]
            lat = round(r["geometry"]["lat"], 2)
            lng = round(r["geometry"]["lng"], 2)
            # Возвращаем только координаты: город подставим в show_result, где у нас есть перевод
            return lat, lng
        else:
            return None
    except Exception as e:
        return f"Ошибка геокодинга: {e}"

def show_result(event=None):
    city = entry.get().strip()
    if not city:
        messagebox.showinfo("Инфо", "Введите название города")
        return

    # Сначала получаем перевод (он быстрый)
    #translated = translate_city(city)
    translated = city

    # Потом координаты (это сетевой запрос)
    coords = get_coordinates(city)

    if isinstance(coords, tuple):
        lat, lng = coords
        result = f"Город {city} ({translated})\nШирота: {lat}, Долгота: {lng}"
    elif isinstance(coords, str):
        # Это сообщение об ошибке от геокодера
        result = f"{coords}"
    else:
        result = "Город не найден"

    label_result.config(text=result)
    print (result)

# Проверка ключа при старте (без создания лишнего окна)
if API_KEY == "db71ebb348bb40a8a2f187e461a60bce":
    print("ВНИМАНИЕ: используется тестовый ключ. Для реальной работы задайте OPENCAGE_API_KEY в переменных окружения.")

root = Tk()
root.title("Поиск координат и перевод")
root.geometry("400x250")

entry = Entry(root, width=40)
entry.pack(pady=10)
entry.focus_set()
entry.bind("<Return>", show_result)

btn = Button(root, text="Найти", command=show_result)
btn.pack()

label_result = Label(root, wraplength=350, justify="left", anchor="w")
label_result.pack(pady=15)

root.mainloop()
