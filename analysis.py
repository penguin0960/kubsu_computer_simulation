from typing import Dict, Union

from data import WEIGHTS

SUCCESS_INTERVIEW_RATING = 0
YES_NO_VALUES = {
    'Да': 1,
    'Нет': 0,
}


def is_success_interview(answers: Dict[str: str]) -> bool:
    return calculate_rating(answers) > SUCCESS_INTERVIEW_RATING


def calculate_rating(answers: Dict[str: str]) -> int:
    important_answers = {
        key: value
        for key, value in answers.items
        if key in WEIGHTS
    }
    formatted_answers = format_answers(important_answers)
    rating = 0
    for key, value in formatted_answers.items():
        rating += value * WEIGHTS[key]

    return rating


def format_answers(answers: Dict[str: str]) -> Dict[str: int]:
    result = {}
    for key, value in answers.items():
        result = YES_NO_VALUES[value] if value in YES_NO_VALUES else int(value)

    return result
