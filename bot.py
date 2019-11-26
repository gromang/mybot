import logging
import os
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

load_dotenv()

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log')


def main():
    mybot = Updater(os.getenv('TOKEN'), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planetarium))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    print(update)
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planetarium(bot, update):

    user_text = update.message.text
    planet = user_text.split(' ')[-1].lower()

    if planet == 'mars':
        const = ephem.constellation(ephem.Mars('2019'))
    elif planet == 'saturn':
        const = ephem.constellation(ephem.Saturn('2019'))
    elif planet == 'jupiter':
        const = ephem.constellation(ephem.Jupiter('2019'))
    elif planet == 'moon':
        const = ephem.constellation(ephem.Moon('2019'))

    print(const)
    update.message.reply_text(const[-1])


main()
