from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup

greet = "Привет, {name}! Я бот Алёна. Делаю записи на маникюр ☺️"
menu = "📍 Главное меню"

big_button_1 = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 1', callback_data='big_button_1_pressed')
big_button_2 = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 2', callback_data='big_button_2_pressed')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)

big_button_3 = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 3', callback_data='big_button_3_pressed')
big_button_4 = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 4', callback_data='big_button_4_pressed')

keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_3],
                     [big_button_4]]
)

big_button_5 = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 5', callback_data='big_button_5_pressed')
big_button_6 = InlineKeyboardButton(text='БОЛЬШАЯ КНОПКА 6', callback_data='big_button_6_pressed')

keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_5],
                     [big_button_6]]

)