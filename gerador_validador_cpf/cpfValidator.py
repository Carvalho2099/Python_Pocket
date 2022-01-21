from resources.validator import validar
from resources.generator import generate, format_cpf

if __name__ == '__main__':
    validar(cpf)
    generate()
    format_cpf(cpf)