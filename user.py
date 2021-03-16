import telebot
bot = telebot.TeleBot('1630299681:AAETYUXFhczaZ2gAozn_3_Iqgq4-WX6o3js')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    print(message.from_user.id)

bot.polling(none_stop=True)