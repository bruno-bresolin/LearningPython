import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Teste Tkinter")

def on_pressed():
    global contador
    contador += 1
    print(contador)
    label.config(text=f"Contador: {contador}") 

# Adiciona um rótulo
button = tk.Button(text="Clique", command=on_pressed)
button.pack()


label = tk.Label(root, text=f"Contador: {contador}")
label.pack()


# Inicia o loop principal da interface
root.mainloop()