import asyncio, random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj%2==0:
        return f"Broj {broj} je paran"
    else:
        return f"Broj {broj} je neparan"

async def main():
    brojevi=[random.randint(1,100) for i in range(10)]
    print(brojevi)
    zadaci=[asyncio.create_task(provjeri_parnost(i)) for i in brojevi]
    rezultati = await asyncio.gather(*zadaci)
    print(*rezultati, sep="\n")

asyncio.run(main())
