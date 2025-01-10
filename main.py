import asyncio
from handlers.Moki_TgBot_handlers import router
from handlers.Moki_TgBot_config import bot, dp


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
