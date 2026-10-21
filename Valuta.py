from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
import requests
import json
import pprint

def update_currency_label(event):
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def exchange():
    #code = entry.get().upper().strip()
    code=combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = currencies[code]
                mb.showinfo('Курс обмена', f'Курс к USD: {exchange_rate: .1f}{code} за 1 USD')
            else:
                mb.showerror('Ошибка', f'Валюта не найдена')
        except Exception as err:
            mb.showerror('Ошибка')
    else:
        mb.showerror('Ошибка')


currencies = {
    'EUR': 'Евро',
    'JPY': '',
    'GBP': '',
    'AUD': '',
    'RUB': 'Российский рубль',
    'KZT': 'Тэнге'

}

root = Tk()
root.title("курс обмена валют к USD")
root.geometry("500x500")

Label(root, text='Введите код валюты').pack(pady=10, padx=10)
Popular_currencies = ['EUR', 'USD', 'JPY', 'GBP', 'AUD', 'RUB', 'KZT']
combobox = ttk.Combobox(root, values=Popular_currencies, state='readonly')
combobox.pack(pady=10, padx=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(pady=10, padx=10)
#entry = Entry(root)
#entry.pack()

Button(text = 'Получить курс обмена к доллару',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()

#
# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)