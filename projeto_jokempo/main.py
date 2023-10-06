print("JOGO PEDRA, PAPEL E TESOURA!!")
c1 = 0
c2 = 0
loop = "s"
while loop.lower() == "s":
    for x in range(3):
        j1 = input("considere m1 = pedra, m2 = papel e m3 = tesoura. agora digite a sua escolha: ")
        j2 = input("considere m1 = pedra, m2 = papel e m3 = tesoura. agora digite a sua escolha: ")
        if (j1 == "m1" and j2 == "m3") or (j1 == "m2" and j2 == "m1") or (j1 == "m3" and j2 == "m2"):
            c1 += 1
            print("o jogador n°1 ganhou essa rodada.")
        elif (j1 == "m1" and j2 == "m2") or (j1 == "m2" and j2 == "m3") or (j1 == "m3" and j2 == "m1"):
            c2 += 1
            print("o jogador n°2 ganhou essa rodada.")
        elif (j1 == "m1" and j2 == "m1") or (j1 == "m2" and j2 == "m2") or (j1 == "m3" and j2 == "m3"):
            print("essa rodada foi empate.")
    if c1 >= 2 or (c1 == 1 and c2 == 0):
        print("o jogador n°1 ganhou a melhor de 3!!")
    elif c2 >= 2 or (c2 == 1 and c1 == 0):
        print("o jogador n°2 ganhou a melhor de 3!!")
    else:
        print("o jogo foi empate!!")
    loop = input("você deseja jogar novamente? (s/n): ")
    if loop.lower() != "s":
        break
print("programa finalizado")
