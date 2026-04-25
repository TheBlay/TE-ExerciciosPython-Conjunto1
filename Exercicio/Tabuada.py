# Henrique Blay Barboza - RA: 1290482612001
# Veja também pelo GitHub! => https://github.com/TheBlay/TE-ExerciciosPython-Conjunto1

# O usuário informa qual o número que deseja que seja mostrada a tabuada

def validaNumero(valor):
    while True:
        try:
            numero = float(input(valor).strip().replace(",", "."))
            if numero.is_integer(): # Como o nome diz, is_integer() checa se é um numero inteiro, poupando os decimais se o usuário não digitar um float
                numero = int(numero)
        except ValueError:
            print("Valor inválido: digite um número.")
        else:
            return numero
        
numero = validaNumero("Digite o número para a tabuada: ")

print(f"Tabuada do {numero}:")
for i in range(1, 11): # range é uma função que gera uma sequência de números, do primeiro ao número logo antes do último (tipo um loop "for" com contador)
    print(f"{numero} x {i} = {numero * i}")