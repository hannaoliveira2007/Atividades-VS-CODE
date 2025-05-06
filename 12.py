#- Faça um algoritmo que leia o valor de um produto e determine o valor que
# deve ser pago, conforme a escolha da forma de pagamento pelo comprador e
# imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela
# de condições de pagamento para efetuar o cálculo adequado.
# Tabela de Código de Condições de Pagamento
# 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
# 2 - À Vista no cartão de crédito, recebe 10% de desconto
# 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
# 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%

print("A tabela de pagamentos e condições é: ")
print(20*"-")
print("1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto")
print("2 - À Vista no cartão de crédito, recebe 10% de desconto") 
print("3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros") 
print("4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%")
print(20*'-')

valor = float(input("Diga o valor do produto: "))

opcao = int(input("Qual dos números você escolhe? "))

if opcao == 1:
    print("O valor a ser pago é R$ ", valor+(valor*0.15))
elif opcao == 2:
    print("O valor a ser pago é R$ ", valor+(valor*0.1))
elif opcao == 3:
    print("O valor a ser pago em cada parcela é R$ ", valor/2, "totalizando", valor)
elif opcao == 4:
    print("O valor a ser pago em cada parcela é R$ ", (valor+(valor*0.1))/3, "totalizando R$ ", (valor+(valor*0.1)))
