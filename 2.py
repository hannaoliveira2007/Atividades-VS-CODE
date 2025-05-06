#Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

x = float(input("Digite um número: "))

if x < 0:
    print("O número é negativo")
else:
    print("O número é positivo")

if x % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")