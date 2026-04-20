import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, PreCheckoutQuery, LabeledPrice

TOKEN = '8671015752:AAEsttbvnv698gP3D3vO0TtkkrZCovSU2uY'
APP_URL = 'https://redanvoronezh-lang.github.io/MyBot/'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="🎁 Открыть LapiGift", web_app=WebAppInfo(url=APP_URL))]],
        resize_keyboard=True
    )
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=markup)

@dp.message(F.web_app_data.data == "pay_stars")
async def create_invoice(message: types.Message):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Пополнение",
        description="Зачисление 10 💎",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=10)],
        payload=f"refill_{message.from_user.id}"
    )

@dp.pre_checkout_query()
async def process_pre_checkout(query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(query.id, ok=True)

@dp.message(F.successful_payment)
async def success_pay(message: types.Message):
    await message.answer(f"✅ Зачислено: {message.successful_payment.total_amount} 💎")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
