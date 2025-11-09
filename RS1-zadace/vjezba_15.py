def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    v = 0
    c = 0
    for ch in tekst:
        if ch in vowels:
            v += 1
        elif ch in consonants:
            c += 1
    return {"vowels": v, "consonants": c}

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))
