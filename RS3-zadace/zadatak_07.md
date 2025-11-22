# ZADATAK 7

### Program:
``` python
async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main())
```

### Izlaz:
```
Timer 1: 3 sekundi preostalo...
Timer 2: 5 sekundi preostalo...
Timer 3: 7 sekundi preostalo...
Timer 1: 2 sekundi preostalo...
Timer 2: 4 sekundi preostalo...
Timer 3: 6 sekundi preostalo...
Timer 1: 1 sekundi preostalo...
Timer 2: 3 sekundi preostalo...
Timer 3: 5 sekundi preostalo...
Timer 1: Vrijeme je isteklo!
Timer 2: 2 sekundi preostalo...
Timer 3: 4 sekundi preostalo...
Timer 2: 1 sekundi preostalo...
Timer 3: 3 sekundi preostalo...
Timer 2: Vrijeme je isteklo!
Timer 3: 2 sekundi preostalo...
Timer 3: 1 sekundi preostalo...
Timer 3: Vrijeme je isteklo!
```

### Objašnjenje

1. Prvo se izvršavanjem `asyncio.run(main())` pokreće `main()` korutina, koja samim time ulazi u event loop
    - u `main()` korutini definiraju se taskovi i pohranjuju se u listu `timers`, čime se tri `timer()` korutine s različitim ulaznim parametrima schedulaju, odnosno ulaze u pripravno stanje unutar event loopa.
    - pozivanjem `asyncio.gather(*timers)`, lista taskova se raspakira i redoslijedom se aktiviraju schedulane korutine
2. U event loopu aktivira se `timer()` korutina koja je prva definirana u listi `timers`, dakle ona s parametrima `name='Timer 1'` i `delay=3`
    - pokreće se prva iteracija for petlje unutar Timera 1 i dolazi do izvršavanja `asyncio.sleep(1)`. Taj task je pozadinska (background I/O) operacija zbog koje se prva korutina, ondnosno Timer 1, suspendira u event loopu
3. Unutar event loopa aktivira se sljedeća schedulana korutina, odnosno Timer 2.
    - unutar nje se isto pokreće prva iteracija njezine for petlje
    - sleep proces prelazi iz event loopa u background I/O, a Timer 2 se suspendira u korist iduće schedulane korutine - trećeg timera
4. Timer 3 se pokreće
    - prva iteracija njegove for petlje kreće
    - sleep task odlazi u background I/O, a Timer 3 se suspendira
    - event loop gleda ima li koja slobodna korutina za izvršavanje - trenutno je nema pa čeka da završi prvi background I/O proces, a to će biti sleep task prvog timera jer je prvi pokrenut (iako su praktički sva tri timera krenula istodobno, odnosno asinkrono)
5. Završava background I/O proces prvog Timera čime se pononvno vraćamo u Timer 1, koji je sada aktivan unutar event loopa
    - prelazimo u iduću iteraciju for petlje
    - opet ide `asyncio.sleep(1)` i prelazak u background I/O
    - prva korutina, odnosno Timer 1 se opet suspendira kako bi se mogla nastaviti iduća korutina, a to je drugi timer
6. Ovaj proces se ponavlja više puta do isteka for petlji svakog od timera
    - dakle, svaka `timer()` korutina će se suspendirati prilikom pozivanja `asyncio.sleep(1)`
    - taj proces će prijeći u background I/O, a event loop će preuzeti sljedeću schedulanu korutinu i tako u krug...
    - prvi će isteći Timer 1 pa će prvi i izaći iz event loopa
    - zatim će se isti proces izmjenjivati između Timera 2 i Timera 3 dok Timer 2 ne završi i izađe iz event loopa
    - na kraju će ostati samo Timer 3, a kada završi i Timer 3 u event loopu će ostati samo `main()` korutina koja također završava jer su se sve korutine gatherale čime cjelokupni program završava


