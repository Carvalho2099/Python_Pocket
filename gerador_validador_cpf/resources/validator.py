import re

def get_digit(cpf: str) -> int:
    len_cpf = len(cpf) + 1
    multiplication = []
    for cpf_index, multiplier in enumerate(range(len_cpf, 1, -1)):
        multiplication.append(int(cpf[cpf_index]) * multiplier)
    total_sum = sum(multiplication)
    digit = 11 - (total_sum % 11)
    return digit if digit < 10 else 0

def get_digit_one(cpf: str) -> int:
    return get_digit(cpf[:9])

def get_digit_two(cpf: str) -> int:
    return get_digit(cpf[:10])

def somente_numeros(cpf: str) -> str:
    return re.sub(r'\D', '', cpf)

def caracteres_cpf(value: str) -> bool:
    return len(value) == 11

def is_sequence(value: str) -> bool:
    return (value[0] * len(value)) == value

def validar(cpf: str) -> bool:
    cpf_limpo = somente_numeros(cpf)

    if not caracteres_cpf(cpf_limpo):
        return False

    if is_sequence(cpf_limpo):
        return False

    digito_one = get_digit_one(cpf_limpo)
    digito_two = get_digit_two(cpf_limpo)
    new_cpf = f'{cpf_limpo[:9]}{digito_one}{digito_two}'

    if new_cpf == cpf_limpo:
        return True
    return False
