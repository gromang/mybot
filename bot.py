import logging
import os
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from dotenv import load_dotenv
from ephem_handlers import *
from other_handlers import *
from city_game_handler import *
from handler_cat import *

load_dotenv()

PROXY = {
    "proxy_url": "socks5://t1.learn.python.ru:1080",
    "urllib3_proxy_kwargs": {"username": "learn", "password": "python"},
}

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log",
)


def main():

    mybot = Updater(os.getenv("TOKEN"),request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planetarium))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("city", enter_city_game)],
        states={"start city game": [MessageHandler(Filters.text, city_game)]},
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    dp.add_handler(conv_handler)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

def cancel(update, context):
    update.message.reply_text("Приятно было поиграть.")
    return ConversationHandler.END


if __name__ == "__main__":
    main()
