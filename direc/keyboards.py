from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from direc.config import load_config

config = load_config()

start_keyboard_buttons = [KeyboardButton(text=i) for i in [*config.message_answers["start_keyboard_buttons"].values()]]
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     keyboard=[start_keyboard_buttons])

game_keyboard_buttons = [KeyboardButton(text=i) for i in [*config.message_answers["agree_message_keyboard"].values()]]
game_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                    keyboard=[game_keyboard_buttons])

username_inline_keyboard_button = InlineKeyboardButton(text=config.message_answers["inline_keyboard_button"], url="t.me/hudp72")
username_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[username_inline_keyboard_button]])