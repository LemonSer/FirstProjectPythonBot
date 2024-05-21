from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_menu():
    menu_inline = InlineKeyboardMarkup(row_width=1)
    button_character = InlineKeyboardButton('Мордекайзер', callback_data='tutorial')
    menu_inline.add(button_character)
    return menu_inline

def skills():
    slills_inline = InlineKeyboardMarkup(row_width=2)
    button_skills_1 = InlineKeyboardButton('Восхождение тьмы', callback_data='skills_1')
    button_skills_2 = InlineKeyboardButton('Уничтожение', callback_data='skills_2')
    button_skills_3 = InlineKeyboardButton('Несокрушимый', callback_data='skills_3')
    button_skills_4 = InlineKeyboardButton('Смертельная хватка', callback_data='skills_4')
    button_skills_5 = InlineKeyboardButton('Царство смерти', callback_data='skills_5')
    slills_inline.add(button_skills_1, button_skills_2, button_skills_3, button_skills_4, button_skills_5)
    return slills_inline