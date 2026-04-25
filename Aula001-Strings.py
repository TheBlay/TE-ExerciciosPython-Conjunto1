# Variáveis:
inteiro = 10
decimal = 10.4
texto = "Olá"
texto2 = 'Olá'
booleano = True # ou False

# Manipulação de Strings
texto = "Python"
#      -1012345
s1 = 'Olá, mundo!'
s2 = "Python é incrível!"
s3 = '''Essa é uma
string de múltiplas
linhas.'''

print(s3.upper()) # Retorna a string em maiúsculas
print(s2.lower()) # Retorna a string em minúsculas
print(texto[0])  # P
print(texto[-1])  # n (índice negativo conta de trás para frente)

# Fatiamento de Strings (Slicing) -> sintaxe string[início:fim:passo].
print(texto[0:3])   # "Pyt" (do índice 0 até 2)
print(texto[1:])    # "ython" (do índice 1 até o final)
print(texto[:4])    # "Pyth" (do começo até o índice 3)
print(texto[::2])   # "Pto" (passo 2, pegando de 2 em 2)

# Concatenando Strings
somastring = s1 + " + " + s2  # "Olá, mundo! + Python é incrível!"
print(somastring)

# Repetindo String
print(texto * 3)  # "PythonPythonPython"

print(len(texto)) # Retorna o tamanho da string
print("  ..Python..   ".strip()) # Remove espaços em branco no início e no final da string.

# Substitui todas as ocorrências de old por new: .replace(old,new)
print(s2.replace("incrível", "Python"))

# Divide a string em uma lista usando o separador sep .split(sep)
print(s2.split())

# Retorna o índice da primeira ocorrência da substring sub,
# ou -1 se não for encontrado.
print(s2.find("w"))

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

print ("Análise do IF......")
# Entrada de dados com conversão de dados para inteiro
idadenova = int(input("Digite a sua idade: "))
idadenova = idadenova + 5
print (nome,"sua nova idade é",idadenova)

# Condicionais (if, elif, else)
if idadenova >= 18:
    print (nome,"você é adulto")
    print ("Ainda estou analisando idade >= 18")
elif idadenova >= 13:
    print (nome, "você é Adolescente")
else:
    print (nome, "você é criança")
print("Acabamos!")
