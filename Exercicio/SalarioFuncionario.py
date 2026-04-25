# Henrique Blay Barboza - RA: 1290482612001

# Peça o salário de um funcionário e calcule um aumento de 10%

def validaValor(valor):
    while True:
        try:
            resultado = float(input(valor))
        except ValueError:
            print("Valor inválido: digite um número.")
        else:
            return resultado
        
aumento = 0.10
        
salario = validaValor("Digite o salário do funcionário: ")

novoSalario = salario + (salario * aumento)
print(f"O novo salário do funcionário é R${novoSalario:.2f}")