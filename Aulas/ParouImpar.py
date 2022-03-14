from random import randint

nome = str(input("Informe o nome do jogador: "))

escolha = str(input("VEZ DO JOGADOR!\n'IMPAR' OU 'PAR'? "))

computador = " "
jogador = " "
j = 0
c = 0


if escolha == "impar" or escolha == "IMPAR" or escolha == "Impar":
    jogador = "impar"
    computador = "par"
    print("O jogador {} será '{}'.".format(nome.upper(), jogador.upper()))
    print("O Computador será '{}'.".format(computador.upper()))
elif escolha == "par" or escolha == "PAR" or escolha == "Par":
    jogador = "par"
    computador = "impar"
    print("O jogador {} será '{}'.".format(nome.upper(), jogador.upper()))
    print("O Computador será '{}'.".format(computador.upper()))
else:
    print("Erro!")

cont = 1
while cont != 6:
    print("\nRodada", cont, "\n")

    numero = int(input("VEZ DO {}!\nEscolha um número de (0/10): ".format(nome).upper()))
    while numero > 10 or numero < 0:
        numero = int(input("VEZ DO {}!\nEscolha um número de (0/10): ".format(nome).upper()))

    compNumero = randint(0, 10)

    total = numero + compNumero

    if total % 2 == 0:
        print("Você jogou {}.".format(numero))
        print("O Computador jogou {}.".format(compNumero))
        print("O total é: {}.".format(total))
        print(total, "é 'Par!'")
        computador = 'par'
    else:
        print("Você jogou {}.".format(numero))
        print("O Computador jogou {}.".format(compNumero))
        print("O total é: {}.".format(total))
        print(total, "é Impar!")
        computador = 'impar'

    if jogador == "par" and computador == "par":
        print()
        print("VENCEU O JOGADOR:", nome.upper() + "!")
        j += 1
    elif jogador == "impar" and computador == "impar":
        print()
        print("VENCEU O JOGADOR:", nome.upper() + "!")
        j += 1
    else:
        print()
        print("VENCEU O COMPUTADOR!")
        c += 1

    if j >= 3:
        print("O jogador {}, venceu a partida com {} vitoria, escolhendo '{}'!".format(nome.upper(), j, jogador))
        break
    elif c >= 3:
        print("O computador venceu a partida com {} vitoria!".format(c))
        print("O jogador {}, perdeu a partida com {} vitoria!".format(nome.upper(), j, computador))
        break

    cont += 1







