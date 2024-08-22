import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config
logging.basicConfig(level=logging.INFO)
API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Выбери свою профессию:")
    kb = InlineKeyboardBuilder()
    kb.button(text="Аналитик", callback_data="analyst")
    kb.button(text="Тестировщик", callback_data="tester")
    kb.button(text="Программист", callback_data="developer")
    await message.answer("Выбери профессию:", reply_markup=kb.as_markup())
@dp.callback_query(lambda x: x.data.startswith("analyst"))
async def analyst_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Выбери квалификацию:")
    kb = InlineKeyboardBuilder()
    kb.button(text="Junior", callback_data="analyst_junior")
    kb.button(text="Middle", callback_data="analyst_middle")
    await callback.message.edit_reply_markup(reply_markup=kb.as_markup())
@dp.callback_query(lambda x: x.data.startswith("tester"))
async def tester_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Выбери квалификацию:")
    kb = InlineKeyboardBuilder()
    kb.button(text="Junior", callback_data="tester_junior")
    kb.button(text="Middle", callback_data="tester_middle")
    await callback.message.edit_reply_markup(reply_markup=kb.as_markup())
@dp.callback_query(lambda x: x.data.startswith("developer"))
async def developer_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Выбери квалификацию:")
    kb = InlineKeyboardBuilder()
    kb.button(text="Junior", callback_data="developer_junior")
    kb.button(text="Middle", callback_data="developer_middle")
    await callback.message.edit_reply_markup(reply_markup=kb.as_markup())
@dp.callback_query(lambda x: x.data.endswith("_junior"))
async def junior_program(callback: types.CallbackQuery):
    profession, _ = callback.data.split("_")
    program_name = await generate_program_number(profession, "junior")
    await callback.message.answer(f"{program_name} для {profession} Junior.")
@dp.callback_query(lambda x: x.data.endswith("_middle"))
async def middle_program(callback: types.CallbackQuery):
    profession, _ = callback.data.split("_")
    program_name = await generate_program_number(profession, "middle")
    await callback.message.answer(f"{program_name} для {profession} Middle.")
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
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
