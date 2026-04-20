import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = '8671015752:AAEsttbvnv698gP3D3vO0TtkkrZCovSU2uY'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ Бот в сети! Мы победили ошибки!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
