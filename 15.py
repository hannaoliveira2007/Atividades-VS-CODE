#- Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na
#  tela quantos anos, meses e dias essa pessoa ja viveu. Leve em
# consideração o ano com 365 dias e o mês com 30 dias.
# (Ex: 5 anos, 2 meses e 15 dias de vida)

ano = int(input("Ano em que você nasceu: "))

anos = 2025 - ano
meses = 12 * anos
dias = meses * 30

print(f"Você já viveu {anos} anos, ou {meses} meses, ou {dias} dias.")