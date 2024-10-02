import random

from direc.config import load_config

config = load_config()

class RPS:
    GAME_CHOICES = [*config.message_answers["agree_message_keyboard"].values()]

    def __init__(self):
        self.rock = config.message_answers["agree_message_keyboard"]["rock"]
        self.paper = config.message_answers["agree_message_keyboard"]["paper"]
        self.scissors = config.message_answers["agree_message_keyboard"]["scissors"]

        self.choice = random.choice(self.GAME_CHOICES)


    def play(self, inp: str) -> str:
        if inp == self.choice:
            return config.message_answers["draw"] + f"\nМой выбор {self.choice}"

        if ((inp == self.rock and self.choice == self.scissors) or
                (inp == self.scissors and self.choice == self.paper) or
                (inp == self.paper and self.choice == self.rock)):
            return config.message_answers["win"] + f"\nМой выбор {self.choice}"

        return config.message_answers["lose"] + f"\nМой выбор {self.choice}"
