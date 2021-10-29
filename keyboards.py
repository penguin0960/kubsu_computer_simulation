from telegram import ReplyKeyboardMarkup

KEYBOARD_YES_OR_NO = ReplyKeyboardMarkup(
    keyboard=[['Да', 'Нет']],
    one_time_keyboard=True,
    input_field_placeholder='Да или Нет?',
)
