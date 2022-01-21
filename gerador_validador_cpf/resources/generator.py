from random import randint
from resources.validator import get_digit_one, get_digit_two

def generate() -> str:
    nine_digits = ''.join(str(randint(0,9)) for x in range(9))
    digit_one = get_digit_one(nine_digits)
    digit_two = get_digit_two(f'{nine_digits}{digit_one}')
    new_cpf = f'{nine_digits}{digit_one}{digit_two}'
    return new_cpf

def format_cpf(cpf: str) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'