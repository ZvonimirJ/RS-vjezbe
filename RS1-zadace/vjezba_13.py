def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

def maks_i_min(lista):
    maxv = lista[0]
    minv = lista[0]
    for x in lista:
        if x > maxv:
            maxv = x
        if x < minv:
            minv = x
    return (maxv, minv)

def presjek(s1, s2):
    return {x for x in s1 if x in s2}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))

lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista2))

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))
