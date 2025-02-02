import asyncio
import logging
from aiogram import Bot

from config import bot, dp, database, databade_dish
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.random import random_router
from handlers.review_dialog import dialog_router
from handlers.dishes import dish_router
from handlers.group_management import group_router


async def start_up(bot: Bot):
    database.create_table()
    databade_dish.create_table()


async def main():
    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(random_router)
    dp.include_router(dialog_router)
    dp.include_router(dish_router)
    dp.include_router(group_router)

    dp.startup.register(start_up)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
