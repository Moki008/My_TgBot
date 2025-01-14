from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

dialog_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()
    the_and = State()


@dialog_router.callback_query(F.data == "review")
async def review_dialog(call: types.CallbackQuery, state=FSMContext):
    await call.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.phone_number)


@dialog_router.message(RestourantReview.phone_number)
async def review_dialog(message: types.Message, state=FSMContext):
    await message.answer("Напишите, пожалуйста ваш номер телефона")
    await state.set_state(RestourantReview.rate)


@dialog_router.message(RestourantReview.rate)
async def review_dialog(message: types.Message, state=FSMContext):
    await message.answer("Оцените нашу кафешку[0/5]")
    await state.set_state(RestourantReview.extra_comments)


@dialog_router.message(RestourantReview.extra_comments)
async def review_dialog(message: types.Message, state=FSMContext):
    await message.answer("Напишите, что можете добавить про нашу кафешку")
    await state.set_state(RestourantReview.the_and)


@dialog_router.message(RestourantReview.the_and)
async def review_dialog(message: types.Message, state=FSMContext):
    await message.answer("Спасибо за ваш отзыв!")
    await state.clear()
