import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def autentifikacija(username, password):
    #await asyncio.sleep(2)
    await asyncio.sleep(3)
    if korisnici[username] == password:
        return True
    else:
        raise ValueError(f"Neispravna lozinka za {username}!")

async def main():
    zadaci = [
        autentifikacija("korisnik1", "lozinka1"),
        autentifikacija("korisnik2", "lozinka2"),
        #autentifikacija("korisnik3", "aaaaaaaa"), #asyncio.gather() ovdje staje s ValueErrorom i ne obrađuje daljnje taskove
        asyncio.wait_for(autentifikacija("korisnik3", "lozinka3"), timeout=3),
        autentifikacija("korisnik4", "lozinka4")
    ]

    try:
        rezultati = await asyncio.gather(*zadaci)
    except ValueError as e:
        print("ValueError:", e)
    except asyncio.TimeoutError:
        print("TimeoutError: Autentifikacija je istekla zbog predugog trajanja.")
asyncio.run(main())
