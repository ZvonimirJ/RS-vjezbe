zbroj = 0
broj = int(input("Unesite cijeli broj (0 za kraj): "))

while broj != 0:
    zbroj += broj
    broj = int(input("Unesite cijeli broj (0 za kraj): "))

print(f"Zbroj unesenih brojeva je {zbroj}")
