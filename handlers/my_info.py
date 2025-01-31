from aiogram import Router, types
from aiogram.filters import Command

my_info_router = Router()

@my_info_router.message(Command("myinfo"))
async def get_my_info(message: types.Message):
    my_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    await message.answer(f'Ваш id: {my_id}'
                         f'\nИмя: {name}'
                         f'\nНик: {user_name}')
