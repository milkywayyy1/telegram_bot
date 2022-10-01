from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CallbackContext, 
    Updater,
    CommandHandler,
    MessageHandler,
    Filters, 
    CallbackQueryHandler
)

from menu import main_menu_keyboard, course_menu_keyboard

def start (update: Update, context: CallbackContext):
    update.message.reply_text(
        'Welcome, {username}, Heyy, what do you want to know about?:'.format(
                username = update.effective_user.username
        ),
        reply_markup = main_menu_keyboard()
    )

def back (update: Update, context: CallbackContext):
    update.message.reply_text(
        'you are on main menu,  choose option:', 
        reply_markup = main_menu_keyboard()
    )

def course_menu_message(update: Update, context: CallbackContext):
    update.message.reply_text(
        'А вот и наши ребята:',
        reply_markup = course_menu_keyboard()
    )

def about_us(update: Update, context: CallbackContext):
    context.bot.send_sticker(
    chat_id = update.effective_chat.id, 
    sticker = 'CAACAgIAAxkBAAEF-QhjOEPxPaGcn7YcNWWdG5jpbnyDagACbAIAAladvQoqGV6cxNDenyoE'

    )
    update.message.reply_text(
        'Наш ментор-ДИН, его настоящее имя Динмухаммед Стамалиев, он утверждаетб что ему всегда 18, но мы думаем что он 2000  года.',
        
    )

# 42.87371196259388, 74.61994788677738

def location (update: Update, context: CallbackContext):
    msg = context.bot.send_message(
        chat_id = update.effective_chat.id, 
        text = 'Python — это скриптовый язык программирования. Он универсален, поэтому подходит для решения разнообразных задач и многих платформ, начиная с iOS и Android и заканчивая серверными ОС. Это интерпретируемый язык — он не компилируется, то есть до запуска представляет из себя обычный текстовый файл.А вот наш  адрес'
    )
    update.message.reply_location(
        longitude = 74.61994788677738,
        latitude = 42.87371196259388,
        reply_to_message_id = msg.message_id
    )

#aslan
def python_inline_menu(update: Update, context: CallbackContext):
    keyboard =[
        [  
            InlineKeyboardButton('Look at me!', callback_data = 'p_mentors'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Aslan ', 
        reply_markup = reply_markup
    )
#akmaral
def javascript_inline_menu(update: Update, context: CallbackContext):
    keyboard =[
        [
            InlineKeyboardButton('Look at me!', callback_data = 'j_mentors'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'I am Akmaral. I am 18 years old. I am student, I  study at Manas University. As for me, I interested in python, but not only, I am also good at sports. That is all. Good buy my friend ', 
        reply_markup = reply_markup
    )
#Madi
def madina_inline_menu(update: Update, context: CallbackContext):
    keyboard =[
        [  
            InlineKeyboardButton('Look at me!', callback_data = 'd_mentors')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'My name is Madina, I am 19 y.o., I study at University. My hobby is listening to music, and of course I like  to sleep.', 
        reply_markup = reply_markup
    )
def myrzaiym_inline_menu(update: Update, context: CallbackContext):
    keyboard =[
        [  
            InlineKeyboardButton('Look at me!', callback_data = 'de_mentors')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'My name is Meka, I am 14 y.o., I study at school. My hobby is listening to music, and of course I like  to sleep.', 
        reply_markup = reply_markup
    )
def kanimet_inline_menu(update: Update, context: CallbackContext):
    keyboard =[
        [  
            InlineKeyboardButton('Look at me!', callback_data = 'ka_mentors')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'I am Kani', 
        reply_markup = reply_markup
    )
    
def nurbolot_inline_menu(update: Update, context: CallbackContext):
    keyboard =[
        [  
            InlineKeyboardButton('Look at me!', callback_data = 'nu_mentors')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'I am Nurbolot', 
        reply_markup = reply_markup
    )
    
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    
    if query.data == 'p_mentors':
        query.message.reply_photo(
            'https://yandex.ru/images/search?pos=6&from=tabbar&img_url=http%3A%2F%2Faslan.com.au%2Fwp-content%2Fuploads%2F2021%2F05%2FASLAN-logo.png&text=aslan+name&rpt=simage&lr=10309', 
            caption = 'ASlan'
        )
    
    if query.data == 'j_mentors':
        query.message.reply_photo(
            'https://yandex.ru/images/search?pos=7&from=tabbar&img_url=http%3A%2F%2Ftextopics.ru%2Fimgbig%2Fname_25022.jpg&text=akmaral+name&rpt=simage&lr=10309', 
            caption = 'ты думал что здесь будет моя фотка?'
        )

    if query.data == 'd_mentors':
        query.message.reply_photo(
            'https://yandex.ru/images/search?pos=9&from=tabbar&img_url=http%3A%2F%2Fdzenpw.ru%2Fwp-content%2Fuploads%2Fd%2Fe%2Fd%2Fded5dd96faef55c60d03e8274fc01103.jpeg&text=madina+name&rpt=simage&lr=10309', 
            caption = 'Madina'
        )
    if query.data == 'dschedule':
        query.message.reply_text('lpluiillo')

    if query.data == 'de_mentors':
        query.message.reply_photo(
            'https://yandex.ru/images/search?pos=0&from=tabbar&img_url=http%3A%2F%2Flogos.flamingtext.com%2FName-Logos%2FMeka-design-china-name.png&text=meka+name+&rpt=simage&lr=10309', 
            caption = 'Meka'
        )
    if query.data == 'dschedule':
        query.message.reply_text('lpluiillo')
    if query.data == 'ka_mentors':
        query.message.reply_photo(
            'https://logos.flamingtext.com/Name-Logos/Peri-design-china-name.png', 
            caption = 'Kanimet'
        )
    if query.data == 'dschedule':
        query.message.reply_text('lpluiillo')
    if query.data == 'nu_mentors':
        query.message.reply_photo(
            'https://yandex.ru/images/search?p=1&text=%D0%BD%D1%83%D1%80%D0%B1%D0%BE%D0%BB%D0%BE%D1%82+%D0%B8%D0%BC%D1%8F&pos=57&rpt=simage&img_url=http%3A%2F%2Fsun9-14.userapi.com%2Fc625629%2Fv625629320%2F1d2b1%2FeeQjvT0jbJM.jpg&from=tabbar&lr=10309', 
            caption = 'Nurbolot'
        )
    if query.data == 'dschedule':
        query.message.reply_text('lpluiillo')


      



updater = Updater('5361469571:AAEFaNuJFVfnwcEJyiw_HPuV8dIJG-J6RRc')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('Guys'), 
    course_menu_message
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('ASLAN'), 
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('AKMARAL'), 
    javascript_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('MADINA'), 
    madina_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('MYRZAIYM'), 
    myrzaiym_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('KANIMET'), 
    kanimet_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('NURBOLOT'), 
    nurbolot_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('🔙'), 
    back
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('Course'), 
    location
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('Mentor'), 
    about_us
))


updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
