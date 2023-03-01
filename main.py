import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '6080835241:AAGbIitOW7IdPmsaVEdWDXez61MPqL5OtA8'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.answer('Nikita Dvornitsyn\'s test bot')


@dp.message_handler(commands=['commands', 'help'])
async def commands_help(message: types.Message):
    commands_option = {
        '/start': 'Bot start-up',
        '/help': 'Assistance and questions',
        '/commands': 'Shows the list of usable commands',
        '/quit': 'log out'
    }
    for i in commands_option:
         await message.answer(f'Command {commands_option.keys()[i]} is reliable for {commands_option.values()[i]}')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
