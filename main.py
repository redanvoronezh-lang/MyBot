import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo

# Твой токен и инициализация
TOKEN = "8671015752:AAEsttbvnv698gP3D3vO0TtkkrZCovSU2uY"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Кнопки
    kb = [
        [types.InlineKeyboardButton(text="🚀 Играть", web_app=WebAppInfo(url="https://redanvoronezh-lang.github.io/MyBot/"))],
        [types.InlineKeyboardButton(text="📢 Канал", url="https://t.me/LapiGift")],
        [types.InlineKeyboardButton(text="🎧 Поддержка", url="https://t.me/LapiGift_sup_bot")]
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=kb)

    # Текст сообщения
    text = (
        "🎉 Привет, на связи команда **LapiGift** и теперь ты в нашей большой семье! 🎁\n\n"
        "Открывай кейсы и выигрывай лучшие NFT гифты!\n\n"
        "💰 Делись своей реферальной ссылкой с друзьями – и за каждого приведённого друга "
        "который сделает депозит ты получишь 5% от суммы их пополнений!\n"
        "Заинтересовало?\n\n"
        "🎁 Хочешь попробовать?\n"
        "Жми «Играть» и забирай свой приз!"
    )

    await message.answer(text, reply_markup=markup, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
