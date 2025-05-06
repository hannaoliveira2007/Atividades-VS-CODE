#Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na
# tela a soma entre A e B é mostre se a soma é menor que C.

a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))

print(f"{a} + {b} = ", a+b)
if a+b < c:
    print("A soma de a + b é menor que c")
elif a+b == c:
    print("A soma de a+b é igual a c")
else:
    print("A soma de a+b é maior que c")
