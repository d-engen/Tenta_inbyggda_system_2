#Author: David Engen
#Date: 2025-10-10

termer = input('Vilka tabeller vill du beräkna? ')
tal_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
produkt = 0
if termer == (""):
    print('Avslutar')
else:
    termer = termer.split()
    for i in range(len(termer)):
        termer[i] = int(termer[i])

    for j in range(len(termer)):
        for x in range(len(tal_lista)):
            produkt = termer[j] * tal_lista[x]
            print(f'{termer[j]} * {tal_lista[x]} = {produkt}')
        print('\n')
