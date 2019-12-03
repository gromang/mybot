with open("cities.txt", "r", encoding="utf-8") as f:
    city_list = f.read().split("\n")

bot_city = ""
while True:
    user_city = input("Введите город:  ").capitalize()

    if user_city in city_list:

        city_list.remove(user_city)
        for city in city_list:
            if city.startswith(user_city[-1].capitalize()):
                city_list.remove(city)
                print(city)
                bot_city = city
                break
    else:
        print("Введите другой город")
        break
