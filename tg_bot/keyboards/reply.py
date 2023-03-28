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


only_back = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='назад')
        ]
    ],

    resize_keyboard=True
)

