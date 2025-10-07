#Author: David Engen
#Date: 2025-10-07

print('Ei24 - genrep praktiskt prov ht25')
r = input('Ange resistorer:')
if r == (""):
    print('Serieresistans:0')
    print('Parallellresistans:0')
else:
    r = r.split(' ')
    for i in range(len(r)):
        r[i] = int(r[i])
    serie = 0
    for x in range(len(r)):
        serie = serie + r[x]
    parallell = 0
    for y in range(len(r)):
        parallell = parallell + (1/r[y])
    parallell = (1/parallell)
    print(f'Serieresistans: {serie}')
    print(f'Parallellresistans: {parallell}')
