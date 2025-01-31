from aiogram import Router , types
from aiogram.filters import Command
from random import choice

random_router = Router()


@random_router.message(Command("random"))
async def get_random_name(message: types.Message):
    dishes = ["plov", "ragu", "samsy"]
    random_dish = choice(dishes)
    dish = types.FSInputFile(f"images/{random_dish}/{random_dish}.jpg")
    # dish_caption = FSInputFile(f"images/{random_dish}/{random_dish}.txt")
    with open(f"images/{random_dish}/{random_dish}.txt", "r", encoding="utf-8") as file:
        dish_caption = file.read()
    await message.answer_photo(photo=dish, caption=dish_caption)
