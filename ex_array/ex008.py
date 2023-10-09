a = [""] * 5
b = [""] * 5
for x in range(0, 5):
    a[x] = input("digite seu nome: ")
    b[x] = input("digite sua senha: ")
for i in range(0, 5):
    print(f"nome: {a[i]}\nsenha: {b[i]}\nposição: {i}")
    print()
