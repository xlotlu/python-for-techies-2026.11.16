# 1. metoda .append(element)
#    adaugă la finalul listei.
lst = ['ala', 'bala', 'porto']
lst.append("cala")
print(lst)


# micro-exercițiu:
# creați o listă ce conține pătratul
# numerelor impare de la 1 la 11 inclusiv.

# Pattern de acumulare
# 1. ne definim obiectul în care acumulăm
lst = []
# 2. iterăm prin sursa de date
for elem in range(1, 11 + 1):
    # 3. filtrăm
    if elem % 2 == 1:
        # 4. acumulăm
        lst.append(elem ** 2)
# 5. suntem gata
print(lst)


# scrieți o funcție
def filter_by_first_letter(lst, letter):
    pass
# ce returnează o listă nouă ce conține
# doar elementele care încep cu litera `letter`

def filter_by_first_letter_v2(lst, letter):
    new_lst = []

    for elem in lst:
        if elem[0] == letter:
            new_lst.append(elem)

    return new_lst

# testați-o cu dataset-ul
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

print(
    filter_by_first_letter_v2(cities, "T")
)
print(
    filter_by_first_letter_v2(cities, "B")
)
print(
    filter_by_first_letter_v2(cities, "C")
)

# vorbeam despre .append():
lst = ["ala", "bala", "porto", "cala"]
lst.append("ceva") # adaugă elemntul "ceva"
                   # la sfârșitul listei.
# atenție: nu returnează nimic
#          (mutează lista in-place)

# 2. metoda .extend(iterable)
#    adaugă fiecare element din iterable
lst2 = ["un item", "doi item"]
lst.extend(lst2)
# note:
# 1) nu returnează nimic (operație in-place)
# 2) primește orice fel de iterabil
lst.extend(("ab", "bc", "cd"))
lst.extend("abcdefg")
lst.extend(range(5))

# echivalent cu:
for elem in range(5):
    lst.append(elem)

# 3. .pop()
# returnează ultimul element din listă
# în timp ce îl șterge din listă

# .pop(idx) -- cu argument face pop
# pe elementul de la acel index
lst = ["ala", "bala", "porto", "cala"]
lst.pop(1) # --> "bala"


# 4. .insert(index, object)
lst.insert(2, "ceva nou")
# nu returnează


# 5. .clear()
# golește lista
# nu returnează
lst.clear()

# 6. .remove(object)
# șterge prima apariție a lui object din listă
lst = ["ala", "bala", "ala", "porto", "cala", "ala", "bala"]
lst.remove("bala")
# nu returnează nimic


# 7. .count(obj)
lst.count("ala")  # --> 3

# 8. .index(obj)
lst.index("ala")  # --> 0

# Notă:
# .count() și .index()
# sunt suportate și de `tuple` și `str`

# 9. .sort()
# in-place sorting.
# nu returnează.
lst.sort()

# 10. .reverse()
# in-place reversal.
# nu returnează
lst.reverse()


###
# Excepțiile cu care avem de-a face
# când lucrăm cu lista (și de altfel
# și cu alte sequences).

lst = ['ala', 'bala', 'porto', 'cala']
try:
    lst[5]
    lst.pop(5)
except IndexError:
    print("a fost IndexError")

try:
    lst.index("calaxx")
    lst.remove("balaxx")
except ValueError:
    print("a fost ValueError")


# task:
# scriem o funcție
def remove_from_list(lst, value):
    pass
# ce șterge prima apariție a lui
# `value` din `lst`

def remove_from_list(lst, value):
    # 1. căutăm index-ul
    idx = 0
    for elem in lst:
        if elem == value:
            # 2. ștergem de la acel index
            del lst[idx]
            # suntem gata!
            return
        idx = idx + 1

# task:
# scriem o funcție
def remove_all_from_list(lst, value):
    idx = 0
    for elem in lst:
        if elem == value:
            del lst[idx]
        idx = idx + 1
# `value` din `lst`

#######
# lecția este:
# nu ștergem niciodată din listă
# în timp ce iterăm pe ea.
#######

# Exemplu ce se întâmplă dacă ștergem
# în timp ce iterăm pe indecși crescător:

lst = ["Aaa", "Bbb", "Ccc", "Ddd", "Eee", "Fff"]

for idx in range(0, len(lst)):
    print(idx, lst[idx])
    del lst[idx]

# .... decât dacă
# iterația se face de la coadă la cap

# 1. folosim range,
#    deci nu mai iterăm pe element,
#    ci iterăm pe indecși
# 2. facem range-ul descrescător

def remove_all_from_list(lst, value):
    for idx in range(len(lst) - 1, -1, -1):
        if lst[idx] == value:
            del lst[idx]



# Temă:
# Dată fiind structura de date
# care este o listă de liste
# de forma [name, distance]
cities = [
    ['Cluj-Napoca', 450],
    ['Timișoara', 550],
    ['Iași', 390],
    ['Constanța', 225],
    ['Brașov', 180],
    ['Craiova', 230],
    ['Galați', 250],
    ['Ploiești', 60],
    ['Oradea', 610],
    ['Sibiu', 275],
    ['Arad', 560],
    ['Bacău', 300],
    ['Brăila', 200],
    ['Buzău', 110],
    ['Suceava', 450],
    ['Pitești', 120],
    ['Târgu Mureș', 330],
    ['Baia Mare', 600],
]

# scrieți o funcție
def filter_by_distance(dataset, distance):
    pass
# ce returnează o listă nouă
# formată din perechile oraș-distanță
# cu distanța mai mică decât `distance`.
