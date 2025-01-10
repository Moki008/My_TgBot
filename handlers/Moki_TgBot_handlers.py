import asyncio
from aiogram import Router, types
from aiogram.filters import Command
from random import choice
from aiogram.types import FSInputFile

router = Router()

all_id = []
@router.message(Command("start"))
async def start(message: types.Message):
    name = message.from_user.first_name
    my_id = message.from_user.id
    if my_id not in all_id:
        all_id.append(my_id)
    await message.answer(f"Привет, {name}, наш бот обслуживает уже {len(all_id)} пользователя "
                         f"\nМои команды:"
                         f"\n/start - начать работу с ботом"
                         f"\n/random - случайное блюдо"
                         f"\n/myinfo - информация о пользователе")


@router.message(Command("myinfo"))
async def get_my_info(message: types.Message):
    my_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    await message.answer(f'Ваш id: {my_id}'
                         f'\nИмя: {name}'
                         f'\nНик: {user_name}')


@router.message(Command("random"))
async def get_random_name(message: types.Message):
    dishes = ["plov", "ragu", "samsy"]
    random_dish = choice(dishes)
    dish = FSInputFile(f"images/{random_dish}/{random_dish}.jpg")
    # dish_caption = FSInputFile(f"images/{random_dish}/{random_dish}.txt")
    with open(f"images/{random_dish}/{random_dish}.txt", "r", encoding="utf-8") as file:
        dish_caption = file.read()
    await message.answer_photo(photo=dish, caption=dish_caption)