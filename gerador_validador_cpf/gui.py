import tkinter as tk
import cpfValidator

root = tk.Tk()

def validate_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = stringvar.get()
    if cpfValidator.validar(cpf):
        button.config(
            text='OK', activeforeground='green', foreground='green'
        )
    else:
        button.config(
            text='Inválido', activeforeground='red', foreground='red'
        )


def generate_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = cpfValidator.generate()
    cpf_formatado = cpfValidator.format_cpf(cpf)
    stringvar.set(cpf_formatado)

main_title = tk.Label(root, text='Gerador/Validador CPF', background='#fff', font=('Helvetica', 12, 'bold'))
main_title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

validate_label = tk.Label(root, text='Validar:', background='#fff', font=('Helvetica', 12, 'bold'))
validate_label.grid(row=1, column=0)

validate_stringvar = tk.StringVar()
validate_entry = tk.Entry(root, textvariable=validate_stringvar, highlightthickness=1)
validate_entry.grid(row=1, column=1, pady=10)

validate_button = tk.Button(root, text='Validar')
validate_button.grid(row=1, column=2, sticky='ew')
validate_button.config(command=lambda: validate_cpf(
    validate_stringvar,
    validate_button
))

generate_label = tk.Label(root, text='Gerar:', background='#fff', font=('Helvetica', 12, 'bold'))
generate_label.grid(row=2, column=0)

generate_stringvar = tk.StringVar()
generate_entry = tk.Entry(root, textvariable=generate_stringvar, highlightthickness=1)
generate_entry.grid(row=2, column=1, pady=10)

generate_button = tk.Button(root, text='Gerar CPF')
generate_button.grid(row=2, column=2, sticky='ew')
generate_button.config(command=lambda: generate_cpf(
    generate_stringvar,
    generate_button
))

root.title('Gerador/Validador CPF')
root.config(background='#fff', padx=20, pady=20)
root.mainloop()