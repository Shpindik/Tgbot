import asyncio, random
from functools import wraps
import kb, images
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

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
    await message.answer(
        kb.greet.format(name=message.from_user.first_name),
        reply_markup=kb.keyboard1
        )


@dp.callback_query(F.data == 'back_to_start')
async def process_back_to_start(callback: CallbackQuery):
    await callback.message.edit_text(
        kb.greet.format(name=callback.from_user.first_name),
        reply_markup=kb.keyboard1
    )


@dp.callback_query(F.data == 'big_button_1_pressed')
@check_old_answer('big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    random_images = random.sample(images.image_urls_nails, 4)
    media = [InputMediaPhoto(media=url) for url in random_images]
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(
        text='Работа - хуй повешать на ворота', reply_markup=kb.keyboard2
    )


@dp.callback_query(F.data == 'big_button_2_pressed')
@check_old_answer('big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Ноготь не воробей - тоже пизды получит', reply_markup=kb.keyboard3
        )


@dp.callback_query(F.data == 'big_button_2_1_pressed')
@check_old_answer('big_button_2_1_pressed')
async def process_button_2_1_press(callback: CallbackQuery):
    media = []
    for i, url in enumerate(images.image_urls_studio):
        media.append(InputMediaPhoto(media=url, caption=f"Image {i+1}"))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(
        kb.description, reply_markup=kb.keyboard4
        )


if __name__ == '__main__':
    asyncio.run(main())
