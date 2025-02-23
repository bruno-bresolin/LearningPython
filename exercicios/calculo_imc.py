from tkinter import *

nome = "Bruno"
altura = 1.82
peso = 85
imc =  0

def calcular_imc():
    global imc
    imc = peso / (altura ** 2)
    print(f"O IMC do {nome} é {imc}")
    label.config(text=f"O IMC de {nome} é: {imc:.2f}") 
    

root = Tk()

root.title("Calculo IMC")
root.geometry("400x400")
root.resizable(False, False)

button = Button(text="Calcular!", command=calcular_imc, height=4, width=20)
button.pack()

label = Label(root, text=imc,)
label.pack()



root.mainloop()