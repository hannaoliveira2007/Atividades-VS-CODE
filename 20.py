#- Faça um algoritmo que receba um valor inteiro e imprima na tela a sua
# tabuada

valor = int(input("Digite um valor inteiro: "))

for i in range(1, valor+1):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")