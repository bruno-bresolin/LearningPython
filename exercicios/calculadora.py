# função calcular
def calculadora():

    print("Digite os números:")

    num1 = float(input())
    num2 = float(input())

    print("Digite 1 para adicao (+)")
    print("Digite 2 para subtracao (-)")
    print("Digite 3 para multiplicacao (*)")
    print("Digite 4 para divisao (/)")

    print("Por favor selecione: 1/2/3/4")

    user_input = input()

    if (user_input == "1"):
        print(f"o resultado {num1 + num2}")

    if (user_input == "2"):
        print(f"o resultado {num1 - num2}")

    if (user_input == "3"):
        print(f"o resultado {num1 * num2}")

    if (user_input == "4"):

        resultado = num1 / num2

        try: print(f"o resultado {resultado}")
        except ZeroDivisionError:
            print("Erro: não é possível dividir por zero")

calculadora()

        