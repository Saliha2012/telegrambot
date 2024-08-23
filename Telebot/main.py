import telebot

# Укажите ваш токен бота
TOKEN = '7510185286:AAGFYESe4nH7onBXCU7bNOlBGNtPp3AJAkM'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Dior')
    button2 = telebot.types.KeyboardButton('')
    button3 = telebot.types.KeyboardButton('Help')
    button4 = telebot.types.KeyboardButton('Audio') 
    keyboard.add(button1, button2, button3, button4)

    # Отправка приветственного сообщения с клавиатурой
    bot.send_message(message.chat.id, "Welcome to my shopping bot! Please choose an option:", reply_markup=keyboard)

# Обработчик нажатия на кнопку "Nike"
@bot.message_handler(func=lambda message: message.text == 'gucci')
def send_Dior(message):
    # Отправка изображения
    with open('image1.webp', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first shirt. Dior!")

# Обработчик нажатия на кнопку "Video-Nike"
@bot.message_handler(func=lambda message: message.text == 'Video-Dior')
def send_video_nike(message):
    # Отправка видео
    with open('Dior - COMMERCIAL - 2024 -  JUST DO IT - AI ENTERTAINMENT.mp4', 'rb') as vid:
        bot.send_video(message.chat.id, vid, caption="Это видео.")

# Обработчик нажатия на кнопку "Help"
@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):
    # Отправка сообщения со справкой
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")

# Обработчик нажатия на кнопку "Audio"
@bot.message_handler(func=lambda message: message.text == 'Audio')
def send_audio(message):
    # Отправка аудиосообщения
    with open('АДЛИН - No Love.mp3', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")

# Запуск бота
bot.polling()