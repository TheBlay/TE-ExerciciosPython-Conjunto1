# Henrique Blay Barboza - RA: 1290482612001

# Calcule a média ponderada de 3 notas informadas pelo usuário, sendo:
# P1 peso 4, P2 peso 4 e T peso 2
# Se média > 6: aprovado
# media = (P1 * 4 + P2 * 4 + T * 2) / (4 + 4 + 2) <-(pesos) daria pra trabalhar com constantes nos pesos
P1_PESO = 4
P2_PESO = 4
T_PESO = 2

# Transformei a validação em função pra evitar amontoar um monte de código igual
def validaNota(nota):
    while True:
        try:
            try:
                nota = float(input(nota).strip().replace(",", "."))
            except ValueError:
                raise ValueError("Digite um número.")
            if not 0 <= nota <= 10:
                raise ValueError("Digite um valor entre 0 e 10.")
            
            return nota
        except ValueError as e:
                print(f"Valor inválido: {e}")
        

nota1 = validaNota("Digite a nota da P1: ")
nota2 = validaNota("Digite a nota da P2: ")
notaTP = validaNota("Digite a nota de Trabalho: ")

mediaFinal = (nota1 * P1_PESO + nota2 * P2_PESO + notaTP * T_PESO) / (P1_PESO + P2_PESO + T_PESO)
# aprendi formatação de string literal em PHP no estágio no meu projeto e to testando nesses exercícios, mt mió!
print(f"Média Final: {mediaFinal:.1f}")
if mediaFinal > 6:
    print("Passou!")
elif mediaFinal == 6:
    print("Passou por pouco!")
else:
    print("Rodou :c")