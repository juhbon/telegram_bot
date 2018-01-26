import telebot
from datetime import datetime
from telebot import types
from random import randint, seed
import re

token = '' # here's your token
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup()
markup.row('rand')
markup.row('/help','/rand')

# Regular expression for random message
retest = '^[Бб]от?[^\d] (скажи|отреагируй|напиши|реагируй|пиши|ответь)*'
# retest = '^[Bb]ot?[^\d] (say|comment|write)*'

archive = []

# Function for updating archive, from which random message taken
def updating():
    try:
        for line in open('some.txt'):
            archive.append(line)
    except:
        file = open('some.txt','w')
        file.write('Will it work? Nope\n')
        file.write('Just nope')
        file.close()

updating()

# First launch
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Че надо')

# Reply to "help"
@bot.message_handler(commands=['help'])
def nontest(message):
    bot.send_message(message.chat.id,'Ничем не могу помочь. Хотя нет, могу. Можно вывести случайное сообщение фразой "бот, скажи\отреагируй (и что угодно далее)".')

# Random message
@bot.message_handler(commands=['rand'])
def nontest(message):
    #random = randint(len(open('some.txt'). ))
    #seed(message)
    bot.send_message(message.chat.id, archive[randint(0,len(archive)-1)])

# Checking for repost from 2ch public channel
@bot.message_handler(content_types=["text", "sticker", "video", "photo", "audio"], func=lambda msg: msg.forward_from_chat and msg.forward_from_chat.id == -1001009232144)
def bidlo(message):
    bot.send_message(message.chat.id, "Вы быдло, сэр.")

# Write message to file or getting random message
@bot.message_handler()  #content_types=['text'])
def communication(message):
    if re.match(retest, message.text) is not None:
        nontest(message)
    else:
        if (len(message.text) > 500):
            try:
                open("some.txt", 'a+').write(message.text)
                open("some.txt", 'a+').write('\n')
                updating()
            except:
                nontest(message)

# Make bot working always after start
# Not recommended for servers due to amount of requests  
bot.polling(none_stop=True)
