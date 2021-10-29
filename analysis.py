from typing import Dict

from data import (
    WEIGHTS,
    SALARY,
    AGE,
    MAX_SALARY,
    MAX_AGE,
    SUCCESS_INTERVIEW_RATING,
    YES_NO_VALUES,
    EXPERIENCE,
    MIN_EXPERIENCE,
)
from logger import logger


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
    calculate_rating_history = []
    for key, value in formatted_answers.items():
        current_weight = WEIGHTS[key]
        rating += value * current_weight
        calculate_rating_history.append(' {value} * {weight} [{key}]'.format(
            value=value,
            weight=current_weight,
            key=key,
        ))

    logger.info('rating =' + ' +'.join(calculate_rating_history))
    return rating


def format_answers(answers: Dict[str, str]) -> Dict[str, int]:
    result = {}
    for key, value in answers.items():
        if key == SALARY:
            result[key] = MAX_SALARY - int(value)
        elif key == AGE:
            result[key] = MAX_AGE - int(value)
        elif key == EXPERIENCE:
            result[key] = int(value) - MIN_EXPERIENCE
        else:
            result[key] = YES_NO_VALUES[value] if (value in YES_NO_VALUES) else int(value)

    return result
