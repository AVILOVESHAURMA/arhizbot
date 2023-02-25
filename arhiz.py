import telebot
botToken="5807004233:AAFdRb2KXZIECrNsUmDNOLzs8c5ytjq8PNY"
bot=telebot.TeleBot(botToken)


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, "Хай, играешь в танки?")

@bot.message_handler(func=lambda message: True)
def echo_message(msg):
    match msg.text.lower():
        case "привет":
            bot.send_message(msg.chat.id, "О, привет, как дела?")
        case "нормально":
            bot.send_message(msg.chat.id, "у меня тоже")

    if(msg.text.lower()=="привет"):
        bot.send_message(msg.chat.id, "О, привет, как дела?")
    elif (msg.text.lower() == "нормально"):
        bot.send_message(msg.chat.id, "у меня тоже")

bot.infinity_polling()
