# https://docs.python.org/3/tutorial/modules.html

# python modules
import datetime

print(datetime.datetime.now())

# own modules
import sum_module

print(sum_module.sum([1, 2, 3, 4, 5]))

# third party modules
from colorama import Fore, Back, Style

print(Fore.RED + "Hello World!" + Style.RESET_ALL)
print(Back.GREEN + "Hello World!" + Style.RESET_ALL)
