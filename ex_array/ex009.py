print("cadastro de usuario e senha: ")
a = [""] * 1
b = [""] * 1
for i in range(1):
    a[i] = input("cadastre seu nome: ")
    b[i] = input("cadastre a sua senha: ")
print()
print("agora faça o login: ")
nome = input("digite o seu nome: ")
senha = input("digite a sua senha: ")

while senha != b[0]:
    senha = input("a senha é invalida.\ndigite a senha novamente: ")
else:
    print(f"bem vindo {nome}, login concluido com sucesso. ")