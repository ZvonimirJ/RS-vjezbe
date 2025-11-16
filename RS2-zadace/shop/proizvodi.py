class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Dostupna količina: {self.dostupna_kolicina}")


skladiste = [
    Proizvod("Stol", 250, 5),
    Proizvod("Stolica", 120, 10)
]


def dodaj_proizvod(p):
    if isinstance(p, Proizvod):
        skladiste.append(p)
        return
    if isinstance(p, dict):
        naziv = p.get('naziv')
        cijena = p.get('cijena')
        dostupna_kolicina = p.get('dostupna_kolicina')
        if naziv is None or cijena is None or dostupna_kolicina is None:
            raise ValueError('Rječnik mora sadržavati ključeve naziv, cijena i dostupna_kolicina')
        skladiste.append(Proizvod(naziv, cijena, dostupna_kolicina))
        return
    raise TypeError('dodaj_proizvod prihvaća dict ili Proizvod')
