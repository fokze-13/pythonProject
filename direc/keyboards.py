from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from direc.config import load_config

config = load_config()

start_keyboard_buttons = [KeyboardButton(text=i) for i in [*config.message_answers["start_keyboard_buttons"].values()]]
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     keyboard=[start_keyboard_buttons])

game_keyboard_buttons = [KeyboardButton(text=i) for i in [*config.message_answers["agree_message_keyboard"].values()]]
game_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                    keyboard=[game_keyboard_buttons])
