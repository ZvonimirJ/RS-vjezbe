import asyncio

async def dohvati_s_weba():
    podatci_s_weba=[x for x in range(1,11)]
    await asyncio.sleep(3)
    print("Podatci dohvaćeni")
    return podatci_s_weba

asyncio.run(dohvati_s_weba())