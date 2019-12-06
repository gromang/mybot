from glob import glob
from random import choice

def send_cat_picture(update, context):
    cat_list = glob('cats/*cat*.pn*')
    cat_pic = choice(cat_list)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(cat_pic, 'rb'))