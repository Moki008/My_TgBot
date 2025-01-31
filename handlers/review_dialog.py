from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton

from config import database

dialog_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    comments = State()

kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1", callback_data="1"),
        ],
        [types.InlineKeyboardButton(text="2", callback_data="2"),
        ],
        [types.InlineKeyboardButton(text="3", callback_data="3"),
        ],
        [types.InlineKeyboardButton(text="4", callback_data="4"),
        ],
        [types.InlineKeyboardButton(text="5", callback_data="5"),
        ]
    ]
)

@dialog_router.callback_query(F.data == "review")
async def process_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)


@dialog_router.message(RestourantReview.name)
async def process_phone_num(message: types.Message, state=FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Напишите, пожалуйста ваш номер телефона"
                         "\nНапример: 996706155108")
    await state.set_state(RestourantReview.phone_number)



@dialog_router.message(RestourantReview.phone_number)
async def process_rate(message: types.Message, state=FSMContext):
    phone_number = message.text
    if not str(phone_number).startswith("996") and not len(phone_number) == 12:
        await message.answer("Введите номер правильно!")
        return
    await state.update_data(phone_number=phone_number)
    await message.answer("Оцените нашу кафешку[0/5]",
                         reply_markup=kb)
    await state.set_state(RestourantReview.rate)

@dialog_router.callback_query(F.data == "1")
async def rate_1(call: types.CallbackQuery, state: FSMContext):
    await update_rate(call, state, '1')

@dialog_router.callback_query(F.data == "2")
async def rate_2(call: types.CallbackQuery, state: FSMContext):
    await update_rate(call, state, '2')

@dialog_router.callback_query(F.data == "3")
async def rate_3(call: types.CallbackQuery, state: FSMContext):
    await update_rate(call, state, '3')

@dialog_router.callback_query(F.data == "4")
async def rate_4(call: types.CallbackQuery, state: FSMContext):
    await update_rate(call, state, '4')

@dialog_router.callback_query(F.data == "5")
async def rate_5(call: types.CallbackQuery, state: FSMContext):
    await update_rate(call, state, '5')

async def update_rate(call: types.CallbackQuery, state: FSMContext, rate: str):
    await state.update_data(rate=rate)
    await call.message.answer("Напишите, что можете добавить про нашу кафешку")
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
