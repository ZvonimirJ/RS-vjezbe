import aiohttp, asyncio

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    response_dict = await response.json()
    return response_dict["fact"]
    
async def filter_cat_facts(fact_list):
    return [fact for fact in fact_list if any(word in ["cat","cats"] for word in fact.lower().replace(",","").replace(".","").split(" "))]

async def main():
    async with aiohttp.ClientSession() as session:
        korutine = [get_cat_fact(session) for i in range (20)]
        rezultati = await asyncio.gather(*korutine)
        filtered = await filter_cat_facts(rezultati)
        print("Filtrirane činjenice o mačkama:\n")
        print(*filtered, sep="\n\n")

asyncio.run(main())
