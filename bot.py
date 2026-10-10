import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Salom! 🎨 Emoji yaratish botiga xush kelibsiz!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Emoji yaratish uchun rasm yoki so‘z yuboring 🎨")

bot.infinity_polling()
