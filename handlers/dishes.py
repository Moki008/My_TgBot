from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
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
