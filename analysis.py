from typing import Dict

from data import WEIGHTS, SALARY, AGE, MAX_SALARY, MAX_AGE
from logger import logger

SUCCESS_INTERVIEW_RATING = 0
YES_NO_VALUES = {
    'Да': 1,
    'Нет': 0,
}


def is_success_interview(username: str, answers: Dict[str, str]) -> bool:
    user_rating = calculate_rating(answers)
    logger.info('{username} rating = {rating}'.format(
        username=username,
        rating=user_rating,
    ))
    return user_rating > SUCCESS_INTERVIEW_RATING


def calculate_rating(answers: Dict[str, str]) -> int:
    important_answers = {
        key: value
        for key, value in answers.items()
        if key in WEIGHTS
    }
    formatted_answers = format_answers(important_answers)
    rating = 0
    for key, value in formatted_answers.items():
        rating += value * WEIGHTS[key]

    return rating


def format_answers(answers: Dict[str, str]) -> Dict[str, int]:
    result = {}
    for key, value in answers.items():
        if key == SALARY:
            result[key] = MAX_SALARY - int(value)
        elif key == AGE:
            result[key] = MAX_AGE - int(value)
        else:
            result[key] = YES_NO_VALUES[value] if (value in YES_NO_VALUES) else int(value)

    return result
