import telebot
import os
from dotenv import load_dotenv
load_dotenv()

from classChatSupport import ChatSupport

bot = telebot.TeleBot(os.getenv("TGTOKEN"))
chatSupport = ChatSupport()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, пиши все что хочешь")

@bot.message_handler(func=lambda message: True)
def generate(message):
    if message.text:
        ans = chatSupport.getAnswer(message.chat.id,message.text)
        bot.send_message(message.chat.id, ans)
    else:
        bot.send_message(message.chat.id, "я могу отвечать только на текстовые сообщения.")


bot.polling()