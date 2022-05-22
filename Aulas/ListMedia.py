""" Escreva um algoritmo simples em python que utilizando uma lista [ ] resolva o problema para
manipulação de números.

    Uma administradora de condomínios está analisando o consumo de água de seus clientes.
Ajude a administradora desenvolvendo um algoritmo que receba a quantidade de moradores (N)
de um determinado condomínio, leia as N leituras de relógio de consumo de água,
e por fim, apesente a média de consumo e a quantidade de condôminos que ficaram acima ou igual a média.

exemplo de execução:

entrada	5
12000
15000
8000
10000
20000
-----------------------
saída	MEDIA = 13000
ACIMA = 2

"""

n = int(input("Informe a quantidade de moradores: "))

if n <= 0:
    print("Não existe nenhum Morador nesse condominio!")
    print("--" * 30)
else:
    print("Quantidade de moradores: ", n)
    print("--" * 30)
cont = 0
lst = []
maior = 0
media = 0
while cont != n:
    consumo = float((input("Informe o consumo de água do {}º morador: ".format(cont + 1))))

    lst.append(consumo)

    cont = cont + 1


print("--" * 30)
print(">>>>>>>>>>>> Consumo de Água de cada Morador! <<<<<<<<<<<<<<")
print("--" * 30)

cont1 = 0

for i in lst:
    print("{}° Morador: {}".format(cont1 + 1, i))

    media = sum(lst) / len(lst)
    cont1 = cont1 + 1

    if i >= media:
        maior += 1

print("\n-------------- Resultado! -----------------")
print("\nMédia = {:.1f}L".format(media))
print("Acima = {}".format(maior))
