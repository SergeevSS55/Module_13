import asyncio


async def start_strongman(name: str, power: int):
    if power <= 0:
        raise Exception("Сила не может быть меньше 0")
    print(f'Силач {name} начал(-а) соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял(-а) {i} шар')
    print(f'Силач {name} закончил(-а) соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    task4 = asyncio.create_task(start_strongman('Grandmother', 10))
    task5 = asyncio.create_task(start_strongman('Iron man', -1))
    await task1
    await task2
    await task3
    await task4
    await task5

asyncio.run(start_tournament())
