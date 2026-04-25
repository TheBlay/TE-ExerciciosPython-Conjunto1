print("=======> Formatação Strings <========")
# Formatando Strings
# Entrada de dados - input
# Saída de dados - print
nome = input("Digite o seu nome: ")
print ("Olá,",nome)
idade = input("Digite a sua idade: ")
print ("Sua idade é",idade)

print("Meu nome é",nome,"e eu tenho",idade,"anos.")

# Usando f-strings (a partir do Python 3.6)
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Usando str.format()
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
