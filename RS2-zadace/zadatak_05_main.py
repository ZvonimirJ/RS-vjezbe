from shop import proizvodi, narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p)

print('Broj proizvoda na skladistu:', len(proizvodi.skladiste))

for proizvod in proizvodi.skladiste:
    proizvod.ispis()

naruceni = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

nar = narudzbe.napravi_narudzbu(naruceni)
if nar:
    nar.ispis_narudzbe()
