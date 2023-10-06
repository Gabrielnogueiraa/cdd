def somar(n1,n2):
    soma = n1 + n2
    print(f"a soma dos dois numeros é igual a {soma}")

def subtrair(n1,n2):
    sub = n1 - n2
    print(f"a subtração dos dois numeros é igual a {sub}")

def multiplicar(n1,n2):
    mult = n1 * n2
    print(f"a multplicação dos dois numeros é igual a {mult}")

def dividir(n1,n2):
    div = n1 / n2
    print(f"a divisão dos dois numeros é igual a {div}")

def ex001(n1):
    for i in range(1, n1 + 1):
        print((str(i) + " ") * i)

def ex002(n):
    a = " "
    for i in range(1, n + 1):
        a += str(i)
        print(a)

def ex003(txt):
    vogais = 0
    branco = 0
    for x in txt:
        if x in "AaEeIiOoUu":
            vogais += 1
        if x in " ":
            branco += 1
    print(f"o texto digitado tem {vogais} vogais e {branco} espaços em branco.")
