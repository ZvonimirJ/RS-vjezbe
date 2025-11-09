def validiraj_broj_telefona(broj: str):
    mapa = {
        '01': ('fiksna mreža', 'Grad Zagreb i Zagrebačka županija', None),
        '020': ('fiksna mreža', 'Dubrovačko-neretvanska županija', None),
        '021': ('fiksna mreža', 'Splitsko-dalmatinska županija', None),
        '022': ('fiksna mreža', 'Šibensko-kninska županija', None),
        '023': ('fiksna mreža', 'Zadarska županija', None),
        '031': ('fiksna mreža', 'Osječko-baranjska županija', None),
        '032': ('fiksna mreža', 'Vukovarsko-srijemska županija', None),
        '033': ('fiksna mreža', 'Virovitičko-podravska županija', None),
        '034': ('fiksna mređa', 'Požeško-slavonska županija', None),
        '035': ('fiksna mreža', 'Brodsko-posavska županija', None),
        '040': ('fiksna mređa', 'Međimurska županija', None),
        '042': ('fiksna mreža', 'Varaždinska županija', None),
        '043': ('fiksna mreža', 'Bjelovarsko-bilogorska županija', None),
        '044': ('fiksna mreža', 'Sisačko-moslavačka županija', None),
        '047': ('fiksna mređa', 'Karlovačka županija', None),
        '048': ('fiksna mreža', 'Koprivničko-križevačka županija', None),
        '049': ('fiksna mreža', 'Krapinsko-zagorska županija', None),
        '051': ('fiksna mreža', 'Primorsko-goranska županija', None),
        '052': ('fiksna mreža', 'Istarska županija', None),
        '053': ('fiksna mređa', 'Ličko-senjska županija', None),
        '091': ('mobilna mreža', None, 'A1 Hrvatska'),
        '092': ('mobilna mreža', None, 'Tomato'),
        '095': ('mobilna mreža', None, 'Telemach'),
        '097': ('mobilna mreža', None, 'bonbon'),
        '098': ('mobilna mreža', None, 'Hrvatski Telekom'),
        '099': ('mobilna mreža', None, 'Hrvatski Telekom'),
        '0800': ('posebne usluge', None, None),
        '060': ('posebne usluge', None, None),
        '061': ('posebne usluge', None, None),
        '064': ('posebne usluge', None, None),
        '065': ('posebne usluge', None, None),
        '069': ('posebne usluge', None, None),
        '072': ('posebne usluge', None, None)
    }
    digits = ''.join(ch for ch in broj if ch.isdigit())
    national = digits
    if digits.startswith('00385'):
        national = '0' + digits[5:]
    elif digits.startswith('385'):
        national = '0' + digits[3:]
    elif digits.startswith('0'):
        national = digits
    else:
        national = digits
    prefixes = sorted(mapa.keys(), key=lambda x: -len(x))
    match = None
    for p in prefixes:
        if national.startswith(p):
            match = p
            break
    if not match:
        return {'validan': False, 'pozivni_broj': None, 'broj_ostatak': national}
    ostatak = national[len(match):]
    vrsta, mjesto, operater = mapa[match]
    if vrsta == 'posebne usluge':
        if len(ostatak) == 6:
            return {'pozivni_broj': match, 'broj_ostatak': ostatak, 'vrsta': vrsta, 'mjesto': None, 'operater': None, 'validan': True}
        else:
            return {'validan': False, 'pozivni_broj': match, 'broj_ostatak': ostatak}
    if vrsta == 'mobilna mreža':
        if len(ostatak) in (6, 7):
            return {'pozivni_broj': match, 'broj_ostatak': ostatak, 'vrsta': vrsta, 'mjesto': None, 'operater': operater, 'validan': True}
        else:
            return {'validan': False, 'pozivni_broj': match, 'broj_ostatak': ostatak}
    if vrsta == 'fiksna mreža':
        if len(ostatak) in (6, 7):
            return {'pozivni_broj': match, 'broj_ostatak': ostatak, 'vrsta': vrsta, 'mjesto': mjesto, 'operater': None, 'validan': True}
        else:
            return {'validan': False, 'pozivni_broj': match, 'broj_ostatak': ostatak}

print(validiraj_broj_telefona('+385917217633'))
print(validiraj_broj_telefona('0917217633'))
print(validiraj_broj_telefona('0800123456'))
