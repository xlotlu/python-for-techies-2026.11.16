d = {
    "k1": "valoare 1",
    "k2": "valoare 2",
}

# cheia este unică

# 1. acces după item (după cheie):
d["k1"]

# 2. assignment-ul se face exact la fel
d["k2"] = "valoare nouă"

# dacă cheia este existentă sau nu,
# comportamentul este același:
d["k3"] = "valoare și mai nouă"

# valorile pot să fie orice
import datetime
today = datetime.date.today()
d["ceva"] = today

# cheile pot să fie aproape orice:
k1 = datetime.date.today()
k2 = (1, 2, 3)
k3 = 55
k4 = 55.55

d[k1] = "something"
d[k2] = "something"
d[k3] = "something"
d[k4] = "something"

# cheile nu pot fi:
# - liste
# - dicționare

# există două modalități de a folosi dicționarele:
# 1. mapping cheie-valoare
#    ce emulează un tabel cu două coloane
#    id / valoare

d = {
    "București": 0,
    "Craiova": 200,
    "Pitești": 180,
}

# 2. liste de dicționare
#    când emulăm un tabel cu mai multe coloane
#
# exemplu: tabel de persoane,
# cu coloanele: 'name', 'age', 'city'

[
    {
        'name': 'Gigel',
        'age': 40,
        'city': 'Pitești',
    },
    {
        'name': 'John',
        'age': 20,
        'city': 'Arad',
    },
    # ....
]

# Exercițiu:
# dată fiind lista de tuple
# de forma (name, distance)
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 180),
    ('Craiova', 230),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 610),
    ('Sibiu', 275),
    ('Arad', 560),
    ('Bacău', 300),
    ('Brăila', 200),
    ('Buzău', 110),
    ('Suceava', 450),
    ('Pitești', 120),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600)
]

# creați un dicționar al cărui chei
# să fie numele orașului, respectiv
# valorile să fie distanța.

# Pattern de acumulare,
# doar că într-un dicționar...
#
# (pentru că pentru fiecare element din lista sursă
#  vom crea o cheie/valoare în dicționar)

# acumulare:
# 1. definesc obiect
d_cities = {}
# 2. iterez în sursă
for city in cities:
    # 3. acumulez
    d_cities[city[0]] = city[1]

# țineți minte iterable unpacking:
for city in cities:
    name, distance = city
    d_cities[name] = distance

# se poate face iterable unpacking inline în for:
for name, distance in cities:
    d_cities[name] = distance

# Exercițiu:
# dată fiind lista de tuple `cities`
# creați o listă de dicționare,
# în care fiecare element este de forma
# {'name': numele, 'distance': distanța}
[
    {
        'name': 'Cluj-Napoca',
        'distance': 450,
    },

    {
        'name': 'Timișoara',
        'distance': 550,
    },

    # ....
]

lst_of_dicts = []

for name, distance in cities:
    lst_of_dicts.append({
        'name': name,
        'distance': distance,
    })


# modalitățile de a instanția un dicționar:
# 1. explicit:
d = {'k1': 'v1', 'k2': 'v2'}

# 2. folosind clasa dict, cu keyword arguments
dict(k1="v1", k2="v2", k3="v3")
# deci suntem limitați la ce este identifier valid:
#dict(o cheie="ceva") # SyntaxError

# 3. dintr-un iterabil al cărui elemente
#    sunt la rândul său iterabile a câte 2 elemente

lst = [
    ('k1', 'v1'),
    ('k2', 'v2'),
    ('k3', 'v3'),
]
dict(lst)

# Exercițiu:
# dat fiind raportul primit ca string:
s = """-----------------------------------
|    Name    | Age |     City     |
-----------------------------------
| Gigel      |  20 | Copenhaga    |
| Andrei     |  42 | București    |
| Georgiana  |  20 | Timișoara    |
| Andreea    |  20 | Constanța    |
| Carmencita |  20 | Satu Mare    |
| George     |  20 | Sfântu Gheor |
-----------------------------------"""

# și dată fiind funcția
def parse_report(txt):
    my_lst = []

    # ne apucăm să acumulăm în my_lst
    for row in txt.splitlines()[3:-1]:
        cells = row.split('|')[1:-1]
        my_lst.append(list(
            map(str.strip, cells)
        ))

    return my_lst

# adaptați funcția `parse_report()`
# astfel încât să returneze o listă
# de dicționare.
# ideal, citind numele cheilor din header.

def parse_row(row):
    cells = row.split('|')[1:-1]

    return list(
        map(str.strip, cells)
    )

# strategie?

def parse_report(txt):
    my_lst = []

    rows = txt.splitlines()
    header = parse_row(rows[1])

    for row in rows[3:-1]:
        cells = parse_row(row)
        # avem de făcut aici un dicționar
        # în loc de lista cells:
        d = dict(zip(header, cells))
        my_lst.append(d)
    
    return my_lst

# f. important:
# cum iterăm în dicționare:
d = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}
# dicționarul este iterabil pe chei
for k in d:
    print(k)

# cele 3 metode ale dicționarului
# ce returnează un iterabil
# sunt .keys(), .values(), .items()

# după chei (rezultatul este același ca mai sus):
for k in d.keys():
    print(k)

# după valori:
for v in d.values():
    print(v)

# după "items" (adică perechea cheie-valoare):
for item in d.items():
    print(item)

for item in d.items():
    k, v = item
    print(k, v)

# de referință, cu unpacking de item inline în for:
for k, v in d.items():
    print(k, v)


# TEMĂ, opțional:
# care este cel mai succint și simplu și direct mod
# să obținem un dicționar nou dintr-unul existent
# sucind cheile <--> valorile?
