import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from aiogram.types import ReplyKeyboardMarkup

from keyboards import kb1

# включаем логирование
logging.basicConfig(level=logging.INFO)

# создаем объект бота
API_TOKEN = config.token

bot = Bot(token=API_TOKEN)

# диспетчер
dp = Dispatcher()


# хэндлер на команду
@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне сообщение, и я его повторю")


@dp.message()
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if "привет" in msg_user:
        await message.answer(f"Привет-привет, {name}")
    elif "пока" == msg_user:
        await message.answer(f"Пока-пока, {name}")
    elif "ты кто" in msg_user:
        await message.answer(f"Я бот, {name}")
    elif "лиса" in msg_user:
        await message.answer(f"Смотри, что у меня есть, {name}", reply_markup=kb1)
    else:
        await message.answer(f"Я не знаю такого слова")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
