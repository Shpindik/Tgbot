from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup, WebAppInfo


greet = 'Привет, {name}! Я бот Алёна. Делаю записи на маникюр ☺️'
menu = '📍 Главное меню'
description = 'Вы перешли в фанклуб ранеток!'

back = InlineKeyboardButton(text='Назад', callback_data='back_to_start')

big_button_1 = InlineKeyboardButton(text='Посмотреть работы', callback_data='big_button_1_pressed')
big_button_2 = InlineKeyboardButton(text='Записаться на ноготочки', callback_data='big_button_2_pressed')
big_button_2_1 = InlineKeyboardButton(text='О себе', callback_data='big_button_2_1_pressed')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2],
                     [big_button_2_1]]
)
big_button_3 = InlineKeyboardButton(text='Instagram', url='https://www.youtube.com/watch?v=ZVqRV5LwaRI', callback_data='big_button_3_pressed')
big_button_4 = InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/watch?v=ZVqRV5LwaRI', callback_data='big_button_4_pressed')

keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_3],
                     [big_button_4],
                     [back]]
)

big_button_5 = InlineKeyboardButton(text='БОЯРЕ(В работе)', callback_data='big_button_5_pressed')
big_button_6 = InlineKeyboardButton(text='Записаться через Дикиди', web_app=WebAppInfo(url='https://dikidi.ru/1295192'))

keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_5],
                     [big_button_6],
                     [back]]

)

big_button_7 = InlineKeyboardButton(text='////', url='https://yandex.ru/maps/org/neon_nails_studio/238892078116/?ll=37.645276%2C55.775191&z=16.67', callback_data='big_button_7_pressed')

keyboard4 = InlineKeyboardMarkup(inline_keyboard=[[big_button_7],
                                                  [back]])
