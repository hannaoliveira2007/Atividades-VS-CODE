#Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a
# média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi
# aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final
# deve ser maior ou igual a 7.

nome = input("Qual seu nome? ")
a = float(input("nota 1: "))
b = float(input("nota 2: "))
c = float(input("nota 3: "))
d = float(input("nota 4: "))

media = (a+b+c+d)/4
print("A sua média é: ", media )

if media >= 7:
    print(f"{nome} foi aprovado!")
else:
    print(f"{nome} foi reprovado :[")