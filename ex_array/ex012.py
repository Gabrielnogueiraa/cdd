nomes = [""] * 5
for x in range(5):
    nomes[x] = input(f"digite o {x +1 }ª nome: ")
print(nomes)
print(f"agora esses numeros na ordem inversa:")
for j in range(4, -1, -1):
    print(nomes[j])
