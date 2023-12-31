import asyncio
from functools import wraps
import kb
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import  Message, CallbackQuery

router = Router()


bot = Bot(token='6643070029:AAEoeFbuqG3730zg6Lx9M36AeKLbLhuAORA')
dp = Dispatcher()
dp.include_router(router)
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

def check_old_answer(text):
    def decorator(func):
        @wraps(func)
        async def wrapper(callback: CallbackQuery):
            if callback.message.text != text:
                await func(callback)

            await callback.answer()

        return wrapper

    return decorator


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(kb.greet.format(name=message.from_user.first_name), reply_markup=kb.keyboard1)


@dp.callback_query(F.data == 'big_button_1_pressed')
@check_old_answer('big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.answer(text='Была нажата БОЛЬШАЯ КНОПКА 1',reply_markup=kb.keyboard2)

if __name__ == '__main__':
    asyncio.run(main())
 