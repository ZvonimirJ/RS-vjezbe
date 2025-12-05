import aiohttp, asyncio

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    response_dict = await response.json()
    return response_dict["data"][0]["attributes"]["body"]

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    response_dict = await response.json()
    return response_dict["fact"]

async def mix_facts(dog_facts, cat_facts):
    return [dog_fact if len(dog_fact)>len(cat_fact) else cat_fact for dog_fact, cat_fact in zip(dog_facts, cat_facts)]

async def main():
    async with aiohttp.ClientSession() as session:
        dog_korutine = [get_dog_fact(session) for i in range(5)]
        cat_korutine = [get_cat_fact(session) for i in range(5)]
        
        facts = await asyncio.gather(*dog_korutine, *cat_korutine)
        dog_facts = facts[:5]
        cat_facts = facts[5:]
        mix = await mix_facts(dog_facts, cat_facts)
        print(*mix, sep="\n")

asyncio.run(main())
