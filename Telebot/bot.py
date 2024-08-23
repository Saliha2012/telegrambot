import telebot
from time import sleep

TOKEN = '7492596940:AAG_fND8XPD4ETwRvF9G7W7hcpvWZ9IbeFc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(comands=['start'])
def start(message):
   bot.send_message(message.chat.id, 'Привет, я бот. Чем могу помочь?')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == ("Привет"):
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == "ты можеш помочь":
        sleep(2)
        bot.send_message(message.from_user.id, 'Да, я могу тебе помочь')
    elif message.text == "Что сделал Касым Тыныстанов для Кыргызстана?": 
        sleep(2)
        bot.send_message(message.from_user.id, 'Касым Тыныстанов разработал основные принципы современной кыргызской орфографии, написал учебники, создал начальную грамматику, кыргызскую научную языковедческую терминологию. Он был одним из первых, кто приспособил кыргызский язык сначала к арабскому алфавиту, затем к латинскому и впоследствии к кириллице.')
    elif  message.text == "Кем был Александр Пушкин":
        sleep(2)
        bot.send_message(message.from_user.id, 'Александр Сергеевич Пушкин – величайший русский поэт, прозаик, драматург. Создатель русского литературного языка, родоначальник новой русской литературы. В качестве главных традиций русской литературы им утверждены гуманизм, народность, историзм, реализм, гражданственность.')
    elif  message.text == ("Спасибо"):
        bot.send_message(message.from_user.id, 'Пожалуйста! Если у вас есть ещё вопросы, не стесняйтесь обращаться')
    elif  message.text ==  ("Сколько тебе лет?"):  
        bot.send_message(message.from_user.id, 'я не знаю')              
    else: 
        bot.send_message(message.from_user.id, 'Я тебя не поняла.')

bot.infinity_polling()    