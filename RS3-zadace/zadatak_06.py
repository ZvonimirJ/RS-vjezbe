import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    await asyncio.sleep(2) # ovdje sam dodao dodatan sleep -> ide u backgorund I/O -> prva korutina se suspendira kako bi se druga korutina mogla nastaviti i obaviti svoj print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    # mogao sam sleep dodati i ovdje, onda bi se suspendirala main korutina, kako bi se dovršila druga korutina
    print("Fetch 1 uspješno završen.")
    return [result1]


t1 = time.perf_counter()
results = asyncio.run(main())
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")