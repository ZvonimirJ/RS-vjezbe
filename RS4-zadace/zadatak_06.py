import asyncio, random

async def fetch_weather_data():
    await asyncio.sleep(random.uniform(1, 5))
    return random.uniform(20, 25)

async def main():
    tasks = [asyncio.create_task(asyncio.wait_for(fetch_weather_data(), timeout=2)) for i in range(10)]
        
    results = []
    for i in range(len(tasks)):
        try:
            temp = await tasks[i]
            results.append(temp)
        except asyncio.TimeoutError:
            print(f"TimeoutError: Stanica {i+1} nije odgovorila na vrijeme.")
            results.append(None)

    valid_temps = [t for t in results if t is not None]
    if valid_temps:
        avg_temp = sum(valid_temps) / len(valid_temps)
        print(f"Prosječna temperatura (bez timeout stanica): {avg_temp:.1f}°C")
    else:
        print("Nema dostupnih podataka za izračun prosjeka.")


asyncio.run(main())
