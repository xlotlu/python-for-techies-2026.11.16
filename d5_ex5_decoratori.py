# definiție:
# un decorator este o funcție
# ce "decorează" o altă funcție.

from functools import cache # acesta este un decorator
import random
from time import sleep

@cache
def myfunc(a, b):
    sleep(3)
    # very cpu-intensive processing
    # or maybe network request that takes time...
    return random.randint(a, b)


# definiție:
# un decorator este o funcție
# ce primește ca argument o funcție
# și returnează o altă funcție.

@cache
def myfunc():
    pass
# face de fapt
# următorul lucru:

# dat fiind
def myfunc():
    pass
myfunc = cache(myfunc)