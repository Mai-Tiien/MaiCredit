import telebot
import time
import random

TOKEN = '5769001050:AAE6tjmtU0diovOjnf7rqGQ4p-oPxbGFj14'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def help_command(message):
    bot.send_message(message.chat.id, "Привіт, свої повідомлення сюди!")          

@bot.message_handler(commands=['id'])
def help_command(message):
    bot.send_message(message.chat.id, "Ваш ID: {test}".format(test=message.chat.id)) 
      
@bot.message_handler(func=lambda message: True, content_types=['text'])
def help_command(message):
    if message.text == '/maicredit':
        rn = random.randint(1,2) 
        if rn > 1:
            bot.reply_to(message, "Вітаю *{name}*, твій рейтинг піднявся на +{num} соціальних балів МайКредіт".format(name = message.chat.first_name, num=random.randint(15, 200)), parse_mode="Markdown") 
        elif rn < 2:    
            bot.reply_to(message, "Нажаль *{name}*, твій рейтинг впав на -{num} соціальних балів МайКредіт".format(name = message.chat.first_name, num=random.randint(15, 100)), parse_mode="Markdown")     
    elif message.text == 'Май Геній' or 'Май геній' or 'Слава Україні':
            bot.reply_to(message, "Вітаю *{name}*, ти отримуэш від вождя плюс {num} МайКредіт".format(name = message.chat.first_name, num=random.randint(15, 80)), parse_mode="Markdown") 
  

@bot.message_handler(func=lambda message: True, content_types=['photo'])
def echo_photo(message):
    img = message.photo[2].file_id
    bot.send_message(560831108, "Запит від @{name} десь там 👇".format(name=message.chat.username), parse_mode="Markdown")
    bot.send_photo(560831108, img, message.caption)

@bot.message_handler(func=lambda message: True, content_types=['video', 'video_note'])
def echo_video(message):
    bot.send_message(560831108, "Відправка відео від @{name} десь там 👇".format(name=message.chat.username), parse_mode="Markdown")
    bot.send_video(560831108, message.video.file_id, timeout=10)

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)
