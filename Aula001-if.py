# Entrar com 2 notas P1 e P2, calcular a média e informar se está aprovado ou não
# Média >= 6 aprovado
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
print("N1 =",n1,"N2 =",n2,"Média =",media)
if media >= 6:
    print("Passou!")
else:
    print("Rodou!")
