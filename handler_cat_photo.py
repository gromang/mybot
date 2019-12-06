from glob import glob
from random import choice


def send_cat_picture(bot, update):
    cat_list = glob("cats/*cat*.pn*")
    cat_pic = choice(cat_list)
    bot.send_photo(
        chat_id=update.message.chat.id,
        photo=open(cat_pic, "rb"),
        reply_markup=get_keyboard(),
    )

