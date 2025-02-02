from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_widgets.pagination import TextPaginator
from aiogram.fsm.state import State, StatesGroup

from config import database

dish_router = Router()
dish_router.message.filter(
    F.from_user.id == 7309817854
)


class Dish(StatesGroup):
    name = State()
    price = State()
    about = State()
    photo = State()
    category = State()
    portion = State()


@dish_router.message(Command("setdish"))
async def add_dish(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, введите название блюда: ")
    await state.set_state(Dish.name)


@dish_router.message(Dish.name)
async def add_dish(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Пожалуйста, введите цену блюда: ")
    await state.set_state(Dish.price)


@dish_router.message(Dish.price)
async def add_dish(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)
    await message.answer("Пожалуйста,напишите о вашем блюде: ")
    await state.set_state(Dish.about)


@dish_router.message(Dish.about)
async def add_dish(message: types.Message, state: FSMContext):
    about = message.text
    await state.update_data(about=about)
    await message.answer("Пожалуйста отправьте фото вашего блюда: ")
    await state.set_state(Dish.photo)

@dish_router.message(Dish.photo, F.photo)
async def add_dish(message: types.Message, state: FSMContext):
    photo = message.photo
    mid_image = photo[-2]
    await state.update_data(photo=mid_image.file_id)
    await message.answer("Выберите,категорию блюда: ")
    await state.set_state(Dish.category)


@dish_router.message(Dish.category)
async def add_dish(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(category=category)
    await message.answer("Выберите,порцию блюда: ")
    await state.set_state(Dish.portion)


@dish_router.message(Dish.portion)
async def add_dish(message: types.Message, state: FSMContext):
    portion = message.text
    await state.update_data(portion=portion)
    await message.answer("Блюдо добавлено! ")
    data = await state.get_data()
    print(data)
    database.save_dishes(data)
    await state.clear()

@dish_router.message(Command("getdish"))
async def get_dish(message: types.Message):
    await message.answer("Наше меню блюд")
    dish_list = database.get_dishes()

    text_dishes = [
        f"Название: {dish.get('name', 'Без названия')}\nЦена: {dish.get('price')} сом\nО блюде: {dish.get('about')}\nКатегория: {dish.get('category')}\nПорция: {dish.get('portion')}" for dish in dish_list
    ]

    paginator = TextPaginator(data=text_dishes, router=dish_router, per_page=1)
    current_text_chunk, reply_markup = paginator.current_message_data

    await message.answer(
        text=current_text_chunk,
        reply_markup=reply_markup
    )
