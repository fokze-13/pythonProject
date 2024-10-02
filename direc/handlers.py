from aiogram.filters import Command
from aiogram import F
from direc.keyboards import *
from aiogram import Router, types
from direc.config import load_config
from direc.utils import RPS

config = load_config()
router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(config.message_answers["start"], reply_markup=start_keyboard)
    await message.answer("Связаться со мной", reply_markup=username_inline_keyboard)


@router.message(F.text == config.message_answers["start_keyboard_buttons"]["agree"])
async def agree(message: types.Message):
    await message.answer(config.message_answers["agree_message"], reply_markup=game_keyboard)


@router.message(F.text == config.message_answers["agree_message_keyboard"]["rock"])
@router.message(F.text == config.message_answers["agree_message_keyboard"]["paper"])
@router.message(F.text == config.message_answers["agree_message_keyboard"]["scissors"])
async def rock(message: types.Message):
    await message.answer(RPS().play(message.text))
    await message.answer("Хочешь сыграть еще?", reply_markup=start_keyboard)


@router.message(F.text == config.message_answers["start_keyboard_buttons"]["disagree"])
async def disagree(message: types.Message):
    await message.answer(config.message_answers["disagree_message"])


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(config.message_answers["help"], reply_markup=start_keyboard)


@router.message(F.text)
async def echo(message: types.Message):
    await message.answer(config.message_answers["echo_message"])
