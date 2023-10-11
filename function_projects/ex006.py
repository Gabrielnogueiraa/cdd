from biblioteca import adicao
l = []
while True:
    l.append(float(input("digite o numero que você quer que some: ")))
    perg = input("você quer digitar outro numero para somar? (s/n): ")
    if perg.lower() != "s":
        break
soma = adicao(l)
print(f"a soma total dos números é igual a: {soma}")
