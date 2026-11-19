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
# scrieți o funcție
def parse_report(txt):
    pass
# ce returnează o listă de liste
# fiecare element fiind de forma
# [Name, Age, City]
# adică:
[
    ["Gigel", "20", "Copenhaga"],
    # ["Andrei", ...]
    # ...
]

# strategie:
# 1. îl spargem în rânduri --> o listă de string-uri, fiecare string = un rând
'-----------------------------------'
'| Gigel      |  20 | Copenhaga    |'

# 2. vedem cum scăpăm de cele care nu sunt rânduri cu date adevărate

# 3. pt. fiecare rând cu date, split-uim după '|'

# [dacă nu vă vine o idee salvatoare, vă opriți la acest punct]

# 4. vrem să facem cleanup (strip) pe fiecare element
#    al row-ului de date curent

def parse_report(txt):
    my_lst = []

    # ne apucăm să acumulăm în my_lst
    for row in txt.splitlines()[3:-1]:
        cells = row.split('|')[1:-1]
        my_lst.append(list(
            map(str.strip, cells)
        ))

    return my_lst

print(parse_report(s))
