import time
from colorama import Fore


def equal(x, y):
    if x == y:
        return print(Fore.GREEN + "Test passed")
    else:
        return print(Fore.RED + "Test failed")
        