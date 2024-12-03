import telebot
import secrets

import string




TOKEN = '7942564359:AAGWUHwIlNSX5w9MWQtKk92yAtYq5h7XeCQ'


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(message, "Привіт! Я бот для генерації паролів /generate.")



@bot.message_handler(commands=['generate'])
def generate_password(message):

    msg = bot.reply_to(message, "Введіть довжину пароля:")
    bot.register_next_step_handler(msg, process_password_length)


def process_password_length(message):

    try:
        password_length = int(message.text)

        if password_length < 1:
            raise ValueError

        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))

        bot.reply_to(message, f"Ось твій новий пароль: {password}")

    except ValueError:

        bot.reply_to(message, "Некоректна довжина пароля.nВведіть ціле число від 1pip.")
        generate_password(message)



bot.polling()