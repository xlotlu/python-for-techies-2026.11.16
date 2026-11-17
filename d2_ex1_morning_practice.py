# 1. partea întreagă a împărțirii lui 17 la 4?
17 // 4

# 2. restul împărțirii lui 17 la 4?
17 % 4

# 3. repetați string-ul "tra la la" de 7 ori
# (concatenați-l cu sine).
"tra la la" * 7

# 4. scrieți o funcție `cube(x)` ce returnează
# cubul numărului `x`.
def cube(x):
    return x ** 3

# 5. cereți un număr întreg de la utilizator și,
# folosind funcția cube de mai sus, faceți output string-ului
# "Cubul numărului <număr> este <cub>."
# Folosiți una din formele de string interpolation.
number = input("Spune-mi un număr întreg: ")
number = int(number)
print(
    "Cubul numărului %s este %s." % (number, cube(number))
)
print(
    f"Cubul numărului {number} este {cube(number)}."
)

# 6. scrieți un condițional ce să rezulte în output-ul (print)
"<name> is a student."
# sau
"<name> is not a student."
# conform seturilor de variable
name = "Jane"
is_student = False
# și apoi
name = "Andrew"
is_student = True

name = "Jane"
is_student = False

if is_student is True:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

name = "Andrew"
is_student = True

if is_student:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

# 7. scrieți o funcție
def format_minutes(total_minutes):
    pass
# ce primind un număr întreg returnează un string
# de forma H:MM sau HH:MM după caz.
# adică:
# format_minutes(58)  -->  0:58
# format_minutes(62)  -->  1:02
# format_minutes(602) --> 10:02


def format_minutes(total_minutes):
    hours = int(total_minutes / 60)
    # perfect echivalent cu:
    hours = total_minutes // 60

    minutes = total_minutes - hours * 60
    # perfect echivalent cu:
    minutes = total_minutes % 60

    if minutes < 10:
        return f"{hours}:0{minutes}"
    else:
        return f"{hours}:{minutes}"

# scurtăm la versiunea 1:
def format_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60

    if minutes < 10:
        return f"{hours}:0{minutes}"
    else:
        return f"{hours}:{minutes}"

# v.2: cu opțiuni de formatare a str-ului
# introducing string formatting:
height = 1.82
distance = 5
location = "Arad"
print(
    f"ești la {location:_>12} la distanța {distance:04d} cu înălțime {height:.4f}"
)

def format_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60

    return f"{hours}:{minutes:02d}"

# v.3: cu iterable unpacking

# introducem iterabile:
tup = (1, 2, 3)
lst = ["ala", "bala", "porto"]
rng = range(5, 8)
s = "xyz"

# dovadă că sunt iterababile:
for elem in tup:
    print("»", elem)
for elem in lst:
    print("»", elem)
for elem in rng:
    print("»", elem)
for elem in s:
    print("»", elem)

# fiecăruia i se poate face "unpacking",
# adică se pot asigna deodată la mai multe variabile:
a, b, c = tup
print(a, b, c)

a, b, c = lst
print(a, b, c)

a, b, c = rng
print(a, b, c)

a, b, c = s
print(a, b, c)

# și atunci, rezolvare simplificată folosind `divmod()`
def format_minutes(total_minutes):
    hours, minutes = divmod(total_minutes, 60)
    return f"{hours}:{minutes:02d}"

# 8. [opțional] [pentru cine a terminat]

# folosind funcția de ieri
def get_greeting_for_hour(hour):
    # early exit în caz de valoare nepotrivită:
    if hour < 0 or hour > 23:
        raise ValueError("Invalid hour")

    if 5 <= hour < 10:
        return 'Buna dimineata'
    elif 10 <= hour < 18:
        return 'Buna ziua'
    elif 18 <= hour < 22:
        return 'Buna seara'
    else:
        return 'Noapte buna'

# scrieți o funcție
def get_current_greeting():
    pass
# ce returnează salutul potrivit orei curente.
# pentru a obține ora curentă, țineți cont că:
# a) există modulul datetime
import datetime
# b) acesta conține o clasă datetime, ce are
# o metodă numită `now()`
datetime.datetime.now()
# c) aceasta returnează un obiect care are
# atributul `hour`.

from datetime import datetime
def get_current_greeting():
    now = datetime.now()
    hour = now.hour
    greeting = get_greeting_for_hour(hour)
    return greeting

# sau one-liner:
def get_current_greeting():
    return get_greeting_for_hour(datetime.now().hour)


# după ce ați scris și testat funcția `get_current_greeting()`
# cereți input utilizatorului numele său și salutați-l
# cu un string de forma "<greeting>, <nume>!"

def greet_user():
    # este o idee bună ca funcțiile să fie cât mai concise,
    # cât mai simple, cât mai punctuale.
    name = input("Spune-mi numele tău: ")
    greeting = get_current_greeting()
    print(f"{greeting}, {name}!")
