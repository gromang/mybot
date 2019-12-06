from emoji import emojize
import settings
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton


def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data["emo"] = emo
    text = f"Привет {emo}"

    update.message.reply_text(text, reply_markup=get_keyboard())


def get_keyboard():
    contact_button = KeyboardButton("Прислать контакты", request_contact=True)
    locatiom_button = KeyboardButton("Прислать координаты", request_location=True)
    my_keyboard = ReplyKeyboardMarkup(
        [["Призвать КОТЭ"], [contact_button, locatiom_button]], resize_keyboard=True
    )
    return my_keyboard


def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = f"Привет, {update.message.chat.first_name} {emo}! Ты написал {update.message.text}"
    update.message.reply_text(user_text, reply_markup=get_keyboard())


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
    update.message.reply_text(message, reply_markup=get_keyboard())


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text(
        "Спасибо {}".format(get_user_emo(user_data)), reply_markup=get_keyboard()
    )


def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text(
        "Спасибо {}".format(get_user_emo(user_data)), reply_markup=get_keyboard()
    )

