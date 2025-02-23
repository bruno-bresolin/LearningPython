senha_correta = 2022

# Inicia o loop para pedir a senha
while True:
    senha = int(input("Digite a senha: "))
    
    if senha == senha_correta:
        print("Acesso Concedido")
        break  # Sai do loop quando a senha estiver correta
    else:
        print("Acesso Negado. Tente novamente.")
