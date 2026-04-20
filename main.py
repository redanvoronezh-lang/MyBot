import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo

# Твои данные
TOKEN = '8671015752:AAEsttbvnv698gP3D3vO0TtkkrZCovSU2uY'
APP_URL = 'https://redanvoronezh-lang.github.io/MyBot/'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    # Создаем кнопку под полем ввода
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🎁 Открыть LapiGift", web_app=WebAppInfo(url=APP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n\nДобро пожаловать. Нажми на кнопку ниже, чтобы запустить приложение:",
        reply_markup=markup
    )

async def main():
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
