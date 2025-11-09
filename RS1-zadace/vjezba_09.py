def ukloni_duplikate(lista):
    videno = set()
    rezultat = []
    for x in lista:
        if x not in videno:
            rezultat.append(x)
            videno.add(x)
    return rezultat

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))
