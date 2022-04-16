from typing import Set
import aiogram
import sqlite3
from bs4 import BeautifulSoup
import requests
import lxml
import starts
import sqlb
import parsing
from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keyboard

bot = Bot(token="5292539763:AAGOlnQfykqYpd3MUPj-IrsXX3sWsyYgYw4")

dp = Dispatcher(bot, storage=MemoryStorage())

class seting(StatesGroup):
    set_lan = State()

class setting2(StatesGroup):
    set_lan2 = State()

with open ('test.txt', 'r') as f:
  old_data = f.read()
new_data = old_data.replace('starts.a', str((int(starts.a)+1)))
with open ('test.txt', 'w') as f:
  f.write(new_data)

@dp.message_handler(commands='start')
async def lang(message: types.Message):
  if starts.a=='1':
      sqlb.create()
  if sqlb.chest(message) is None:
    sqlb.add_id(message)
  elif sqlb.chest(message)[0] == message.chat.id:
   await message.answer("Привет, я бот, помогающий тебе в заработке на валютной бирже. С моей помощью ты можешь смотреть курс валют, а также следить за состоянием своего портфеля.", reply_markup=keyboard.startt())

@dp.message_handler(lambda message: message.text=="Курс валют📈")
async def choise(message: types.Message):
  await message.answer("Выберите валюту или криптовалюту",reply_markup=keyboard.duo())

@dp.message_handler(lambda message:message.text=="Валюта 💲")
async def vall(message: types.Message):
  await message.answer(parsing.kurs())

@dp.message_handler(lambda message:message.text=="Криптовалюта ₿")
async def kripta(message: types.Message):
  pass

@dp.message_handler((lambda message:message.text=="Назад🔙"))
async def back(message: types.Message):
  await message.answer("Вы вернулись в главное меню.",reply_markup=keyboard.startt())

@dp.message_handler((lambda message:message.text=="Мой портфель💼"))
async def case(message: types.Message):
 await message.answer("Портфель", reply_markup=keyboard.case())
 global n
 n=[sqlb.check(message),sqlb]

@dp.message_handler(lambda message:message.text=="Выбрать валюты")
async def value(message: types.Message):
    await message.answer(f"Введите название валют через запятую: \n {parsing.name_val()}")
    await seting.set_lan.set()

@dp.message_handler(state=seting.set_lan)
async def f(message: types.Message, state: FSMContext):
    global n
    n[0] = [message.text]
    await message.answer("Валюты выбрана")
    await state.finish()

@dp.message_handler(lambda message:message.text=="Выбрать количество валют")
async def count(message: types.Message):
    await message.answer(f"Введите количтво валют, в таком же порядке, как вы вводили валюты(через запятую)")
    await setting2.set_lan2.set()

@dp.message_handler(state=setting2.set_lan2)
async def f(message: types.Message, state: FSMContext):
    global n
    n[1] = [message.text]
    await message.answer('Кол-во валюты выбрано')
    await state.finish()
n=[[0],[0]]

@dp.message_handler(lambda message:message.text=="Узнать состояние моего портфеля")
async def har(message: types.Message):
    if n[0][0]!=0 and n[1][0]!=0:
     sqlb.value(str(n[0][0]).split(","),str(n[1][0]).split(","),message.chat.id)
     await message.answer(f"{parsing.rub(message.chat.id)} RUB")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
