from . import proizvodi

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        stavke = ', '.join(f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi)
        print(f"Naručeni proizvodi: {stavke}, Ukupna cijena: {self.ukupna_cijena} eur")


narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print('Argument naruceni_proizvodi mora biti lista')
        return None
    if len(naruceni_proizvodi) == 0:
        print('Lista ne smije biti prazna')
        return None
    for el in naruceni_proizvodi:
        if not isinstance(el, dict):
            print('Svi elementi moraju biti rjecnici')
            return None
        if not all(k in el for k in ('naziv', 'cijena', 'narucena_kolicina')):
            print('Rjecnik mora sadrzavati kljuceve naziv, cijena i narucena_kolicina')
            return None

    for p in naruceni_proizvodi:
        naziv = p['naziv']
        trazena = p['narucena_kolicina']
        pronadeno = None
        for sklad_item in proizvodi.skladiste:
            if sklad_item.naziv == naziv:
                pronadeno = sklad_item
                break
        if pronadeno is None:
            print(f"Proizvod {naziv} nije dostupan!")
            return None
        if pronadeno.dostupna_kolicina < trazena:
            print(f"Proizvod {naziv} nije dostupan u trazenoj kolicini!")
            return None

    ukupna_cijena = sum(item['cijena'] * item['narucena_kolicina'] for item in naruceni_proizvodi)

    nar = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(nar)

    for p in naruceni_proizvodi:
        for sklad_item in proizvodi.skladiste:
            if sklad_item.naziv == p['naziv']:
                sklad_item.dostupna_kolicina -= p['narucena_kolicina']
                break

    return nar
