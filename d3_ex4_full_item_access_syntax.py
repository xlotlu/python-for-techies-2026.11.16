# dat fiind
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
    'Baia Mare'
]

cities[0]
cities[-1] # poziția de la sfârșit


# slicing:
cities[1:5]


#   sintaxa completă de slice:
# sequence[start:stop]
#   sau
# sequence[start:stop:step]
#
# cu nota importantă: oricare dintre ele poate să fie omis:
cities[:5]
cities[5:]

cities[:] # echivalent cu
cities.copy()

cities[::2]


# următoarea notă:
# în interiorul parantezelor drepte
# se cere un "item" din interiorul obiectului-colecție.
#
# ce înseamnă acest "item" decide obiectul.
#
# sequence-urile au "item"-uri numerice (după indecși).


# introducem dicționarul
# care este un mapping cheie - valoare:

d = {
    "cheie": "valoare",
    "altă cheie": "altă valoare",
}
# dicționarul suportă item access:
d["cheie"]

d = {
    15: "ceva",
    88: "altceva",
}
d[15]

d = {
    (1, 2): "pion alb",
    (1, 3): "pion negru",
    (2, 4): "turn alb",
    (3, 2): "damă neagră",
}

d[(2, 4)] # "turn alb"

1, 2 # aceasta este o tuplă. rezultă că:
d[1, 2] # "pion alb"
# este același lucru cu:
d[(1, 2)]

x = 3
y = 2
d[x, y] # 'damă neagră'


# aplicat la numpy:
import numpy

arr = numpy.array([
  [1, 2, 3],
  [22, 33, 44],
  [66, 77, 88],
])
arr[1, 1]
# echivalent cu
arr[(1, 1)] # returnează un element de la coordonatele
arr[1]  # returnează un row
# echivalent cu:
arr[1, :]

arr[:, 1] # coloana 1

arr[:2, :3]     # primele 2 rânduri, primele 3 coloane
arr[:2, -2:]    # primele 2 rânduri, ultimele 2 coloane
