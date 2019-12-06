from emoji import emojize
import settings
from random import choice

def greet_user(update, context):
    smile = get_user_emo(context.user_data)
    context.user_data['emo']=smile
    text = f"Привет {smile}"
    update.message.reply_text(text)


def talk_to_me(update, context):
    smile = get_user_emo(context.user_data)
    user_text = f"Привет, {update.message.chat.first_name} {smile}! Ты написал {update.message.text}"
    print(user_text)
    update.message.reply_text(user_text)

def get_user_emo(userdata):
    if 'emo' in userdata:
        return context.user_data['emo']
    else:
        context.user_data['emo'] = emojize(choice(settings.USER_EMOJI),use_aliases=True)
        return context.user_data['emo']



def wordcount(update, context):
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
