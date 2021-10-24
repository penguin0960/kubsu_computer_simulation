import logging
import os
from typing import Union

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

KEYBOARD_YES_OR_NO = ReplyKeyboardMarkup(
    keyboard=[['Да', 'Нет']],
    one_time_keyboard=True,
    input_field_placeholder='Да или Нет?',
)

FIO, AGE, CITY, PHONE, MAIL, EDUCATION, SKILLS, EXPERIENCE, PORTFOLIO, FULL_DAY, SALARY, SOURCE = range(12)


def log_user_info(user_nickname: str, field_name: str, value: Union[str, int]) -> None:
    logger.info('{user_nickname}.{field_name} = {value}'.format(
        user_nickname=user_nickname,
        field_name=field_name,
        value=value,
    ))


def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    update.message.reply_text(
        'Здравствуйте!\n'
        'Чтобы перестать общаться со мной, нажмите /cancel.\n'
        'Введите ваше ФИО:'
    )
    return FIO


def fio(update: Update, context: CallbackContext) -> int:
    field_name = 'fio'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    context.user_data['success'] = True
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    update.message.reply_text('Введите ваш возраст:')
    return AGE


def age(update: Update, context: CallbackContext) -> int:
    field_name = 'age'
    user = update.message.from_user
    user_answer = int(update.message.text)
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    if user_answer > 40:
        context.user_data['success'] = False

    update.message.reply_text('Введите ваш город проживания:')
    return CITY


def city(update: Update, context: CallbackContext) -> int:
    field_name = 'city'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    update.message.reply_text('Введите ваш номер телефона:')
    return PHONE


def phone(update: Update, context: CallbackContext) -> int:
    field_name = 'phone'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    update.message.reply_text('Введите ваш E-mail:')
    return MAIL


def mail(update: Update, context: CallbackContext) -> int:
    field_name = 'email'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )

    update.message.reply_text(
        'Есть ли у вас образование в сфере дизайна?',
        reply_markup=KEYBOARD_YES_OR_NO,
    )

    return EDUCATION


def education(update: Update, context: CallbackContext) -> int:
    field_name = 'education'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    if user_answer == 'Нет':
        context.user_data['success'] = False

    update.message.reply_text(
        'Умеете ли вы работать в Adobe Illustrator и Photoshop?',
        reply_markup=KEYBOARD_YES_OR_NO,
    )
    return SKILLS


def skills(update: Update, context: CallbackContext) -> int:
    field_name = 'skills'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    if user_answer == 'Нет':
        context.user_data['success'] = False

    update.message.reply_text('Укажите ваш стаж работы дизайнером (в месяцах):')
    return EXPERIENCE


def experience(update: Update, context: CallbackContext) -> int:
    field_name = 'experience'
    user = update.message.from_user
    user_answer = int(update.message.text)
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    if user_answer < 12:
        context.user_data['success'] = False

    update.message.reply_text('Пришлите ссылку на портфолио:')
    return PORTFOLIO


def portfolio(update: Update, context: CallbackContext) -> int:
    field_name = 'portfolio'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )

    update.message.reply_text(
        'Готовы ли вы к работе на полную занятость в нашей компании? (5-8ч/день)',
        reply_markup=KEYBOARD_YES_OR_NO,
    )

    return FULL_DAY


def full_day(update: Update, context: CallbackContext) -> int:
    field_name = 'full_day'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    if user_answer == 'Нет':
        context.user_data['success'] = False
    
    update.message.reply_text('Предпочитаемый уровень зарплаты:')
    return SALARY


def salary(update: Update, context: CallbackContext) -> int:
    field_name = 'salary'
    user = update.message.from_user
    user_answer = int(update.message.text)
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )
    if user_answer > 70000:
        context.user_data['success'] = False

    update.message.reply_text('Из какого источника вы узнали о вакансии?')
    return SOURCE


def source(update: Update, context: CallbackContext) -> int:
    field_name = 'source'
    user = update.message.from_user
    user_answer = update.message.text
    context.user_data[field_name] = user_answer
    log_user_info(
        user_nickname=user.username,
        field_name=field_name,
        value=user_answer,
    )

    update.message.reply_text('Спасибо за ответы!')
    if context.user_data['success']:
        update.message.reply_text('Мы приглашаем вас на собеседование!')
    else:
        update.message.reply_text('К сожалению, вы нам не подходите')

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.',
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    updater = Updater(os.getenv('TOKEN'))

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIO: [MessageHandler(Filters.text & ~Filters.command, fio)],
            AGE: [MessageHandler(Filters.regex(r'^(\d+)$'), age)],
            CITY: [MessageHandler(Filters.text & ~Filters.command, city)],
            PHONE: [MessageHandler(Filters.regex(r'^(\d{11})$'), phone)],
            MAIL: [MessageHandler(Filters.regex(r'^[\w\-]+@\w+\.\w+$'), mail)],
            EDUCATION: [MessageHandler(Filters.regex('^(Да|Нет)$'), education)],
            SKILLS: [MessageHandler(Filters.regex('^(Да|Нет)$'), skills)],
            EXPERIENCE: [MessageHandler(Filters.regex(r'^(\d+)$'), experience)],
            PORTFOLIO: [MessageHandler(Filters.text & ~Filters.command, portfolio)],
            FULL_DAY: [MessageHandler(Filters.regex('^(Да|Нет)$'), full_day)],
            SALARY: [MessageHandler(Filters.regex(r'^(\d+)$'), salary)],
            SOURCE: [MessageHandler(Filters.text & ~Filters.command, source)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
