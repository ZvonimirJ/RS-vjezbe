import asyncio

data = [{"prezime":"Žutić", "broj_kartice":"2345613812", "CVV":"254"},
        {"prezime":"Crnjak", "broj_kartice":"39458485857", "CVV":"911"},
        {"prezime":"Bjelica", "broj_kartice":"23579473848", "CVV":"443"}]

async def secure_data(sensitive_data):
    await asyncio.sleep(3)
    return {"prezime":sensitive_data["prezime"],
            "broj_kartice":hash(sensitive_data["broj_kartice"]),
            "CVV":hash(sensitive_data["CVV"])}

async def main():
    zadatci=[asyncio.create_task(secure_data(d)) for d in data]
    rezultati= await asyncio.gather(*zadatci)
    print(*rezultati, sep="\n")

asyncio.run(main())




