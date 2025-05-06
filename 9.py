#- Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma
# pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo
# com a tabela abaixo:
# Fórmula do IMC = peso / (altura) ²
# Tabela Condições IMC
# Abaixo de 18,5 | Abaixo do peso
# Entre 18,6 e 24,9 | Peso ideal (parabéns)
# Entre 25,0 e 29,9 | Levemente acima do peso
# Entre 30,0 e 34,9 | Obesidade grau I
# Entre 35,0 e 39,9 | Obesidade grau II (severa)
# Maior ou igual a 40 | Obesidade grau III (mórbida)

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

imc = peso / altura**2

if 18.5 >= imc:
    print("Abaixo do peso")

if 18.6 <= imc <= 24.9:
    print("Peso ideal, parabéns!")

if 25 <= imc <= 29.9:
    print("Levemente acima do peso")

if 30 <= imc <= 34.9:
    print("Obesidade grau I")

if 35 <= imc <= 39.9:
    print("Obesidade grau II")

if imc >= 40:
    print("Obesidade grau III")