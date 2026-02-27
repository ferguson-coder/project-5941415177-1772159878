import telebot

bot = telebot.TeleBot('YOUR_TOKEN')

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling()
