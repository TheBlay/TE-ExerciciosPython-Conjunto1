# Henrique Blay Barboza - RA: 1290482612001

# O usuário informa qual o número que deseja que seja mostrada a tabuada

def validaNumero(valor):
    while True:
        try:
            numero = float(input(valor).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido: digite um número.")
        else:
            return numero
        
numero = validaNumero("Digite o número para a tabuada: ")

print(f"Tabuada do {numero}:")
for i in range(1, 11): # range é uma função que gera uma sequência de números, do primeiro ao número logo antes do último (tipo um loop "for" com contador)
    print(f"{numero} x {i} = {numero * i}")