import telegram

def main_menu_keyboard():
    keyboard = (
        [
            [
                telegram.KeyboardButton('Guys'),
                telegram.KeyboardButton('Mentor'),
                telegram.KeyboardButton('Course')
            ]
        ]
    )
    return telegram.ReplyKeyboardMarkup(
        keyboard, recize_keyboard=True, one_time_keyboard=False
    )

def course_menu_keyboard():
    keyboard = (
        [
            [telegram.KeyboardButton('AKMARAL')], 
            [
                
                telegram.KeyboardButton('MADINA'),
                telegram.KeyboardButton('MYRZAIYM'),
                telegram.KeyboardButton('KANIMET'),
                telegram.KeyboardButton('ASLAN'),
                telegram.KeyboardButton('NURBOLOT'),
            ],
            [telegram.KeyboardButton('🔙')]
        ]
    )
    return telegram.ReplyKeyboardMarkup(
        keyboard, recize_keyboard=True, one_time_keyboard=False
    )