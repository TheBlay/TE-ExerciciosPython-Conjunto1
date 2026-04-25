# While com break
cont = 0
while True:
    print("Valor do contador> ",cont)
    cont += 1 # cont = cont + 1
    if cont == 5:
        print ("Contador....", cont)
        break
    print("Dentro do loop...")

print ("Fora do Loop")
