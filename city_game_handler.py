def enter_city_game(bot, update):
    update.message.reply_text(
        "Предлагаю поиграть в города.\n"
        "Вы называете город в РФ, а я\n"
        "а я в ответ - город, первая \n"
        "буква которого равна последней\n"
        "букве предложенного вами города.\n"
        "Если последняя буква Ы и Ь, \n"
        "то учитывается предыдущая перед\n"
        "ними буква. \n"
        "Для завершения - наберите /cancel\n"
        "Итак, Ваш город?\n"
    )
    with open("cities.txt", "r", encoding="utf-8") as f:
        update.user_data["cities"] = f.read().split("\n")
    return "start city game"


def city_game(bot, update):
    towns = update.user_data["cities"]
    user_city = update.message.text

    update.message.reply_text(town)


def cancel(bot, update):
    update.message.reply_text("Приятно было поиграть.")
    return ConversationHandler.END
