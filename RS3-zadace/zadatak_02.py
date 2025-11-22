import asyncio

async def dohvati_korisnike():
    korisnici=[{"ime":"Ivan", "prezime":"Ivić", "godina_rodenja":"2000"},
               {"ime":"Ana", "prezime":"Anić", "godina_rodenja":"2003"},
               {"ime":"Borna", "prezime":"Borić", "godina_rodenja":"1995"}]
    await asyncio.sleep(3)
    print("Korisnici dohvaćeni!")
    return korisnici

async def dohvati_proizvode():
    proizvodi=[{"naziv":"tjestenina", "cijena":"1.90"},
               {"naziv":"mandarina", "cijena":"1.09"},
               {"naziv":"kefir", "cijena":"1.29"}]
    await asyncio.sleep(5)
    print("Proizvodi dohvaćeni!")
    return proizvodi

async def main():
    rezultat1, rezultat2 = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print(*rezultat1, sep="\n")
    print(*rezultat2, sep="\n")

asyncio.run(main())