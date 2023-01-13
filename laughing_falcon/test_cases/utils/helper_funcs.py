

from colorama import Fore


def equal(x, y):
    if x == y:
        return print(Fore.GREEN + "Test passed")
    else:
        return print(Fore.RED + "Test failed")
    
def above(x,y):
    if x > y:
        return print(Fore.GREEN + "Test passed")
    else:
        return print(Fore.RED + "Test failed")

def below(x,y):
    if x < y:
        return print(Fore.GREEN + "Test passed")
    else:
        return print(Fore.RED + "Test failed")

def close_to(x,y, units=50):
    if abs(x - y) <= units:
        return print(Fore.GREEN + "Test passed")
    else:
        return print(Fore.RED + "Test failed")