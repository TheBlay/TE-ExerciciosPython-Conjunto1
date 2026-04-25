# Henrique Blay Barboza - RA: 1290482612001
# Veja também pelo GitHub! => https://github.com/TheBlay/TE-ExerciciosPython-Conjunto1

# Peça uma temperatura em Celsius e a converta para Fahrenheit
# F = (C * 9/5) + 32

def validaTemperatura(temperatura):
    while True:
        try:
            temperatura = float(input(temperatura))
        except ValueError:
            print("Valor inválido: digite um número.")
        else:
            return temperatura
        
temperatura_celsius = validaTemperatura("Digite a temperatura em Celsius: ")
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit}")