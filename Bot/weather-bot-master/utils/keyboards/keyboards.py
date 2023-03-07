from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def keyboard_for_not_sub() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Узнать погоду")
    keyboard.button(text="Подписаться на погоду")
    keyboard.adjust(2)

    return keyboard.as_markup(resize_keyboard=True)


def keyboard_for_sub() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Узнать погоду")
    keyboard.button(text="Отписаться от погоды")
    keyboard.adjust(2)

    return keyboard.as_markup(resize_keyboard=True)
