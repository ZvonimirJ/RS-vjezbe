import asyncio
import aiohttp
import time

async def fetch_users(session):
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    return await response.json()

async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        korutine = [fetch_users(session) for i in range(5)]
        responses = await asyncio.gather(*korutine)
    
    imena=[user["name"] for user in responses[0]]
    emails=[user["email"] for user in responses[0]]
    usernames=[user["username"] for user in responses[0]]
    end_time = time.time()
    
    
    print(f"\nImena: {', '.join(imena)}")
    print(f"\nEmailovi: {', '.join(emails)}")
    print(f"\nKorisnička imena: {', '.join(usernames)}")
    print(f"\nUkupno vrijeme: {end_time-start_time:.2f} sec")

asyncio.run(main())
