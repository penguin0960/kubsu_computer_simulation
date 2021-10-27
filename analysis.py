from typing import Dict, Union

from data import WEIGHTS


def is_success(user_data: Dict[str: Union[str, int]]):
    result = 0
    for key, value in user_data.items():
        result += value * WEIGHTS[key]

    return result
