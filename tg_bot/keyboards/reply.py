from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='профиль')
        ],
        [
            KeyboardButton(text='О боте')
        ],
        [
            KeyboardButton(text='🔝начать🔝')
        ]

    ],

    resize_keyboard=True

)
