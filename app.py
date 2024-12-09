import time


def soup(number):
    current_time = time.time() + 32400
    # UTCからJSTに変換
    current_day = current_time // 86400
    menu_number = (current_day + number - 19936) % 4
    if menu_number == 0:
        result = "Soy Sauce Seaweed"
    if menu_number == 1:
        result = "Salt Seaweed!!!"
    if menu_number == 2:
        result = "Soy Sauce Egg"
    if menu_number == 3:
        result = "Salt Egg!!!"
    return result
