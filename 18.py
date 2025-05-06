#Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem
#1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e
#imprima na tela em quantos anos serão necessários para que Sara seja maior
#que Francisco

francisco = 150
sara = 110
anos = 0

while sara <= francisco:
    francisco += 2
    sara += 3
    anos += 1

print("Serão necessários", anos, "anos para que Sara seja maior que Francisco.")
