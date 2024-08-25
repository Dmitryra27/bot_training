import logging
from aiogram import Router, types, F
import requests
import config
API_IMAGES = config.images
# Создаем объект Router для обработки сообщений
router = Router()
# Обработчик кнопки "Найти картинку"
@router.callback_query(F.data == 'find_image')
async def find_image(callback: types.CallbackQuery):
    await callback.message.answer("Отправь мне любое слово, и я найду для тебя картинку по этому слову.")
    await callback.answer()
    logging.info("Обработчик find_image работу закончил")
# Обработчик текстовых сообщений
@router.message()
async def get_image(message: types.Message):
    await message.reply('Пожалуйста, отправьте мне слово для поиска картинки.')
    query = message.text
    logging.info(f"Обработчик get_image вызван, сообщение от пользователя: {query}")
    response = requests.get(f'https://api.unsplash.com/search/photos?query={query}&client_id={API_IMAGES}')
    if response.status_code == 200:
        image_url = response.json()['results'][0]['urls']['regular']
        await message.answer_photo(image_url)
    else:
        await message.answer("Извините, не удалось найти картинку по вашему запросу.")
def register_handlers(dp):
    dp.include_router(router)

