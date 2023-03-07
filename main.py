import logging
# import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6080835241:AAGbIitOW7IdPmsaVEdWDXez61MPqL5OtA8'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Nikita Dvornitsyn\'s test bot')


@dp.message_handler(commands=['help'])
async def commands_help(message: types.Message):
    await message.answer('Wait... Uploading your request')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(commands=['img'])
async def image(messgae: types.chat_photo):
    photo_url = 'https://i.pinimg.com/originals/27/56/a4/2756a4304c2820327fd2cc22673be712.jpg'
    await messgae.answer(bot.send_photo(photo=photo_url))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
