from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import LEVELS

def levels_keyboard():
    buttons = [[]]
    for name in LEVELS:
        button = name
        level = LEVELS[name]
        if len(buttons[-1]) == 3:
            buttons.append([])
        buttons[-1].append(InlineKeyboardButton(text=button, callback_data=f'level:{level}'))
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
