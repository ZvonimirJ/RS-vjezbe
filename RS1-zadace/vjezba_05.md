## Vježba 5 — Analiza for petlji 

### 1) Zašto petlja nema (previše) smisla
```python
for i in range(1, 2):
	print(i)
```

- `range(1, 2)` daje samo jedan broj: `1` (gornja granica `2` se ne uključuje).
- Petlja će se izvršiti točno jednom i ispisat će `1` tako da petlja u ovom slučaju praktički nema smisla.

Ispis:
```
1
```

---

### 2) Što će ispisati petlja:
```python
for i in range(10, 1, 2):
	print(i)
```

- Ovdje je `start=10`, `stop=1`, `step=2` (pozitivan).
- Ako je korak pozitivan, niz raste; ali početna vrijednost `10` je veća od `stop=1`, pa se od starta neće ići prema stopu.
- Zato je niz prazan i petlja se uopće neće izvršiti, tj. nema ispisa.

Ispis:
```
(nema ispisa)
```

---

### 3) Što će ispisati petlja:
```python
for i in range(10, 1, -1):
	print(i)
```

- Ovdje je `step=-1` (negativan), pa niz ide od 10 prema dolje.
- `stop=1` je ekskluzivan, znači zadnji ispisani broj će biti `2`.
- Ispisat će se brojevi od `10` do `2` u opadajućem redoslijedu.

Ispis:
```
10
9
8
7
6
5
4
3
2
```
