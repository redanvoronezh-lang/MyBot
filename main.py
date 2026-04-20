import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="8671015752:AAEsttbvnv698gP3D3vO0TtkkrZCovSU2uY")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(m: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Играть", web_app=WebAppInfo(url="https://redanvoronezh-lang.github.io/MyBot/"))],
        [InlineKeyboardButton(text="📢 Канал", url="https://t.me/LapiGift")],
        [InlineKeyboardButton(text="🎧 Поддержка", url="https://t.me/LapiGift_sup_bot")]
    ])
    
    text = (
        "🎉 Привет, на связи команда LapiGift и теперь ты в нашей большой семье! 🎁\n\n"
        "Открывай кейсы и выигрывай лучшие NFT гифты!\n\n"
        "💰 Делись своей реферальной ссылкой с друзьями – и за каждого приведённого друга "
        "который сделает депозит ты получишь 5% от суммы их пополнений!\n"
        "Заинтересовало?\n\n"
        "🎁 Хочешь попробовать?\n"
        "Жми «Играть» и забирай свой приз!"
    )
    
    await m.answer(text, reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
