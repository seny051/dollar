import aiogram
from aiogram import types
def startt():
    start_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    my_port = types.KeyboardButton(text="Мой портфель💼")
    valut = types.KeyboardButton(text="Курс валют📈")
    start_key.add(valut, my_port)
    return start_key

def duo():
    var = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kript = types.KeyboardButton(text="Валюта 💲")
    valut = types.KeyboardButton(text="Криптовалюта ₿")
    back = types.KeyboardButton(text="Назад🔙")
    var.add(kript, valut, back)
    return var

def case():
    c=types.ReplyKeyboardMarkup(resize_keyboard=True)
    val= types.KeyboardButton(text="Выбрать валюты")
    kol= types.KeyboardButton(text="Выбрать количество валют")
    sost= types.KeyboardButton(text="Узнать состояние моего портфеля")
    back = types.KeyboardButton(text="Назад🔙")
    c.add(sost,kol,val,back)
    return c

