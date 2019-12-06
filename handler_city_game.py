import random


def enter_city_game(bot, update, user_data):
    update.message.reply_text(
        "Игра в города.\n"
        "1) Должен быть в РФ,\n"
        "2) состоять из одного слова\n"
        "   или через дефис\n"
        "3) Если оканчивается на Ы и Ь, \n"
        "   то берется идущая перед\n"
        "   ними буква. \n"
        "Для завершения - наберите /cancel\n"
        "Итак, я начинаю: \n"
    )
    with open("cities.txt", "r", encoding="utf-8") as f:
        city_list = user_data["cities"] = f.read().split("\n")
        bot_city = random.choice(city_list)
        city_list.remove(bot_city)
        update.message.reply_text(bot_city)
        user_data["bot"] = bot_city
    return "start city game"


def city_game(bot, update, user_data):
    city_list = user_data["cities"]
    bot_city = user_data["bot"]
    user_city = update.message.text.capitalize()
    if bot_city[-1] in ["ь", "ы", "й"]:
        n = -2
    else:
        n = -1

    if user_city[-1] in ["ь", "ы", "й"]:
        k = -2
    else:
        k = -1

    if user_city not in city_list:
        update.message.reply_text("Напишите другой город")
    elif user_city[0].lower() != bot_city[n].lower():
        update.message.reply_text(f"Должен начинаться на {bot_city[n].capitalize()}")
    else:
        city_list.remove(user_city)
        for city in city_list:
            if city.startswith(user_city[k].capitalize()):
                city_list.remove(city)
                update.message.reply_text(city)
                user_data["bot"] = city
                break

