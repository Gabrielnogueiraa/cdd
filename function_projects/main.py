from biblioteca import *

while True:
    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))
    perg = input("digite 1 para somar, 2 para subtrair, 3 para multiplicar, 4 para dividir e s para sair: ")
    if perg == "1":
        somar(n1, n2)
    elif perg == "2":
        subtrair(n1, n2)
    elif perg == "3":
        multiplicar(n1, n2)
    elif perg == "4":
        dividir(n1, n2)
    elif perg == "s":
        break
print("programa finalizado!")
