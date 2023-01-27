import pandas as pd
import numpy as np
import math as m
#x = input('entrer file link : ')
data = pd.read_csv('c:/Users/BIGNETWORK/Desktop/python/Tiad/data.csv')

#mindist = input('entrer la distance minimum:')


def dif(x, y):  # la distance city Block
    if type(x) == str:
        if (x == y):
            return 0
        else:
            return 1
    else:
        return abs(x-y)

def Moyen(T):
    n=len(T)
    Moy=0
    for i in range(n):
            Moy=Moy+T[i]
    M=Moy/(len(T))
    return M

#def distance_list(groups, data,i, distance=[] ):
    


def clustering(groups, data, i, distance=[]):
    for g in range(len(groups)):
        somme = 0
        # jusqu'a la fin des nombre de colomne
        for j in range(len(list(data.iloc[i, :]))):
            # difference entre la 1er elt dans le cluster et les elt pas encore cluster
            diff = dif(groups[g][0][j], data.iloc[i, j])
            somme = somme+diff
        distance.append(somme)
    print (distance)
    distmoy=Moyen(distance)
    if min(distance) <=distmoy:
        groups[distance.index(distance)].append(list(data.iloc[i, :]))  # on ajoute just qui respect le criter
        #print(f'\n{list(data.iloc[i, :])}')
        
    else:
        group = []
        # else on le met dans un nouveau cluster
        group.append(list(data.iloc[i, :]))
        groups.append(group)

    return groups


def principal(data):
    groups = [[list(data.iloc[0, :])]]
    for line in range(1, len(data)):
        groups = clustering(groups, data, line, [])
    return groups


groups = principal(data)


p = 1
for g in groups:
    print(f'\n cluster  {p}')
    for i in g:
        print([''.join(str(i))])
    p = p+1
