import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random
from aiogram.types import ReplyKeyboardMarkup
# Включаем логирование
logging.basicConfig(level=logging.INFO)
# Создаем объект бота
API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()
# Определяем кнопки
button1 = types.KeyboardButton(text="start")
button2 = types.KeyboardButton(text="Стоп")
button3 = types.KeyboardButton(text="Инфо")
button4 = types.KeyboardButton(text="Покажи лису")
button5 = types.KeyboardButton(text="Закрыть")
# Создаем клавиатуру
keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]
kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
# Хэндлер на команду /start
@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне сообщение, и я его повторю", reply_markup=kb1)
@dp.message()
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if "привет" in msg_user:
        await message.answer(f"Привет-привет, {name}", reply_markup=kb1)
    elif "пока" == msg_user:
        await message.answer(f"Пока-пока, {name}", reply_markup=kb1)
    elif "ты кто" in msg_user:
        await message.answer(f"Я бот, {name}", reply_markup=kb1)
    elif "лиса" in msg_user:
        await message.answer(f"Смотри, что у меня есть, {name}", reply_markup=kb1)
    else:
        await message.answer(f"Я не знаю такого слова", reply_markup=kb1)
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
