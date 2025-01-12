from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

all_id = []
@start_router.message(Command("start"))
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





