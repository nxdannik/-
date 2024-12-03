import telebot

bot = telebot.TeleBot('7892191061:AAFzRgh08J2wt0vyx3bwDKRK_WHgxdYSOnM', parse_mode=None)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()