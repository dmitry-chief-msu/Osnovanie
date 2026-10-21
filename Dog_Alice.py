from tkinter import Tk, Label, Button, messagebox
from PIL import Image, ImageTk
from io import BytesIO
import requests
import threading
import time

# Создаём одну сессию на всё время работы — это ускоряет повторные запросы и стабилизирует соединение
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

def fetch_image_and_update(label_widget):
    err_msg = None
    photo = None

    # 1. Получаем URL картинки
    try:
        resp = session.get('https://dog.ceo/api/breeds/image/random', timeout=7)
        resp.raise_for_status()
        data = resp.json()
        url = data.get('message')
        if not url:
            raise ValueError('В ответе API нет ссылки на картинку')
        print(data)  # твой JSON будет в консоли
    except Exception as err:
        err_msg = f'Ошибка получения ссылки: {err}'
        print(f'Фоновая ошибка: {err_msg}')
        goto_update_ui()
        return

    # 2. Скачиваем картинку с повторными попытками
    attempts = 3
    base_timeout = 15
    for i in range(1, attempts + 1):
        try:
            timeout = base_timeout * i  # 15, 30, 45 сек
            resp_img = session.get(url, timeout=timeout)
            resp_img.raise_for_status()

            # Быстрая проверка: контент действительно картинка?
            if not resp_img.content or len(resp_img.content) < 100:
                raise ValueError('Получен пустой или слишком маленький ответ (возможно, HTML-ошибка вместо картинки)')

            image_data = BytesIO(resp_img.content)
            img = Image.open(image_data)
            img.thumbnail((600, 480))
            photo = ImageTk.PhotoImage(img)
            break  # всё получилось
        except Exception as err:
            print(f'Попытка {i} не удалась: {err}')
            if i == attempts:
                err_msg = str(err)
            else:
                time.sleep(1)  # небольшая пауза перед следующей попыткой

    def goto_update_ui():
        def update_ui():
            if photo is not None:
                label_widget.config(image=photo)
                label_widget.image = photo  # критически важно!
            else:
                messagebox.showerror('Ошибка загрузки', err_msg)
        root.after(0, update_ui)

    goto_update_ui()

def start_load():
    t = threading.Thread(target=fetch_image_and_update, args=(label,), daemon=True)
    t.start()

root = Tk()
root.title('Dogs')
root.geometry('620x550')

label = Label(root)
label.pack(pady=10)

btn = Button(root, text='Загрузить', command=start_load)
btn.pack()

root.mainloop()
