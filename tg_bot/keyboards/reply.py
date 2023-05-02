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

start_now = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔝начать сейчас🔝")
        ],
        [
            KeyboardButton(text='назад')
        ]
    ],

    resize_keyboard=True
)


new_or_old_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Использовать старый список")
        ],
        [
            KeyboardButton(text="Создать новый список слов")
        ],
        [
            KeyboardButton(text="назад")
        ]
    ],
    resize_keyboard=True
)

upload_table = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="назад")
        ]

    ],
    resize_keyboard=True
)

choose_male = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мужчина")
        ],
        [
            KeyboardButton(text="Женщина")
        ],
        [
            KeyboardButton(text="Не указывать")
        ]
    ],
    resize_keyboard=True
)
