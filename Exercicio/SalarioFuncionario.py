# Henrique Blay Barboza - RA: 1290482612001

# Peça o salário de um funcionário e calcule um aumento de 10%


def validaValor(valor):
    while True:
        try:
            try: # Esse tenta atribuir e dispara um raise com msg diferente para cada condição de erro. O except fora do bloco que exibe o erro adequado
                resultado = float(input(valor).strip().replace(",", "."))
            except ValueError:
                    raise ValueError("Digite um número.")
            
            if resultado <= 0:  
                    raise ValueError("Digite um valor maior que zero.")
            
            return resultado
    
        except ValueError as e:
            print(f"Valor inválido: {e}")
        
            
        
aumento = 0.10
        
salario = validaValor("Digite o salário do funcionário: ")

novoSalario = salario + (salario * aumento)
print(f"O novo salário do funcionário é R${novoSalario:.2f}")