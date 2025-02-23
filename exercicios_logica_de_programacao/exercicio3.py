item, quantidade_item = input().split()

quantidade_item = int(quantidade_item)

valor = 0

if item == "1":
    valor = 4.00
elif item == "2":
    valor = 4.50
elif item == "3":
    valor = 5.00
elif item == "4":
    valor = 2.00
elif item ==  "5":
    valor = 1.50
else:
    print("Digite um item válido")

valor_total = valor * quantidade_item
print(valor_total)