from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_iline_mor():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://www.leagueoflegends.com/ru-ru/champions/mordekaiser/')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_iline_atr():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://www.leagueoflegends.com/ru-ru/champions/aatrox/')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_iline_cho():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://www.leagueoflegends.com/ru-ru/champions/cho-gath/')
    keyboard_inline.add(but_inline)
    return keyboard_inline
