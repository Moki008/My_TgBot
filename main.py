import asyncio
from random import choice
from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

token = dotenv_values(".env")["MY_BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name} ")

@dp.message(Command("myinfo"))
async def get_my_info(message):
    my_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    await message.answer(f'Ваш id: {my_id}'
                         f'\nИмя: {name}'
                         f'\nНик: {user_name}')

@dp.message(Command("random"))
async def get_random_name(message):
    names = ["Tom","William", "Kean", "Jon", "Terminator", "Arnold"]
    await message.answer(choice(names))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())