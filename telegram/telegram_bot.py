import telebot
from telebot import types

bot = telebot.TeleBot('6142960419:AAEU9BzyWThxQXHDAQQAaVUEEfxdLLF85ew')

#Поиск курса валюты
import requests
from bs4 import BeautifulSoup

def get_exchange_rate():
    url = "https://www.google.com/search?q=курс+бата+к+рублю"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем блок с курсом валюты
    rate_div = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
    if rate_div:
        rate = float(rate_div.text.split()[0].replace(',', '.'))
        return rate
    else:
        raise Exception("Не удалось найти курс валюты")

#Cтартовая команда
@bot.message_handler(commands=['start']) 
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курс baht/rub")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Приветсвую! Я бот сообщества Only One.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Курс
    if message.text == 'Курс baht/rub':
        exchange_rate = get_exchange_rate()
        print("Курс бата к рублю:", exchange_rate)

bot.polling(none_stop=True, interval=0)