import asyncio
from Moki_config import bot, dp
from Moki_handlers.start import start_router
from Moki_handlers.my_info import my_info_router
from Moki_handlers.random import random_router


async def main():
    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(random_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
