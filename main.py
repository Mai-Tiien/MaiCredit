import telebot
import random
import requests
import os
from bs4 import BeautifulSoup
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

@bot.message_handler(commands=['news'])
def help_news(message):
    url='https://www.liga.net/tag/frank-valter-shtaynmayer'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('a', class_='title')
    rand = random.choice(headlines)
    
    for x in rand: 
        file_head=('⚡ '+x.text.strip().replace('Штайнмайер', 'Май Тієн'))
        bot.reply_to(message, file_head)
            
    
@bot.message_handler(commands=['whoiam'])
def help_test(message):
    emp = ['Хохол', 'Байрактар', 'Байдон', 'Зєлєбобік', 'Окраинец', 'Броварска макака', 'Тернопівска хвойда', 
       'Порохобот', 'Салоїд', 'Майданутий', 'Байрактар', 'Русофоб', 'Натовец', 'Джавелін', 'Мазепонець', 'Кіця', 'Пес']
    emp_text = [
        ', що намагається воскресить Бандеру',
        ', що розробляє нову біологічну зброю',
        ', що ущемля рускоговарящего',
        ', що стріляє в Кубань',
        ', що змусив Пушилина з ДНР сісти на бутилку',
        ', що пічкає ядеркою птахів з Херосонського заповідника',
        ', що копає одеське метро',
        ', що погрожує ядеркою Росії',
        ', що викопав Чорне море',
        ', що особисто з Леніним писав Енеїду в 1917 році',
        ', що донбить бомбас-бімбас',
        ', що кожен ранок спалює російські прапори у львівських школах',
        ', що розбомбив Антонівський міст',
        ', що їсть російських немовлят на сніданок',
        ', що пришиває свастику на форму ЗСУ',
        ', що підірвав автівку Дугіни',
        ', що створив бандеро мобіль',
        ', що розробляє нано-екзоскелет у Броварській нанолабораторії',
        ', що розшатує санкцією проти Росії',
        ', що їбе путліра',
        ', що їбаше сіль',
        ', що ходить в публичну качалку',
        ', що дивиться Гей порно на українському перекладі',
        ', що підпалює петарди',
        ', що лайкає базовані українські меми'
    ]
    emp_list = emp[random.randint(0, 16)]
    emp_type = emp_text[random.randint(0, 25)]
    bot.send_message(message.chat.id, "First name: {test1}\nTitle: {test2}".format(test=message.chat.username, test1=message.from_user.first_name, test2='Ви '+emp_list+emp_type))     
      
@bot.message_handler(func=lambda message: True, content_types=['text'])
def help_command(message):
    if message.text == '/maicredit':
        rn = random.randint(1,4) 
        if rn >= 1:
            bot.reply_to(message, "Вітаю *{name}*, твій рейтинг піднявся на +{num} МайКредіт".format(name = message.from_user.first_name, num=random.randint(15, 200)), parse_mode="Markdown") 
        elif rn >= 2:    
            bot.reply_to(message, "Нажаль *{name}*, твій рейтинг впав на -{num} МайКредіт".format(name = message.from_user.first_name, num=random.randint(15, 100)), parse_mode="Markdown") 
        elif rn >= 3:  
            bot.reply_to(message, "Ти розчарувати великий вождь! *{name}* зробить пуля тобі в лоб вогонь! Ти втратив -{num} МайКредіт".format(name = message.from_user.first_name, num=random.randint(15, 100)), parse_mode="Markdown")

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
