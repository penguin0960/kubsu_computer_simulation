from keyboards import KEYBOARD_YES_OR_NO

StateType = int
FIO, AGE, CITY, PHONE, MAIL, EDUCATION, SKILLS, EXPERIENCE, PORTFOLIO, FULL_DAY, SALARY, SOURCE = range(12)
# FIO, AGE, CITY, PHONE, MAIL, EDUCATION, SKILLS, EXPERIENCE, PORTFOLIO, FULL_DAY, SALARY, SOURCE = (
#     'fio',
#     'age',
#     'city',
#     'phone',
#     'mail',
#     'education',
#     'skills',
#     'experience',
#     'portfolio',
#     'full_day',
#     'salary',
#     'source',
# )
STATES_ORDER = (
    FIO,
    AGE,
    CITY,
    PHONE,
    MAIL,
    EDUCATION,
    SKILLS,
    EXPERIENCE,
    PORTFOLIO,
    FULL_DAY,
    SALARY,
    SOURCE,
)
QUESTION_MESSAGES = {
    FIO: {
        'text': 'Введите ваше ФИО:',
    },
    AGE: {
        'text': 'Введите ваш возраст:',
    },
    CITY: {
        'text': 'Введите ваш город проживания:',
    },
    PHONE: {
        'text': 'Введите ваш номер телефона:',
    },
    MAIL: {
        'text': 'Введите ваш E-mail:',
    },
    EDUCATION: {
        'text': 'Есть ли у вас образование в сфере дизайна?',
        'reply_markup': KEYBOARD_YES_OR_NO,
    },
    SKILLS: {
        'text': 'Умеете ли вы работать в Adobe Illustrator и Photoshop?',
        'reply_markup': KEYBOARD_YES_OR_NO,
    },
    EXPERIENCE: {
        'text': 'Укажите ваш стаж работы дизайнером (в месяцах):',
    },
    PORTFOLIO: {
        'text': 'Пришлите ссылку на портфолио:',
    },
    FULL_DAY: {
        'text': 'Готовы ли вы к работе на полную занятость в нашей компании? (5-8ч/день)',
        'reply_markup': KEYBOARD_YES_OR_NO,
    },
    SALARY: {
        'text': 'Предпочитаемый уровень зарплаты:',
    },
    SOURCE: {
        'text': 'Из какого источника вы узнали о вакансии?',
    },
}
WEIGHTS = {
    AGE: 0,
    EDUCATION: 0,
    SKILLS: 0,
    EXPERIENCE: 0,
    FULL_DAY: 0,
    SALARY: 0,
}
