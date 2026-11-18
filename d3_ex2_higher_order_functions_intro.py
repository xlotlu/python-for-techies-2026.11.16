"funcții de ordin superior"

# primesc ca argument o altă funcție
# "folosesc alte funcții drept sursă de date"

# Dată fiind structura de date
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
# sortați-o, crescător, după distanță.


# 1. în Python totul este obiect
# 2. deci funcția este obiect
# 3. rezultă: putem pasa o funcție
#    drept argument obișnuit

def my_executor(func, arg):
    print("voi executa", func, "cu", arg)
    func(arg)

# metoda .sort() a listei
# primește argument keyword opțional
# key=func -- care va rula func(elem) pt. fiecare element

def sorter(elem):
    return elem[1]

cities.sort(key=sorter)


# alte funcții de rang superior:

# sorted(iterable, key=None, reverse=False)
# ^^ face același lucru ca .sort() al listei
#    doar că merge pe orice iterabil
tup = ("Jkl", "Abc", "Mno", "Def", "Pqr", "Ghi")
sorted(tup) # --> returns a list


# filter(function, iterable)
def fn_dist_higher(el):
    print("   »»", el)
    return el[1] >= 400

for item in filter(fn_dist_higher, cities):
    print(item)
