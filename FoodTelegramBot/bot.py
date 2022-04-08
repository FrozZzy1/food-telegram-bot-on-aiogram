from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from food import *

from random import randint as rd

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!\nНапиши:"Еда"')


@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.reply('Напиши номер категории, чтобы сменить блюдо\nНапиши "Еда", чтобы сменить категорию блюд')

@dp.message_handler()
async def choice_of_dish(msg: types.Message):
    if msg.text == 'Еда' or msg.text == 'еда':
        await msg.reply('Что ты хочешь приготовить?\n1. Суп\n2. Блюдо с рисом\n3. Блюдо с картофелем\n4. Блюдо с макаронами\n5. Блюдо с гречкой\n6. Мясное блюдо\n7. Фастфуд\n8. Выпечку')
    elif msg.text in "12345678":
        category = msg.text
    if category in "12345678":
        if category == "1":
            await msg.reply(SOUPS[rd(0, len(SOUPS))])
        elif category == "2":
            await msg.reply(RICE_DISHES[rd(0, len(RICE_DISHES))])
        elif category == "3":
            await msg.reply(POTATO_DISHES[rd(0, len(POTATO_DISHES))])
        elif category == "4":
            await msg.reply(PASTA_DISHES[rd(0, len(PASTA_DISHES))])
        elif category == "5":
            await msg.reply(BUCKWHEAT_DISHES[rd(0, len(BUCKWHEAT_DISHES))])
        elif category == "6":
            await msg.reply(MEAT_DISHES[rd(0, len(MEAT_DISHES))])
        elif category == "7":
            await msg.reply(FASTFOOD[rd(0, len(FASTFOOD))])
        elif category == "8":
            await msg.reply(PASTRIES[rd(0, len(PASTRIES))])

if __name__ == '__main__':
    executor.start_polling(dp)
