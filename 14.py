#Faça um algoritmo que receba um valor A e B, e troque o valor de A por B
#e o valor de B por A e imprima na tela os valores.

a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")

print("Antes da troca:")
print("a =", a)
print("b =", b)

a, b = b, a

print("Depois da troca:")
print("a =", a)
print("b =", b)
