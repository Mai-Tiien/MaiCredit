import telebot
import random
import os
import time
from flask import Flask, request

APP_NAME='https://maicredit.herokuapp.com/'
TOKEN = '5769001050:AAE6tjmtU0diovOjnf7rqGQ4p-oPxbGFj14'
bot = telebot.TeleBot(TOKEN)
bot.can_join_groups = True

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def help_start(message):
    bot.send_message(message.chat.id, "Привіт, свої повідомлення сюди!")          

@bot.message_handler(commands=['id'])
def help_command(message):
    bot.send_message(message.chat.id, "Ваш ID: {test}".format(test=message.chat.id)) 
    
@bot.message_handler(commands=['whoiam'])
def help_test(message):
    bot.send_message(message.chat.id, "Group: {test}\nFirst name: {test1}\nTitle: {test2}".format(test=message.from_user.username, test1=message.from_user.first_name, test2=message.from_user.title))     
      
@bot.message_handler(func=lambda message: True, content_types=['text'])
def help_command(message):
    if message.text == '/maicredit':
        rn = random.randint(1,2) 
        if rn > 1:
            bot.reply_to(message, "Вітаю *{name}*, твій рейтинг піднявся на +{num} соціальних балів МайКредіт".format(name = message.from_user.first_name, num=random.randint(15, 200)), parse_mode="Markdown") 
        elif rn < 2:    
            bot.reply_to(message, "Нажаль *{name}*, твій рейтинг впав на -{num} соціальних балів МайКредіт".format(name = message.from_user.first_name, num=random.randint(15, 100)), parse_mode="Markdown")     
    elif message.text == 'Май Геній' or 'Май геній' or 'Слава Україні':
            bot.reply_to(message, "Вітаю *{name}*, ти отримуэш від вождя плюс {num} МайКредіт".format(name = message.from_user.first_name, num=random.randint(15, 80)), parse_mode="Markdown") 


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "Hello, world!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_NAME + TOKEN)
    return "Hello, world!", 200    

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
