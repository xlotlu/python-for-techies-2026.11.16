# 1. Dat fiind string-ul
s = "Ce dimineață minunată de scris Python!"

# printați:

# a) primele 12 caractere
print(s[:12])

# b) ultimele 7 caractee
print(s[-7:])

# c) caracterele de la indexul 18 la 26 inclusiv
print(s[18:27])

# d) al 28-lea și al 29-lea caracter
print(s[27:29])

# e) întregul string scris de la coadă la cap
print(s[::-1])


# 2. Scrieți o funcție
def prompt_for_int():
    pass
# ce promptează utilizatorul pentru un număr întreg,
# și îl returnează drept int.
#
# dacă string-ul introdus de utilizator nu este
# numeric, va da un mesaj de eroare și va repeta
# promptul la nesfârșit, până când primește
# un număr întreg.
#
# implementați cel puțin una din versiunile următoare:
#
# a) folosind metoda .isdecimal() a str-ului
#
# b) folosind try / except astfel:
# try:
#     # transformare în număr întreg
# except TipulDeExcepțiePotrivit:
#     # logică în caz de eroare
# else:
#     # logică în caz de succes


def prompt_for_int():
    number = input("Nr. întreg? ")

    while not number.isdecimal():
        print("Eroare: nu a fost număr întreg")
        number = input("Nr. întreg? ")

    # totul în regulă
    return int(number)


def prompt_for_int():
    while True:
        number = input("Nr. întreg? ")

        if number.isdecimal():
            return int(number)

        print("Eroare: nu a fost număr întreg")


def prompt_for_int():
    while True:
        number = input("Nr. întreg? ")

        try:
            number = int(number)
        except ValueError:
            print("Eroare: nu a fost număr întreg")
        else:
            return number


def prompt_for_int():
    while True:
        number = input("Nr. întreg? ")

        try:
            return int(number)
        except ValueError:
            print("Eroare: nu a fost număr întreg")


def prompt_for_int():
    while True:
        number = input("Nr. întreg? ")

        try:
            number = int(number)
        except ValueError:
            print("Eroare: nu a fost număr întreg")
            continue

        return number