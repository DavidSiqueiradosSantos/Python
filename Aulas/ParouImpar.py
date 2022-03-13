from random import randint

nome = str(input("Nome do jogador: "))

b = 0
computador = randint(0, 10)
jogador = str(input("Escolha par ou impar: "))

if jogador == "par":
    par = jogador
    impar = computador
    print("Computador será 'impar' ")
    print("==" * 20)

elif jogador == "impar":
    impar = jogador
    par = computador
    print("Computador será 'par' ")
    print("==" * 20)

else:
    b = 1
    print("ERRO")

if b != 1:

    numero = int(input("Vez do Jogador {}!\nEscolha um número de (0/10): ".format(nome)))
    while numero > 10:
        if numero >= 10:
            numero = int(input("Escolha um número de (0/10): "))

    print(nome + " escolheu: {}".format(numero))
    print("\nComputador escolheu: {}".format(computador))

    total = numero + computador

    print("A Soma é: {}".format(total))
    computador = "0"

    if total % 2 == 0:
        print("O Resultado é: Par")
        computador = "par"
    else:
        print("O Resultado é: Impar")
        computador = "impar"
    if jogador == "par" and computador == "par":
        print()
        print("VENCEU O JOGADOR: ", nome + "!")
    elif jogador == "impar" and computador == "impar":
        print()
        print("VENCEU O JOGADOR: ", nome + "!")
    else:
        print()
        print("VENCEU O COMPUTADOR!")
