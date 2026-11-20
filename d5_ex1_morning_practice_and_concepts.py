# scrieți o funcție
def grep(filename, match, insensitive=False):
    pass
# care printează fiecare linie din fișierul `filename`
# care conține substring-ul `match`

# folosiți `with` când deschideți fișiere.
# testați cu:
grep("notes.md", "python")
grep("notes.md", "python", True)


# de acum încolo, când deschideți un fișier
# (indiferent dacă pentru citire sau scriere)
# folosiți encoding="utf-8"
def grep(filename, match, insensitive=False):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()

        for line in lines:
            if match in line:
                print(line)

# Important: obiectul file pointer este iterabil!
# (și în mod text este iterabil linie cu linie)

def grep(filename, match, insensitive=False):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if match in line:
                print(line)

# diferența dintre
# file_pointer.read()       # <-- citește tot conținutul în memorie
# și
# for line in file_pointer  # <-- citește în memorie doar ce are nevoie

# Concluzie: cele 2 modalități de a lucra cu fișiere:
# 1) dacă use-case-ul este de citire line-by-line:
#      iterăm.
# 2) dacă use-case-ul este să obținem tot conținutul:
#      facem .read().

# spre exemplu: un fișier template pentru trimis pe e-mail
"""
Dragă {name},
Îți mulțumim că ne-ai contactat.
Ticket number-ul tău este {ticket_no}.

Cu drag,
Echipa {team}.
"""

# înapoi la problemă:
# să ținem cont și de `insensitive`

def grep(filename, match, insensitive=False):
    # if insensitive vrem să normalizăm și match și fiecare linie
    if insensitive:
        match = match.casefold()

    with open(filename, encoding="utf-8") as f:
        for line in f:          # line conține și "\n"
            if insensitive:
                if match in line.casefold():
                    print(line.removesuffix("\n"))
            else:
                if match in line:
                    print(line.removesuffix("\n"))

# "DRY" -- "don't repeat yourself"

def grep(filename, match, insensitive=False):
    # if insensitive vrem să normalizăm și match și fiecare linie
    if insensitive:
        match = match.casefold()

    with open(filename, encoding="utf-8") as f:
        for line in f:
            # normalizare
            if insensitive:
                mline = line.casefold()
            else:
                mline = line

            # același lucru cu blocul de mai sus:
            # ("ternary" statement)
            mline = line.casefold() if insensitive else line

            # matching
            if match in mline:
                print(line.removesuffix("\n"))

grep("notes.md", "Python")
grep("notes.md", "Python", True)


# Scrieți o funcție
def count_words(filename, insensitive=False):
    pass
# ce returnează numărul aparițiilor fiecărui cuvânt
# din fișierul `filename`

# strategie:
# - o listă cu cuvinte unice
# - apoi le luăm la rând pe fiecare și le numărăm
# - să apelăm count?

# - facem un dicționar în care cheia este cuvântul
#   și valoarea count-ul


def split_words(txt):
    "returns the words in `txt` as a list"

    for c in '!@#$%^&*()_+-=<>?:";/.`\\':
        txt = txt.replace(c, ' ')

    return txt.split()

import re # regular expressions

def split_words(txt):
    return re.findall(r'\w+', txt)


def count_words(filename, insensitive=False):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        all_words = set(split_words(content))

        out = []
        for word in all_words:
            out.append(
                (word, all_words.count(word))
            )
            # atenție, .count() face search în
            # tot all_words.
            # în mod repetat.
            # nu bun.

        return out

# re-implementare eficientă cu o singură iterație


def count_words(filename, insensitive=False):
    with open(filename, encoding="utf-8") as f:
        content = f.read()

        if insensitive:
            content = content.casefold()

        all_words = split_words(content)

        # facem un dicționar în care cheia este cuvântul
        # și valoarea count-ul
        out = {}

        for word in all_words:
            # dicționarul suportă lookup cu `in`
            if word not in out:
                # dacă nu există, inițializăm
                out[word] = 0

            out[word] += 1

        return out

count_words("notes.md")

# rescris folosind dict.get():
def count_words(filename, insensitive=False):
    with open(filename, encoding="utf-8") as f:
        content = f.read()

        if insensitive:
            content = content.casefold()

        all_words = split_words(content)

        out = {}
        for word in all_words:
            count = out.get(word, 0)
            out[word] = count + 1

        return out



# dar dacă îl vrem sortat?
def sort_dict(d, by_key=False, reverse=False):
    """
    returns a new dictionary sorted by its values by default.
    if `by_key` is True, sorts by key instead.
    """

    if by_key:
        def sorter(elem):
            return elem[0]
    else:
        def sorter(elem):
            return elem[1]

    elements = sorted(d.items(), key=sorter, reverse=reverse)

    return dict(elements)

sort_dict(count_words("notes.md"))

# rescris cu lambda functions

def sort_dict(d, by_key=False, reverse=False):
    """
    returns a new dictionary sorted by its values by default.
    if `by_key` is True, sorts by key instead.
    """

    sorter = (
        (lambda elem: elem[0]) if by_key is True
        else
        (lambda elem: elem[1])
    )

    elements = sorted(d.items(), key=sorter, reverse=reverse)

    return dict(elements)

sort_dict(count_words("notes.md"), by_key=True)
sort_dict(count_words("notes.md"), reverse=True)


# lambda statement este astfel:
# lambda argumente: return_value

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
cities.sort(key=lambda elem: elem[1])


# lucratul cu fișiere binare:

# scriem o funcție
def cp(source, target):
    pass
# ce copiază conținutul fișierului
# `source` în fișierul `target`

def cp(source, target):
    with open(source, 'rb') as fin:
        with open(target, 'wb') as fout:
            data = fin.read()
            fout.write(data)

# it works. problem: everything goes into memory.
# solution: chunked reading.

def cp(source, target, chunk_size=8192):
    with open(source, 'rb') as fin:
        with open(target, 'wb') as fout:
            while True:
                data = fin.read(chunk_size)
                # când ajungem la EOF?
                if not data:
                    break
                fout.write(data)

# modificări:
# 1) context managere simultane
def cp(source, target, chunk_size=8192):
    with (
        open(source, 'rb') as fin,
        open(target, 'wb') as fout
    ):
            while True:
                data = fin.read(chunk_size)
                # când ajungem la EOF?
                if not data:
                    break
                fout.write(data)

# 2) să facem funcția să nu facă overwrite tot timpul
def cp(source, target, overwrite=False, chunk_size=8192):
    mode = 'wb' if overwrite else 'xb'

    with (
        open(source, 'rb') as fin,
        open(target, mode) as fout
    ):
            while True:
                data = fin.read(chunk_size)
                # când ajungem la EOF?
                if not data:
                    break
                fout.write(data)

# divagare utilă:
# itertools.cycle() pentru a genera un "zebra table"

# dat fiind
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
# și
row_template = "<tr class={class_name}><td>{name}</td><td>{distance}</td></tr>\n"

from itertools import cycle
with open("out.html", 'w') as f:
    f.write("""
        <style>
            table 
            tr.even {background-color: yellow}
            tr.odd {background-color: green}

        </style>
        <table>
    """)

    for (name, distance), class_name in zip(cities, cycle(["even", "odd"])):
        f.write(
            row_template.format(class_name=class_name, name=name, distance=distance)
        )
    
    f.write('</table>')
