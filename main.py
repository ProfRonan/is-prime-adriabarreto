numero = int(input("Digite um número inteiro: "))
numero = int(numero)
if numero <= 0:
    print("Número inválido")
if numero == 1: 
    print("Não primo")
else: 
    for i in range(2,numero):
        if numero % i == 0:
            print("Não primo")
            break
    else: 
         print("Primo")
