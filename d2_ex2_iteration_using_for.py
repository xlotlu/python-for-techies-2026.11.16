# for element in iterable:
#     do_something_with(element)
#     do_something_else()
#     # etc.

s = "Ce zi însorită"
for elem in s: # în Python se iterează direct pe elementele colecției
    print("»", elem) # pt. str-uri, elementele sunt fiecare caracter în parte

tup = ("lala", 15, "etc.")
# tupla este o colecție ordonată de alte obiecte.
# tupla este immutable
for elem in tup:
    print("»", elem)

lst = ["tot o colecție", "ordonată", "de orice", 22]
# lista este mutable
for elem in lst:
    print("»", elem)

# str, tuple și list se numesc "sequences".
# ele au multe lucruri în comun.
# unul dintre ele este item access după index

# "item access"
lst[1]
lst[0]

# assignment folosind item access:
lst[1] = "O valoare!"
# ^^ demonstrează că lista este mutable.


# Exercițiu: dată fiind lista de numere
lst = [1, 15, 22, 4, 7]
# printați pătratul fiecăruia
for elem in lst:
    print("»", elem ** 2)

# Notă laterală:
# listele (și tuplele) pot fi adunate:
l1 = ["bla", "bli", "blu"]
l2 = ["tra", "lala"]
l1 + l2

# Exercițiu:
# printați pătratele numerelor impare
# de la 0 la 21, inclusiv.

for num in range(22):
    if num % 2 == 1:
        print(num ** 2)
# sau așa, pentru că
# orice obiect este evaluabil în context boolean:
for num in range(22):
    if num % 2:
        print(num ** 2)

# sau, sărim if-ul, și folosim
# argumentul opțional `step` al range-ului
for num in range(1, 22, 2):
    print(num ** 2)


# range() nu este memory-backed
# concluzie: în Python, iterabilele nu au nevoie
# să fie concrete în memorie.



# Exercițiu:
# Dat fiind setul de date
cities = [
    'Cluj-Napoca',
    'Timișoara',
    'Iași',
    'Constanța',
    'Brașov',
    'Craiova',
    'Galați',
    'Ploiești',
    'Oradea',
    'Sibiu',
    'Arad',
    'Bacău',
    'Brăila',
    'Buzău',
    'Suceava',
    'Pitești',
    'Târgu Mureș',
    'Baia Mare',
]
# printați orașele care încep cu litera "B"
# strategie:
# 1. iterăm în dataset,
# 2. pentru elementul curent aflăm prima literă
#    (țineți minte că str-ul suportă item access după index),
# 3. faceți if, dacă da, printați.

# 1. iterăm
for city in cities:
    # 2. filtrăm
    if city[0] == 'B':
        # 3. acțiune
        print(city)


# Exercițiu 1: scrieți o funcție
def filter_by_first_letter(lst, letter):
    pass
# ce printează elementele care încep cu litera respectivă.

def filter_by_first_letter(lst, letter):
    for elem in lst:
        if elem[0] == letter:
            print(elem)


# Exercițiu 2: modificați funcția de mai sus
# pentru a returna o listă nouă, conținând elementele
# respective.
#
# considerați că lista are metoda `.append()`

# TODO, în capitolul următor