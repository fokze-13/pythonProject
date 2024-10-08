from dataclasses import dataclass
from typing import Any
from aiogram import Bot
from aiogram.types import BotCommand

from environs import Env

@dataclass
class Config:
    token: str
    basic_format: str
    message_answers: dict[str, Any]
    log_file: str
    commands: dict[str, str]



def load_config() -> Config:
    env = Env()
    env.read_env("D:\\Projects\\pythonProject\\.env")

    return Config(
        token=env("TOKEN"),
        basic_format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
        message_answers={"start": "Привет! Хочешь сыграть в игру \"Камень, ножницы, бумага\"?\n Также советую ознакомиться с правилами - /help",
                         "start_keyboard_buttons": {"agree": "Давай!",
                                                    "disagree": "Не хочу",
                                                    "help": "/help"},
                         "inline_keyboard_button": "Telegram",
                         "agree_message": "Отлично! Делай свой выбор!",
                         "agree_message_keyboard": {"rock": "Камень",
                                                    "paper": "Бумага",
                                                    "scissors": "Ножницы"},
                         "disagree_message" :"Хорошо, если вдруг захочешь сыграть нажми \"Давай!\"",
                         "echo_message": "Извини, но я тебя не понял",
                         "win": "Молодец! Ты выиграл!",
                         "lose": "Увы, но ты проиграл..",
                         "draw": "Ух-ты! ничья!",
                         "help": "Ты выбираешь свой вариант и нажимаешь на клавиатуру, после чего я тоже делаю выбор, и потом мы узнаем выиграл ты или нет. Давай приступим к игре!"
                         },
        log_file="log.txt",
        commands={"/start": "Старт бота",
                  "/help": "Помощь"}
    )

config = load_config()

async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command = i, description=j) for i, j in config.commands.items()]
    await bot.set_my_commands(main_menu_commands)
