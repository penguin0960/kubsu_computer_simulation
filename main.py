import os
from typing import Union

from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from analysis import is_success_interview
from data import FIO, AGE, CITY, PHONE, MAIL, EDUCATION, SKILLS, EXPERIENCE, PORTFOLIO, FULL_DAY, SALARY, SOURCE, \
    STATES_ORDER, StateType, QUESTION_MESSAGES
from logger import logger


def log_user_info(user_nickname: str, field_name: str, value: Union[str, int]) -> None:
    logger.info('{user_nickname}.{field_name} = {value}'.format(
        user_nickname=user_nickname,
        field_name=field_name,
        value=value,
    ))


def get_next_state(current_state: StateType) -> StateType:
    if current_state == len(STATES_ORDER) - 1:
        return ConversationHandler.END

    return STATES_ORDER[STATES_ORDER.index(current_state) + 1]


def start(update: Update, context: CallbackContext) -> StateType:
    """Starts the conversation and asks the user about their gender."""
    update.message.reply_text(
        'Здравствуйте!\n'
        'Чтобы перестать общаться со мной, нажмите /cancel.'
    )
    context.user_data['answers'] = {}
    next_state = STATES_ORDER[0]
    update.message.reply_text(**QUESTION_MESSAGES[next_state])
    context.user_data['state'] = next_state
    return next_state


def get_answer(update: Update, context: CallbackContext) -> StateType:
    user = update.message.from_user
    answer = update.message.text
    user_data = context.user_data
    current_state = user_data['state']
    user_data['answers'][current_state] = answer
    log_user_info(
        user_nickname=user.username,
        field_name=current_state,
        value=answer,
    )
    next_state = get_next_state(current_state)

    if next_state != ConversationHandler.END:
        update.message.reply_text(**QUESTION_MESSAGES[next_state])
        user_data['state'] = next_state
        return next_state

    update.message.reply_text('Спасибо за ответы!')
    if is_success_interview(
        username=user.username,
        answers=user_data['answers'],
    ):
        update.message.reply_text('Мы приглашаем вас на собеседование!')
    else:
        update.message.reply_text('К сожалению, вы нам не подходите')

    return next_state


def cancel(update: Update, context: CallbackContext) -> StateType:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.',
        reply_markup=ReplyKeyboardRemove(),
    )
    context.user_data.clear()

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    updater = Updater(os.getenv('TOKEN'))

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIO: [MessageHandler(Filters.text & ~Filters.command, get_answer)],
            AGE: [MessageHandler(Filters.regex(r'^(\d+)$'), get_answer)],
            CITY: [MessageHandler(Filters.text & ~Filters.command, get_answer)],
            PHONE: [MessageHandler(Filters.regex(r'^(\d{11})$'), get_answer)],
            MAIL: [MessageHandler(Filters.regex(r'^[\w\-]+@\w+\.\w+$'), get_answer)],
            EDUCATION: [MessageHandler(Filters.regex('^(Да|Нет)$'), get_answer)],
            SKILLS: [MessageHandler(Filters.regex('^(Да|Нет)$'), get_answer)],
            EXPERIENCE: [MessageHandler(Filters.regex(r'^(\d+)$'), get_answer)],
            PORTFOLIO: [MessageHandler(Filters.text & ~Filters.command, get_answer)],
            FULL_DAY: [MessageHandler(Filters.regex('^(Да|Нет)$'), get_answer)],
            SALARY: [MessageHandler(Filters.regex(r'^(\d+)$'), get_answer)],
            SOURCE: [MessageHandler(Filters.text & ~Filters.command, get_answer)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
