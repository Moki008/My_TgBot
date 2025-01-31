from aiogram import Router, F, types

group_router = Router()
group_router.message.filter(F.chat.type != "private")

words = ("гнида", "дурак", "ишак")

@group_router.message(F.text)
async def echo_handler(message: types.Message):
    for word in words:
        if word.lower() in message.text:
            await message.answer("Такое слово нельзя использовать")
            await message.delete()