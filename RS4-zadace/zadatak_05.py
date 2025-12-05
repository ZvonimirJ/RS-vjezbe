import asyncio, aiohttp

async def fetch_url(session, url):
    response = await session.get(url, timeout=5)
    return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for url, content in zip(urls, results):
            print(f"Fetched {len(content)} characters from {url}")

asyncio.run(main())
