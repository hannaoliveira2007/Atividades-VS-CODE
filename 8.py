#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela
# os valores em ordem decrescente.

a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))

ordem = [a , b , c]
ordem.sort(reverse= True)
print(ordem)