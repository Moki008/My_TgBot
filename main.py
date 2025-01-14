import asyncio
from config import bot, dp
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.random import random_router
from handlers.review_dialog import dialog_router


async def main():
    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(random_router)
    dp.include_router(dialog_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
