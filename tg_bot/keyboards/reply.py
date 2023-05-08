from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Профиль')
        ],
        [
            KeyboardButton(text='О боте')
        ],
        [
            KeyboardButton(text='🔝Начать🔝')
        ]

    ],

    resize_keyboard=True

)


only_back = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Назад')
        ]
    ],

    resize_keyboard=True
)

start_now = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔝Начать сейчас🔝")
        ],
        [
            KeyboardButton(text='Назад')
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
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

upload_table = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
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

back_new_or_old = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ]

    ],
    resize_keyboard=True
)