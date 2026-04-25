# Henrique Blay Barboza - RA: 1290482612001

# Calculadora simples:
# Peça 2 números
# Uma operação (+, -, *, /)
# Exiba o resultado
# Continue em loop até que o usuário indique o final da operação

def validaNumero(valor):
    while True:
        try:
            numero = float(input(valor).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido: digite um número.")
        else:
            return numero
        
def validaOperacao(valor):
    while True:
        operacao = input(valor).strip()
        if operacao in ["+", "-", "*", "/"]:
            return operacao
        else:
            print("Operação inválida: digite uma operação válida (+, -, *, /).")

while True:
    num1 = validaNumero("Digite o primeiro número: ")
    num2 = validaNumero("Digite o segundo número: ")
    operacao = validaOperacao("Digite a operação (+, -, *, /): ")

    match operacao:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero não é permitida.")
                continue

    print(f"Resultado: {resultado}")

    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if continuar != "s":
        print("Encerrando a calculadora. Valeu!")
        break