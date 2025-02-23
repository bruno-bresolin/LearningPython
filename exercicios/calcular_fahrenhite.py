# importar bibliotecas
from tkinter import *

root = Tk()

# função converter celsius em fahrenhite
fahrenhite = Entry(root)
fahrenhite.pack()
fahrenhite.insert(0, "")

# Função para converter Fahrenheit para Celsius
def conversao():
    try:
        temp_f = float(fahrenhite.get())  # Obtém o valor do Entry e converte para float
        celsius = (temp_f - 32) * 5/9  # Converte para Celsius
        label.config(text=f"A conversão é de {celsius:.2f}°C")  # Atualiza o Label
    except ValueError:
        label.config(text="Entrada inválida!") 

root.geometry("400x400")

button = Button(text="Calcular", command=conversao)
button.pack()

label = Label(text="converao:")
label.pack()



root.mainloop()

