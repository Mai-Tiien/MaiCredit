import telebot
import random
import requests
import os
import sqlite3
from bs4 import BeautifulSoup
from flask import Flask, request

connect = sqlite3.connect('users.db', check_same_thread=False)
cursor = connect.cursor()

def db_table_val(user_id: int, user_name: str, balance: int):
    cursor.execute('INSERT OR REPLACE INTO login (user_id, user_name, balance) VALUES (?, ?, ?)',
                   (user_id, user_name, balance))
    connect.commit() 

APP_NAME='https://maicredit.herokuapp.com/'
TOKEN = '5769001050:AAH9LaUlCtOfEEQyjmJprXXgfSg1D65bSB4'
bot = telebot.TeleBot(TOKEN)
bot.can_join_groups = True


server = Flask(__name__)

@bot.message_handler(commands=['start'])
def help_start(message):
    bot.send_message(message.chat.id, "Ведіть запит команд, якій буде виконувати бот!")          

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
    bot.send_message(message.chat.id, "Name: {test1}\nTitle: {test2}".format(test=message.chat.username, test1=message.from_user.first_name, test2='Ви '+emp_list+emp_type))     

def get_coin():
    pow = sqlite3.connect('users.db')
    cursorPow = pow.cursor()
    cursorPow.execute('SELECT user_name, balance FROM login ORDER BY balance DESC')
    rows = cursorPow.fetchall()
    for row in rows:
        coin = row[1]
    return coin

@bot.message_handler(commands=['bavovna']) 
def bavovna_command(message):
    url = 'https://www.unn.com.ua/uk/search?q=%D0%B1%D0%B0%D0%B2%D0%BE%D0%B2%D0%BD%D0%B0'
    res = requests.get(url)

    rd_soup = BeautifulSoup(res.text, 'html.parser')
    bv1 = rd_soup.find_all('div', class_='b-news-search-title')
    bv2 = random.choice(bv1)

    for text_bv in bv2:
        bavov = '💣 ' + text_bv.text
        bot.reply_to(message, bavov)
      
@bot.message_handler(content_types=['text'])
def maicredit_command(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    rn = random.randint(1,6)
    
    if message.text == '/maicredit':
        if rn == 1:
            bale = random.randint(15, 200)
            db_table_val(user_id=us_id, user_name=us_name, balance=get_coin() - bale)
            bot.reply_to(message, "*{name}*, ти розчарувати великий вождь! Святослав зробить пуля тобі в лоб вогонь! Ти втратив -{num} МайКредіт".format(name = message.from_user.first_name, num=bale), parse_mode="Markdown")
            
        if rn == 2:
            bale = random.randint(15, 100)
            db_table_val(user_id=us_id, user_name=us_name, balance=get_coin() - bale)
            bot.reply_to(message, "Нажаль *{name}*, твій рейтинг впав на -{num} МайКредіт".format(name = message.from_user.first_name, num=bale), parse_mode="Markdown") 
        
        if rn >= 3:
            bale = random.randint(15, 250)
            db_table_val(user_id=us_id, user_name=us_name, balance=get_coin() + bale)
            bot.reply_to(message, "Вітаю *{name}*, твій рейтинг піднявся на +{num} МайКредіт".format(name = message.from_user.first_name, num=bale), parse_mode="Markdown") 
    elif message.text == 'Май геній':
        bale = random.randint(15, 250)
        db_table_val(user_id=us_id, user_name=us_name, balance=get_coin() + bale)
        bot.reply_to(message, "Вітаю *{name}*, ти отримаєш від вождя +{num} МайКредіт".format(name = message.from_user.first_name, num=bale), parse_mode="Markdown") 
    
        
@bot.message_handler(commands=['balance']) 
def bl_command(message):
    con = sqlite3.connect('users.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT user_name, balance FROM login ORDER BY balance DESC')
    rows = cursorObj.fetchall()
    with open("out.txt", "w", encoding='utf-8') as file:
        for row in rows:    
            file.write("💸 {row1}, має {row2} МайКредіт\n".format(row1 = row[0], row2 = row[1])) 
    f = open('out.txt', 'r', encoding='utf-8')
    a = f.read
    b = a()
    bot.reply_to(message, b)

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
