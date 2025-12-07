import asyncio
import random
from graphlib import CycleError

from colorama import Fore, Style, init

init(autoreset=True)

c = (
    Style.RESET_ALL,
    Fore.CYAN,
    Fore.RED,
    Fore.MAGENTA,
    Fore.YELLOW,
    Fore.GREEN,
)


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"{c[idx + 1]} inicjalizacja makerandom({idx})")

    i = random.randint(0, 10)  # od 0 do 10
    while i <= threshold:
        print(f"{c[idx + 1]} makerandom({idx}) <= {i} - zbyt niska wartośc. Powtórzenie")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)

    print(f"{c[idx + 1]} zakończenie makerandom({idx}) == {i} -> {c[0]}.")

    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 9 - i) for i in range(5)))
    return res


if __name__ == '__main__':
    random.seed(444)  # ustawienie ziarna w generatorze
    r1, r2, r3, r4, r5 = asyncio.run(main())
    print(f"Wyniki: {r1=}, {r2=}, {r3=}, {r4=},{r5=}")
