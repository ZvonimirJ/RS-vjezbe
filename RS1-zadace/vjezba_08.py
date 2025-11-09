def filtriraj_parne(lista):
    return [x for x in lista if x % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista))
