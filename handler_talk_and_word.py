from emoji import emojize
import settings
from random import choice


def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data["emo"] = emo
    text = f"Привет {emo}"
    update.message.reply_text(text)


def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = f"Привет, {update.message.chat.first_name} {emo}! Ты написал {update.message.text}"
    update.message.reply_text(user_text)


def get_user_emo(user_data):
    if "emo" in user_data:
        return user_data["emo"]
    else:
        user_data["emo"] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data["emo"]


def wordcount(bot, update):
    user_text = update.message.text
    text = user_text.split(" ")[1:]
    word_cnt = 0
    if len(text) < 1:
        message = "Пустая строка"
    else:
        for i in text:
            if i.isalpha():
                word_cnt += 1
        message = f"Колличество слов : {word_cnt} "
    update.message.reply_text(message)
