import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery, LinkPreviewOptions
from aiogram.enums import ParseMode
from keyboards import get_business_keyboard

TOKEN = os.getenv("TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    photo = FSInputFile("media/business1.jpeg")
    await message.answer_photo(
        photo=photo,
        caption="<b>Здравствуйте!</b> 👋 \n\nЯ бот, который " \
        "поможет вам создать свой бизнес с нуля и получить первые " \
        "продажи в течение 30 дней. \n\n" \
        "<b>Если вы хотите узнать больше о нашем курсе, " \
        "нажмите на кнопку ниже.</b>",
        parse_mode="HTML",
        reply_markup=get_business_keyboard()
    )

@dp.callback_query(F.data == "enroll_business")
async def enroll_business(callback: CallbackQuery):
    text = (
        '*Замечательно\\!* Вот ссылка на наше '
        '[приложение](https://www.beboss.ru/start/how)\\.'
    )
    photo = FSInputFile("media/business2.png")
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        link_preview_options=LinkPreviewOptions(is_disabled=True),
        )

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
