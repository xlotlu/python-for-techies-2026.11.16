# context managers
# introdus cu statement-ul `with`:
# with ctx_manager:
#     pass
# with ctx_manager as v:
#     pass

# de ce există context managere?
# Q: pentru că:
# A: garantează execuția de cod specific
# - la intrarea în context
# - și la ieșirea din context

# pe vremuri când lucram fișiere făceam așa:

f = open("new-file.txt", 'w')
# vrem neapărat ca acest file pointer să fie închis
# după ce terminăm treaba cu el

# Q: de ce?
# A: dacă ar rămâne acesta deschis, plus alte câteva zeci de mii,
# la un moment dat OS-ul nu va mai putea aloca
# file handlere, deci nu va ia putea deschide fișiere noi

try:
    print("fac chestii cu f")
    #1 / 0
finally:
    # se execută, garantat,
    # chiar dacă a existat excepție sau nu
    print("închid fișierul")
    f.close()

# Despre `open()` drept context manager:
# garantează că își face singur `.close()`

try:
    with open("new-file.txt", 'w') as f:
        print("fac chestii cu f")
        1 / 0
except ZeroDivisionError:
    print("silent error handling")

print("closed?", f.closed)


# Alt exemplu de context manager

import sqlite3

conn = sqlite3.connect("my-test.db")
conn.execute(
    "CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)"
)

# conexiunea de sqlite3 poate fi folosită drept context manager:

try:
    with conn:
        # statement-uri care sunt cuprinse
        # într-o tranzacție
        # care face auto-rollback on any exception
        #       sau auto-commit on no exception
        conn.execute(
            "INSERT INTO lang(name) VALUES('Rust')"
        )
        conn.execute(
            "INSERT INTO lang(name) VALUES('C++')"
        )
        1 / 0
except ZeroDivisionError:
    print("a fost problemă")
    # (s-a făcut auto-rollback)

# hai să vedem ce s-a inserat
cursor = conn.execute("SELECT * FROM lang")
for elem in cursor:
    print(elem)

# de data asta fără excepție:
with conn:
    conn.execute(
        "INSERT INTO lang(name) VALUES('Rust')"
    )
    conn.execute(
        "INSERT INTO lang(name) VALUES('C++')"
    )

cursor = conn.execute("SELECT * FROM lang")
for elem in cursor:
    print(elem)
