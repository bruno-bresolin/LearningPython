import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

a = round(a, 2)
b = round(b, 2)
c = round(c, 2)

print(a, b, c)

delta = (b ** 2) - (4 * a * c)



if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a) 
    print(f"X1 {x1}")
    print(f"X2 {x2}")

print(delta)