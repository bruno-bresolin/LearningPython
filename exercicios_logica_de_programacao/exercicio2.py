"""
Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro
casas decimais conforme exemplos.
Fórmula:  = .  
Considere o valor de π = 3.14159
"""

raio = float(input())
pi = 3.14159

raio = round(raio, 2)

area = pi * raio ** 2

print(f"{area:.4f}")