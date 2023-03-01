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


@dp.message_handler(commands=['help'])
async def commands_help(message: types.Message):

    await message.answer('Wait... Uploading your request')


@dp.message_handler(commands=['image, img'])
async def cmd_image(message: types.Message):
    URL = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fnature%2F&psig=AOvVaw3Vux3E-IC7QIWyJ2KQjxMR&ust=1677780723183000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCIjzz7Gqu_0CFQAAAAAdAAAAABAE'

    await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))
    await bot.sen



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
