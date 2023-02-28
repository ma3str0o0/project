import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '6080835241:AAGbIitOW7IdPmsaVEdWDXez61MPqL5OtA8'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply('Nikita Dvornitsyn\'s test bot')


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


@dp.message_handler(commands=['weather'])
async def question_answer(message: types.Message):

    cities = {
        'Moscow',
        'Dubai',
        'New-York',
        'Yekaterinburg',
        'Abu-Dhabi',
    }
    url = 'https://wttr.in'
    # не изменяйте значение URL

    weather_parameters = {
        '0': '',
        'T': '',
        'M': '',
        'lang': 'ru'
    }


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
