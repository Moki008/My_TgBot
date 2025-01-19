

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery

from config import database

dialog_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    comments = State()


@dialog_router.callback_query(F.data == "review")
async def process_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)


@dialog_router.message(RestourantReview.name)
async def process_phone_num(message: types.Message, state=FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Напишите, пожалуйста ваш номер телефона")
    await state.set_state(RestourantReview.phone_number)


@dialog_router.message(RestourantReview.phone_number)
async def process_rate(message: types.Message, state=FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Оцените нашу кафешку[0/5]")
    await state.set_state(RestourantReview.rate)


@dialog_router.message(RestourantReview.rate)
async def process_comment(message: types.Message, state=FSMContext):
    rate = message.text
    await state.update_data(rate=rate)
    await message.answer("Напишите, что можете добавить про нашу кафешку")
    await state.set_state(RestourantReview.comments)


@dialog_router.message(RestourantReview.comments)
async def finish_dialog(message: types.Message, state=FSMContext):
    comment = message.text
    await state.update_data(comment=comment)
    await message.answer("Спасибо за ваш отзыв!")
    data = await state.get_data()
    print(data)
    database.save_review(data)
    await state.clear()
