from biblioteca import media, resultado
name = input("digite o nome do aluno: ")
n1 = float(input("digite a primeira nota do aluno: "))
n2 = float(input("digite a segunda nota do aluno: "))
media = media(n1, n2)
resultado = resultado(name, media)
print(f"o aluno {resultado[0]} está {resultado[1]}, com media de: {media}")
