from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

kb_main = ReplyKeyboardBuilder()

kb_main.row(
    KeyboardButton(text="Старт"),
    KeyboardButton(text="Помощь")
)