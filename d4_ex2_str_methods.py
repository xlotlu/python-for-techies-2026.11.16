# metodele str-ului
s = "Ce dimineață minunată de scris Python!"

# A. foarte importante


# .index() are și start / stop
try:
    s.index("i", 7, 12)
except ValueError:
    pass

# notă importantă:
# la str, .index() și .count() și operatorul `in`
# merg pe stubstring-uri, nu doar pe caractere
s.index("imi")
s.count("mi")
"dimi" in s

# există și .rindex()
s.rindex("i")


# notă despre .count():
# și el are start și end opționale


# split cu argumente splitează după substring
"o coloană | altă coloană | etc.".split(" | ")

# split fără argumente splitează după orice whitespace
# indiferent de lungimea sa:
"        iată ceva     text cu \n\n\n alt text".split()


# exemplu de split cu maxsplit
mypath = r"C:\folder\subfolder\file.txt"
# vreau să obțin
# 1) numele fișierului și
# 2) folderul părinte
mypath.split('\\')[-1] # filename
'\\'.join(mypath.split('\\')[:-1]) # dirname

# sau, folosind rsplit cu argument maxsplit:
dirname, filename = mypath.rsplit('\\', 1)


# despre join(), este inversul lui split():
# dat fiind un iterabil de string-uri
columns = ('name', 'address', 'phone')
# vrem să le unim printr-un caracter (sau string):
" @ ".join(columns)

# .strip by default curăță orice whitespace
"   text  \n\t\r  ".strip() # --> "text"

"====Nume Coloană===".strip("=") # --> "Nume Coloană"
"==#==Nume Coloană=#==".strip("=#") # --> "Nume Coloană"

# Notă:
# există .lstrip() și .rstrip()
# transformați
num = "00012340"
# în număr întreg
int("00012340".lstrip("0"))


# .replace():
s.replace("i", "iii")
# și cu max count:
s.replace("i", "iii", 2)


# TODO
#.format()



# B. uzuale
s.upper()
s.lower()


s.startswith("Ce dimi")
s.endswith("ython!")

# splitlines():
txt = """Acesta este un text\r
pe mai multe linii.\r
Etc.\r
Etc.\r
Etc.\r
"""
# este recomandat să folosim
txt.splitlines()
# vs.
txt.split("\n")
# pentru că splitlines()
# se ocupă și de \r
# (carriage return, care este salvat de editoarele
# native windows)


# C.  din când în când

s.casefold()
# se folosește specific pentru comprații de string-uri
# case-insensitive

s1 = "Un STRING!"
s2 = "un string!"
# Q: cum facem comparație case-insensitive?
# A: le normalizăm ambele
s1.lower() == s2.lower()
s1.upper() == s2.upper()

s1 = "ceva în ß germană"
s2 = "CEVA ÎN SS GERMANĂ"

s1.casefold() == s2.casefold()
# vs.
s1.lower() != s2.lower()



s.isdecimal()
"123".isdecimal()



# D. poate nici nu le mai scriem
s.find("imi") # face același lucru cu .index()
s.find("zimi") # returnează -1 când nu există
