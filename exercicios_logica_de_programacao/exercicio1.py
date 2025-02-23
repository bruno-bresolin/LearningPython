"""
Fazer um programa para ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
Calcule e mostre o valor a ser pago.
"""

codigo_roupa, quantiade_roupa, preco_roupa = input().split()
codigo_roupa = int(codigo_roupa)
quantiade_roupa = int(quantiade_roupa)
preco_roupa = float(preco_roupa)


codigo_roupa2, quantiade_roupa2, preco_roupa2 = input().split()
codigo_roupa2 = int(codigo_roupa2)
quantiade_roupa2 = int(quantiade_roupa2)
preco_roupa2 = float(preco_roupa2)

valor_roupa1 = quantiade_roupa * preco_roupa
valor_roupa2 = quantiade_roupa2 * preco_roupa2

valor_total = valor_roupa1 + valor_roupa2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")

