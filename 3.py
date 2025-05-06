#Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem 
# iguais, deverá somar os dois valores, caso contrário devera multiplicar A por B. Ao final 
# de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.

a = int(input("Valor 1: "))
b = int(input("Valor 2: "))

if a == b or b == a:
    print("A soma é: ", a + b)
else:
    print("A multiplicação é: ", a * b)
