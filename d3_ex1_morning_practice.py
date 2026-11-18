# dată fiind lista

lst = [
    'Cluj-Napoca',
    'Arad',
    'Timișoara',
    'Iași',
    'Constanța',
    'Arad',
    'Brașov',
    'Arad',
    'Timișoara',
    'Constanța',
    'Arad',
]

# 1. printați elementul de la index-ul 2.
print(lst[2])

# 2. printați al 2lea element
print(lst[1])

# 3. adăugați la listă "Buzău"
lst.append("Buzău")

# 4. adăugați la listă, într-o singură operațiune:
["Pitești", "Ploiești", "Arad"]
lst.extend(["Pitești", "Ploiești", "Arad"]) # extend cu un obiect iterabil

# 5. ștergeți din listă, în timp ce setați într-o variabilă
# elementul de la index-ul 1
removed = lst.pop(1)
print(removed)

# 6. ștergeți din listă fără a seta în variabilă sau a returna
# ultimul element
del lst[len(lst) - 1]
# sau !! acces după index negativ:
del lst[-1]

# 7. printați index-ul primei apariții a lui "Arad"
print(lst.index("Arad"))

# 8. numărați de câte ori apare "Arad" în listă
print(lst.count("Arad"))

# 9. sortați lista
lst.sort()

# 10. reversați lista
lst.reverse()


# Notă:
# pentru a sorta lista în ordine inversă într-o singură operațiune:
lst.sort(reverse=True)


# 11. inserați pe prima poziție "Alba Iulia"
lst.insert(0, "Alba Iulia")


# 12. de-duplicați lista
dedup = []
for elem in lst:
    if elem not in dedup:
        dedup.append(elem)
print(dedup)

# in-place:
for idx in range(len(lst) -1, -1, -1):
    elem = lst[idx]
    if lst.count(elem) > 1:
        del lst[idx]

# Reminder:
# dacă vă găsiți într-o situație în care vreți
# să modificați lista în timp ce operați pe ea...
# ... challenge your assumptions. Sigur asta vreți?


# rezolvare rapidă, tot cu un obiect adițional:
dedup = set(lst)
# și dacă îl vrem neapărat listă:
dedup = list(dedup)


# Next level:
# Dată fiind lista de liste de forma
# [name, age, hobbies]
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# Scrieți o funcție
def get_friend_by_name(iterable, name):
    pass
# ce returnează elementul-persoană (lista)
# cu acel nume.

get_friend_by_name(friends, "Mike")
# --> ["Mike", 17, ["hiking", "fishing"]]

def get_friend_by_name(iterable, name):
    for friend in iterable:
        if friend[0] == name:
            return friend

print(
    get_friend_by_name(friends, "Mike")
)
print(
    get_friend_by_name(friends, "Anna")
)


# Folosind funcția de mai sus,
# accesați fiecare persoană în parte și faceți
# următoarele operațiuni:

# 1. Îmbătrâniți-o pe Jane cu un an
jane = get_friend_by_name(friends, "Jane")
jane[1] += 1
# echivalent cu
#jane[1] = jane[1] + 1

# 2. Adăugați hobby-urilor Annei "reading" și "cooking"
anna = get_friend_by_name(friends, "Anna")
anna[2].extend(["reading","cooking"])

# 3. Ștergeți-i lui Mike hobby-ul de la indexul 1
mike = get_friend_by_name(friends, "Mike")
del mike[2][1]

# Apoi inspectați lista inițială.

# Scrieți două funcții
def find_friends_by_hobby(friends, hobby):
    pass
# ce returnează o listă de prieteni
# cu aceeași structură ca lista `friends`,
# filtrând astfel încât să conțină doar prietenii
# cu acel hobby.

def find_friends_by_hobby(friends, hobby):
    out = []
    for person in friends:
        if hobby in person[2]:
            out.append(person)
    return out


def find_friends_by_age(friends, min_age=None, max_age=None):
    pass
# ce returnează o listă de prieteni
# cu aceeași structură ca lista `friends`,
# filtrând astfel încât prietenii să aibă
# vârstă cuprinsă între `min_age` și `max_age` inclusiv.
# dacă `min_age` sau `max_age` sunt None,
# nu mai filtrăm respectiv după min sau max.

# dacă min_age și max_age nu ar fi fost opționale:
def find_friends_by_age(friends, min_age, max_age):
    out = []
    for person in friends:
        age = person[1]
        if min_age <= age and age <= max_age:
            out.append(person)
    return out


def find_friends_by_age(friends, min_age=None, max_age=None):
    out = []
    for person in friends:
        age = person[1]
        if (
            min_age is not None
            and min_age <= age
        ) and (
            max_age is not None
            and age <= max_age
        ):
            out.append(person)
    return out



# v.2.: rescris pentru readability,
# condiția este spartă în două expresii

def find_friends_by_age(friends, min_age=None, max_age=None):
    out = []
    for person in friends:
        age = person[1]

        min_age_check = min_age is None or min_age <= age
        max_age_check = max_age is None or age <= max_age

        if min_age_check and max_age_check:
            out.append(person)
    return out

# v.3.: rescrie pentru excluziune
# (las deoparte ce nu mă interesează)

def find_friends_by_age(friends, min_age=None, max_age=None):
    out = []

    for person in friends:
        age = person[1]

        # condițional, dacă acesta nu se potrivește, fac
        if min_age is not None and age < min_age:
            continue # nu mai rulează restul codului din iterația curentă
                    # (trece la începutul iterației pt. elementul următor)
        if max_age is not None and age > max_age:
            continue

        # aici ajungem doar dacă nu a fost exclus
        # de nici-una din cele 2 condiții de mai sus.
        out.append(person)

    return out

# există două statement-uri pentru controlul iterațiilor:
# - break      --- iese complet din iterație ("sparge loop-ul")
# - continue   --- iese din iterația curentă ("trece la loop-ul următor")
