#Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a
#temperatura correspondente em grau Celsius. Imprima na tela as duas
#temperaturas.
#Fórmula: C = (5 * ( F-32) / 9)

f = float(input("Diga a temperatura em fahrenheit: "))

c = ((5 * ( f-32) )/ 9)

print("A temperatura em celsius é: ", c)