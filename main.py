import telebot
import os
import random
import sqlite3



bot = telebot.TeleBot('1630299681:AAETYUXFhczaZ2gAozn_3_Iqgq4-WX6o3js')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, " + " " + message.from_user.first_name + "! " 
                                        "\nВот что я могу: \n/pic -отпраить картику с котиками \n /replay - узнать своё последнее сообщение ")
@bot.message_handler(commands=['pic'])
def send_pic(message):
    bot.reply_to(message, "Хех, На")
    photo = open('photo/' + random.choice(os.listdir('photo')), 'rb')
    bot.send_photo(message.from_user.id, photo, caption=' Если хочешь ещё - жми /pic')



@bot.message_handler(content_types=['text'])
def add_in_table(message):
    print(message.text)

    if message.text != "/replay" and "/pic":
        sql_conn = sqlite3.connect('ProfileUser')
        cursor = sql_conn.cursor()

        user_message = message.text
        user_id = message.from_user.id

        query_check = '''SELECT * FROM UsersLastEntry WHERE id_user=?'''
        query_add = '''INSERT INTO UsersLastEntry (text, id_user) VALUES (?, ?)'''
        query_update = '''UPDATE UsersLastEntry SET text = ? WHERE id_user = ?'''
        info = cursor.execute(query_check, (user_id,))
        if info.fetchone() is None:
            cursor.execute(query_add, (user_message, user_id,))
            sql_conn.commit()
            return

        else:
            data = (user_message, user_id)
            cursor.execute(query_update, data)
            sql_conn.commit()
            return
        cursor.close()
        sql.conn.close()
    else:
        get_text_messages(message)



@bot.message_handler(commands=['replay'])
def get_text_messages(message):
    record = get_record_table(message)
    bot.send_message(message.from_user.id, "Последнее сообщение:" + " " + str(record) + "!")

def get_record_table(message):
    print(message.text)
    sql_conn = sqlite3.connect('ProfileUser')
    cursor = sql_conn.cursor()
    user_id = message.from_user.id
    query_get_rec = '''SELECT text FROM UsersLastEntry WHERE id_user=?'''
    temp = cursor.execute(query_get_rec, (user_id,))
    print(temp)
    record = cursor.fetchall()
    cursor.close()
    sql_conn.close()
    return record


bot.polling(none_stop=True)
