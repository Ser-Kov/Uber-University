from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *
from crud_functions_2 import *


API = '7534014587:AAG8JyHv8adY-UG8Ku9Kr8CS4k7i1sxwNIk'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Регистрация')],
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True)


kb_calculate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')]
    ]
)
kb_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Iphone 10', callback_data='product_buying'),
         InlineKeyboardButton(text='Iphone 11', callback_data='product_buying'),
         InlineKeyboardButton(text='Iphone 12', callback_data='product_buying'),
         InlineKeyboardButton(text='Iphone 13', callback_data='product_buying')],
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью', reply_markup=kb_start)


@dp.message_handler(text='Информация')
async def start(message):
    await message.answer('Этой мой первый бот, который обладает минимальным функционалом. '
                         'Разработчик: @ser_kovalevsky')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_calculate)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    num_iph = 10
    for i in range(4):
        await message.answer(f'Название: {get_all_products()[i][0]} | Описание: {get_all_products()[i][1]} '
                             f'| Цена: {get_all_products()[i][2]}')
        with open(f'iph{num_iph}.jpg', 'rb') as img:
            await message.answer_photo(img)
            num_iph += 1
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_buy)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь с таким именем уже существует. Введите другое имя:')


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data_user = await state.get_data()
    add_user(data_user['username'], data_user['email'], data_user['age'])
    await message.answer('Регистрация прошла успешно')
    await state.finish()

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.answer()
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.answer()
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_man = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {int(calories_man)}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
