import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup

from ..keyboards import keyboards
from ..repository import repository
from ..service import service


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    username = message.from_user.username
    tg_user_id = message.from_user.id
    response = f"<b>Привет, {username}</b>!\nЯ умею показывать погоду и отправлять уведомления о погоде в определенное время <u>только для города Пермь</u>."

    await message.answer(
        response,
        reply_markup=keyboards.keyboard_for_not_sub(),
        parse_mode="HTML"
    )
    repository.create_user(tg_user_id, username)


@router.message(Text("Узнать погоду"))
async def get_weather(message: Message):
    response = service.get_weather()
    date = str(datetime.datetime.today().date()).split("-")
    time = str(datetime.datetime.today().time()).split(".")

    text = f"<b>Погода на {date[2]}.{date[1]}.{date[0]} в {time[0]}:</b>\n\n" \
           f"<u>Описание:</u>  {response['weather'][0]['description']}\n" \
           f"<u>Температура воздуха:</u>  {response['main']['temp']}°C\n" \
           f"<u>Ощущаемая температура:</u>  {response['main']['feels_like']}°C"

    await message.answer(text, parse_mode="HTML")


@router.message(Text("Подписаться на погоду"))
async def create_subscribe(message: Message):
    tg_user_id = message.from_user.id
    response = repository.create_subscribe(tg_user_id)
    if not response:
        await message.answer(
            text="Произошла ошибка, попробуйте позже.",
            reply_markup=keyboards.keyboard_for_not_sub()
        )
        return

    await message.answer("<b>Вы успешно подписались на уведомления о погоде!</b>\nТеперь "
                         "каждый день в 9:00 вам будет приходить уведомление о погоде.",
                         reply_markup=keyboards.keyboard_for_sub(),
                         parse_mode="HTML"
                         )


@router.message(Text("Отписаться от погоды"))
async def delete_subscribe(message: Message):
    tg_user_id = message.from_user.id
    response = repository.delete_subscribe(tg_user_id)
    if not response:
        await message.answer(
            text="Произошла ошибка, попробуйте позже.",
            reply_markup=keyboards.keyboard_for_not_sub()
        )
        return

    await message.answer(
        "<b>Вы успешно отписались от уведомлений о погоде!</b>",
        reply_markup=keyboards.keyboard_for_not_sub(),
        parse_mode="HTML"
        )