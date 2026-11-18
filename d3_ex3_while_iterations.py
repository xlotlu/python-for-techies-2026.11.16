#while condition:
#    statements

# să numărăm de la 1 la 10

x = 1

from time import sleep

while x <= 10: # ne asigurăm că la un moment dat devine False
    print(x)
    x += 1
    sleep(.2)

# Exercițiu:
# Scrieți o funcție
def countdown(seconds):
    pass
# ce primind un număr de secunde, ține
# utilizatorul în așteptare acel număr de secunde
# în timp ce numără descrescător.

def countdown(seconds):
    i = 1

    while i < seconds:
        print(i)
        sleep(1)
        i += 1

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        sleep(1)
        seconds -= 1

# îmbunătățim funcția să facă countdown inline:


def countdown(seconds, inline=False):
    if inline:
        ending = "\r"
    else:
        ending = "\n"

    while seconds > 0:
        print(seconds, end=ending)
        sleep(1)
        seconds -= 1

# TODO:
# [temă pentru acasă, voluntară]
# codul de mai sus are un bug în mod inline:
# dacă începe countdown de la 100, rămâne ultimul 0
# la fel la tranziția sub 10.
#
# fix the bug.
# hint: ne trebuie întotdeauna la print
#       un string cu lungimea secundelor inițiale.
# l = len(str(seconds))


# două feluri de a lucra cu while:

# 1. while condition: ... și avem grijă să se schimbe condiția

# 2. while True: ... și avem grijă să facem break explicit

# exemplu:
from datetime import datetime
future_time = datetime(2026, 11, 18, 15, 57, 30)

while True:
    print("processing")
    sleep(3)
    if datetime.now() > future_time:
        break
