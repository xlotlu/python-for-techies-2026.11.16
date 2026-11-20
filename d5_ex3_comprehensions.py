# list comprehension:

# dat fiind
iterable = range(10)

# creați o listă cu pătratele lor:
lst = []
for elem in iterable:
    lst.append(elem ** 2)

# echivalentul one-liner:
[elem ** 2 for elem in iterable]


# dar dacă vrem doar nr.-ele impare?

lst = []
for elem in iterable:
    if elem % 2:
        lst.append(elem ** 2)

[elem ** 2 for elem in iterable if elem % 2]

[
    elem ** 2
    for elem in iterable
    if elem % 2
]

# dictionary comprehension
lst = [
    ['Cluj-Napoca', 450],
    ['Timișoara', 550],
    ['Iași', 390],
    ['Constanța', 225],
    ['Brașov', 180]
]

d = {}
for name, dist in lst:
    d[name] = dist

# echivalent cu:
{
    name: dist
    for name, dist in lst
}

# dat fiind
lst = [
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
    ['Baia Mare', 600]
]
# creați un dicționar cu orașele
# cu distanță mai mică decât 200
d = {}
for name, dist in lst:
    if dist < 200:
        d[name] = dist

# cu comprehension:
{
    name: dist
    for name, dist in lst
    if dist < 200
}


# la final:
# nu există tuple comprehension
gen_obj = ( elem[0] for elem in lst if elem[1] < 200 )

# generatorul este un obiect iterabil
# care nu concretizează în memorie
# obiectele pe care le "returnează".
#
# mai precis, generează, la runtime, fiecare element în parte.
#
# ("la runtime" = când este iterat)