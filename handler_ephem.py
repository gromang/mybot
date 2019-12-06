import ephem
from datetime import datetime


def planetarium(update, context):

    user_text = update.message.text
    planet = user_text.split(" ")[-1].lower()

    if planet == "mars":
        const = ephem.constellation(ephem.Mars("2019"))
    elif planet == "saturn":
        const = ephem.constellation(ephem.Saturn("2019"))
    elif planet == "jupiter":
        const = ephem.constellation(ephem.Jupiter("2019"))
    elif planet == "moon":
        const = ephem.constellation(ephem.Moon("2019"))

    print(const)
    update.message.reply_text(const[-1])


def next_full_moon(update, context):
    user_text = update.message.text
    user_date = user_text.split(" ")[-1]
    # предполагается что пользователь будет вводить дату в формате ГГГГ-ММ-ДД,
    # иначе придется писать ряд функций по распознаванию и домысливанию того,
    # что ввел пользователь
    user_date = datetime.strptime(user_date, "%Y-%m-%d")
    moon_date = ephem.next_full_moon(user_date)
    update.message.reply_text(moon_date)
