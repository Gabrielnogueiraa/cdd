from biblioteca import adicao
qtd = int(input("quantos numeros você deseja digitar? "))
l = []
for x in range(qtd):
    l.append(int(input(f"digite o {x+1}° numero: ")))
soma = adicao(l)
print(f"a soma dos números é igual a: {soma}")
