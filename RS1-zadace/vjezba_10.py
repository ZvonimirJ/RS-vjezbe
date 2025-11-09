def brojanje_riječi(tekst):
    r = {}
    for w in tekst.split():
        r[w] = r.get(w, 0) + 1
    return r

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))
