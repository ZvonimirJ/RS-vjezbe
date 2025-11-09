def grupiraj_po_paritetu(lista):
    parni = []
    neparni = []
    for x in lista:
        if x % 2 == 0:
            parni.append(x)
        else:
            neparni.append(x)
    return {"parni": parni, "neparni": neparni}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))
