print("Olá")
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
print("Olá",nome,"sua idade é:",idade)
if idade > 60:
    # indentação é importante
    print("Você é idoso")
elif idade > 45:
    print("Você é quase idoso")
else:
    print("Você não é idoso")
print("Fora do if")

