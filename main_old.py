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
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне сообщение, и я его повторю.")

@dp.message(Command("салют"))
async def command_salut(message: types.Message):
    await message.answer("Салют! Я эхобот на aiogram 3. Отправь мне сообщение, и я его повторю.")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
