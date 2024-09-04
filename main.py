import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config
from images import router

import os
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, 'bot_logs.txt')
from logging.handlers import RotatingFileHandler
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5),
        logging.StreamHandler()
    ]
)

API_TOKEN = config.token
API_IMAGES = config.images
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
#register_handlers(dp)
dp.include_router(router)



@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Выбери свою профессию или найди картинку.")
    kb = InlineKeyboardBuilder()
    kb.button(text="Аналитик", callback_data="analyst")
    kb.button(text="Тестировщик", callback_data="tester")
    kb.button(text="Программист", callback_data="developer")
    kb.button(text="Найти картинку", callback_data="find_image")
    await message.answer("Выбери действие:", reply_markup=kb.as_markup())
@dp.callback_query(lambda x: x.data in ["analyst", "tester", "developer"])
async def profession_menu(callback: types.CallbackQuery):
    profession = callback.data
    await callback.message.edit_text(f"Выбери квалификацию для {profession.capitalize()}:")
    kb = InlineKeyboardBuilder()
    kb.button(text="Junior", callback_data=f"{profession}_junior")
    kb.button(text="Middle", callback_data=f"{profession}_middle")
    await callback.message.edit_reply_markup(reply_markup=kb.as_markup())
@dp.callback_query(lambda x: x.data.endswith("_junior") or x.data.endswith("_middle"))
async def program_info(callback: types.CallbackQuery):
    profession, qualification = callback.data.split("_")
    program_name = await generate_program_number(profession, qualification)
    await callback.message.answer(f"{program_name} для {profession.capitalize()} {qualification.capitalize()}.")
    await callback.answer()

async def generate_program_number(profession, qualification):
    program_numbers = {
        ("analyst", "junior"): "Программа обучения 1 - анализ данных для Джунов",
        ("analyst", "middle"): "Программа обучения 2 - анализ данных для Продвинутых ",
        ("tester", "junior"): "Программа обучения 3 - тестировщик начинающий",
        ("tester", "middle"): "Программа обучения 4 - тестировщик продвинутый",
        ("developer", "junior"): "Программа обучения 5 - разработчик с нуля",
        ("developer", "middle"): "Программа обучения 6 - разрабочик продвинутый"
    }
    key = (profession, qualification)
    if key in program_numbers:
        return program_numbers[key]
    else:
        return "Программа не найдена"

async def on_startup(dispatcher: Dispatcher):
    print("Бот запущен")
async def on_shutdown(dispatcher: Dispatcher):
    print("Бот остановлен")
#@dp.error_handler()
#async def error_handler(update: types.Update, exception: Exception):
#    print(f"Произошла ошибка: {exception}")
#    return True

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
if __name__ == '__main__':
    asyncio.run(main())
