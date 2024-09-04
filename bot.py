import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import asyncio

# Замените 'YOUR_BOT_TOKEN' на ваш реальный токен бота
bot = Bot(token='6006413596:AAGd-9s1VOM1uQGs8FU1OrmmXMN9neMzrSo')
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! ")


async def on_startup(bot):
    await bot.set_webhook(
        url=f"https://your-pythonanywhere-username.pythonanywhere.com/{bot.token}"
    )
async def on_shutdown(bot):
    await bot.delete_webhook()

async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")



if __name__ == '__main__':
    asyncio.run(main())

