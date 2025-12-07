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
