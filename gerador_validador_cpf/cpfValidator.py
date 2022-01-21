from resources.validator import validar
from resources.generator import generate, format_cpf

if __name__ == '__main__':
    print(validar('488.611.340-09'))
    cpf = generate()
    cpf_formado = format_cpf(cpf)
    print(cpf, cpf_formado)