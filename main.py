import telebot
import random
import sqlite3

connect = sqlite3.connect('users.db', check_same_thread=False)
cursor = connect.cursor()

def db_table_val(user_id: int, user_name: str, balance: int):
    cursor.execute('INSERT OR REPLACE INTO login (user_id, user_name, balance) VALUES (?, ?, ?)',
                   (user_id, user_name, balance))
    connect.commit() 

TOKEN = '5769001050:AAEMultrMrM1V0E_MB5Mn0sfQA_A6QYfTME'
bot = telebot.TeleBot(TOKEN)
bot.can_join_groups = True


@bot.message_handler(commands=['start'])
def help_start(message):
    bot.send_message(message.chat.id, "Ведіть запит команд, якій буде виконувати бот!")              
    
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


def get_coin(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM login WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    else:
        return 0  

@bot.message_handler(commands=['maicredit'])
def maicredit_command(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    chat_id = message.chat.id
    rn = random.randint(1, 6)

    if rn == 1:
        with open('image/death.png', 'rb') as photo1:
            bale = random.randint(15, 500)
            current_balance = get_coin(us_id)
            new_balance = current_balance - bale
            db_table_val(user_id=us_id, user_name=us_name, balance=new_balance)
            text1 = "*{name}*, ти розчарувати великий вождь! Святослав зробить пуля тобі в лоб вогонь! Ти втратив -{num} МайКредіт".format(name=message.from_user.first_name, num=bale)
            bot.send_photo(chat_id, photo1, caption=text1, parse_mode="Markdown")

    if rn == 2:
        with open('image/down.png', 'rb') as photo2:
            bale = random.randint(15, 500)
            current_balance = get_coin(us_id)
            new_balance = current_balance - bale
            db_table_val(user_id=us_id, user_name=us_name, balance=new_balance)
            text2 = "Нажаль *{name}*, твій рейтинг впав на -{num} МайКредіт".format(name=message.from_user.first_name, num=bale)
            bot.send_photo(chat_id, photo2, caption=text2, parse_mode="Markdown")

    if rn >= 3:
        with open('image/up.png', 'rb') as photo3:
            bale = random.randint(15, 400)
            current_balance = get_coin(us_id)
            new_balance = current_balance + bale
            db_table_val(user_id=us_id, user_name=us_name, balance=new_balance)
            text3 = "Вітаю *{name}*, твій рейтинг піднявся на +{num} МайКредіт".format(name=message.from_user.first_name, num=bale)
            bot.send_photo(chat_id, photo3, caption=text3, parse_mode="Markdown")

@bot.message_handler(commands=['shoot'])
def shoot_command(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    chat_id = message.chat.id
    target_id = message.reply_to_message.from_user.id if message.reply_to_message else None
    target_name = message.reply_to_message.from_user.first_name if message.reply_to_message else None
    
    if not target_id:
        bot.reply_to(message, "Для використання цієї команди, дайте відповідь на повідомлення користувача, якого ви хочете підстрелити.")
        return
    
    if us_id == target_id:
        bot.reply_to(message, "*{us_name}*, ти не можеш себе вистрелити.", parse_mode="Markdown")
        return
    
    chance = random.randint(1, 9)  

    if chance >= 3:
        with open('image/shot.png', 'rb') as photo5:
            bale = random.randint(15, 200)
            current_balance = get_coin(us_id)
            new_balance = current_balance - bale
            db_table_val(user_id=us_id, user_name=us_name, balance=new_balance)
            text = "Поздравляю, *{name}*! Ви підстрелили *{user}* і відібрали у нього -{num} МайКредит".format(name=message.from_user.first_name, user=target_name, num=bale)
            bot.send_photo(chat_id, photo5, caption=text, parse_mode="Markdown")
            
            target_balance = get_coin(target_id)
            target_new_balance = max(0, target_balance - bale)  
            db_table_val(user_id=target_id, balance=target_new_balance)
    else:
        with open('image/miss.png', 'rb') as photo6:
            text = "Нажаль, *{name}*, ви схибили і не попали в *{user}*.".format(name=message.from_user.first_name, user=target_name)
            bot.send_photo(chat_id, photo6, caption=text, parse_mode="Markdown")


@bot.message_handler(commands=['balance'])
def bl_command(message):
    con = sqlite3.connect('users.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT user_name, balance FROM login ORDER BY balance DESC')
    rows = cursorObj.fetchall()
    con.close() 

    if len(rows) > 0:
        balance_info = "\n".join(f"💸 {row[0]}, має {row[1]} МайКредіт" for row in rows)
    else:
        balance_info = "На жаль, немає інформації про баланс користувачів."

    bot.reply_to(message, balance_info)

@bot.message_handler(commands=['sneak'])
def sneak_command(message):
    from_user_id = message.from_user.id
    chat_user_id = message.chat.id
    from_user_name = message.from_user.first_name

    con = sqlite3.connect('users.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT user_id, user_name, balance FROM login WHERE user_id != ?', (from_user_id,))
    rows = cursorObj.fetchall()

    if len(rows) == 0:
        bot.reply_to(message, "На жаль, немає інших користувачів для крадіжки МайКредіт.")
        return

    to_user_id, to_user_name, to_user_balance = random.choice(rows)

    if random.randint(1, 2) == 1:
        with open('image/joker.png', 'rb') as photo4:
            stolen_amount = random.randint(1, to_user_balance)
            joke = f"*{from_user_name}* вкрав {stolen_amount} МайКредіт у *{to_user_name}*! 😈"
            bot.send_photo(chat_user_id, photo4, caption=joke, parse_mode="Markdown")

    else:
        bot.reply_to(message, f"*{from_user_name}*, ви намагалися вкрасти МайКредіт у *{to_user_name}*, але вас впіймали! 🚓", parse_mode="Markdown")

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print("Помилка: ", e)