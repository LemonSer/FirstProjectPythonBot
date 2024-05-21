from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Мордекайзер')
    button_2 = KeyboardButton('Атрокс')
    button_3 = KeyboardButton('Чо`Гат')
    keyboard.add(button_1, button_2, button_3)
    return keyboard

def get_keyboard_mor():
    keyboard_mor = ReplyKeyboardMarkup(resize_keyboard=True)
    button_5 = KeyboardButton('ВОСХОЖДЕНИЕ ТЬМЫ')
    button_6 = KeyboardButton('УНИЧТОЖЕНИЕ')
    button_7 = KeyboardButton('НЕСОКРУШИМЫЙ')
    button_8 = KeyboardButton('СМЕРТЕЛЬНАЯ ХВАТКА')
    button_9 = KeyboardButton('ЦАРСТВО СМЕРТИ')
    button_10 = KeyboardButton('В начальное меню')
    keyboard_mor.add(button_5, button_6, button_7, button_8, button_9, button_10)
    return keyboard_mor

def get_keyboard_atr():
    keyboard_atr = ReplyKeyboardMarkup(resize_keyboard=True)
    button_11 = KeyboardButton('СТОЙКА РАЗРУШИТЕЛЯ')
    button_12 = KeyboardButton('КЛИНОК ДАРКИНОВ')
    button_13 = KeyboardButton('ПРОКЛЯТЫЕ ЦЕПИ')
    button_14 = KeyboardButton('ТЕМНЫЙ РЫВОК')
    button_15 = KeyboardButton('ГУБИТЕЛЬ МИРА')
    button_10 = KeyboardButton('В начальное меню')
    keyboard_atr.add(button_11, button_12, button_13, button_14, button_15, button_10)
    return keyboard_atr

def get_keyboard_cho():
    keyboard_cho = ReplyKeyboardMarkup(resize_keyboard=True)
    button_17 = KeyboardButton('ПЛОТОЯДНОСТЬ')
    button_18 = KeyboardButton('ПРОЛОМ ')
    button_19 = KeyboardButton('ДИКИЙ КРИК')
    button_20 = KeyboardButton('СМЕРТОНОСНЫЕ ШИПЫ')
    button_21 = KeyboardButton('ПОЖИРАНИЕ')
    button_10 = KeyboardButton('В начальное меню')
    keyboard_cho.add(button_17, button_18, button_19, button_20, button_21, button_10)
    return keyboard_cho