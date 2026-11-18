# "EOF" = end of file

fp = open("orar.txt")
fp.read() # citește tot conținutul curent

# acum orice fp.read() va continua de la finalul precedent

# putem să facem rewind cursorului cu
fp.seek(0)
# dar în practică ar fi cazul să nu aveți nevoie
# (dacă chiar aveți nevoie înseamnă că faceți ceva avansat)

# vrem să facem:
content = fp.read()
# acum avem content în memorie, facem ce vrem cu el



fp = open("orar.txt") # aceasta este o cale relativă

open("data/test.txt") # altă cale relativă

# relativ = relativ la directorul curent al executabilului Python.
#           care este (la început!) directorul unde a fost pornit procesul.

REPORTS_DIRECTORY = "/tmp/the-directory/with-reports"

# vreau să deschid pe "test.txt" din `REPORTS_DIRECTORY`

# don't do this
fname = REPORTS_DIRECTORY + '/' + "test.txt"

# but do this:

# either:
# A) new-school, pythonic:
from pathlib import Path

repdir = Path(REPORTS_DIRECTORY)
fname = repdir / "test.txt"
# aici fname este un obiect de tip Path

# B) old-school:
from os import path

fname = path.join(REPORTS_DIRECTORY, "test.txt")
# aici fname este string


# comparație între rezultate dacă am avea ending slash:
REPORTS_DIRECTORY = "/tmp/the-directory/with-reports/"
#
REPORTS_DIRECTORY + '/' + "test.txt"
# vs.
path.join(REPORTS_DIRECTORY, "test.txt")
# vs.
Path(REPORTS_DIRECTORY) / "test.txt"

# când lucrăm cu path-uri de Windows,
# ținem minte că \ este escape character,
# și poate să introducă un escape sequence:

# motiv pentru care facem escape-ing
"C:\\Users\\MyUser\\Desktop\\new-folder"

# sau scriem "raw string"
r"C:\Users\MyUser\Desktop\new-folder"
