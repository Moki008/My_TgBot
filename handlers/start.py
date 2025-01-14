from aiogram import Router,F, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    name = message.from_user.first_name

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="О нашем Кафе", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Каталог блюд", callback_data="True"),
                types.InlineKeyboardButton(text="Реклама", callback_data="True"),
            ],
            [
                types.InlineKeyboardButton(text="Наш рейтинг", callback_data="True"),
                types.InlineKeyboardButton(text="Где мы находимся", callback_data="True"),
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
            ],
        ]
    )
    await message.answer(f"Привет, {name}"
                         f"\nМои команды:"
                         f"\n/start - начать работу с ботом"
                         f"\n/random - случайное блюдо"
                         f"\n/myinfo - информация о пользователе",
                         reply_markup=kb)

@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("Мы ресторан")


@start_router.callback_query(F.data == "True")
async def other(callback: types.CallbackQuery):
    await callback.message.answer("None")





