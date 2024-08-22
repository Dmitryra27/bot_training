#Fox
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config

logging.basicConfig(level=logging.INFO)
API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Хай! Я бот на aiogram. Отправь мне сообщение, и я его повторю.")

@dp.message(Command("привет"))
async def echo(message: types.Message):
    await message.answer("Хай! Я бот на aiogram. Отправь мне сообщение, и я его повторю.")

@dp.message(Command("info"))
async def echo(message: types.Message):
    await message.answer("Данный бот предоставляет простую функцию: получить дублирование своего ответа")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)
    print('Бот запущен')
if __name__ == '__main__':
    asyncio.run(main())
