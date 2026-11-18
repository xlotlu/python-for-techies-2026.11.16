# Concepte

reprezentarea obiectului: un string care apare la interacțiunea cu developer-ul


Python este whitespace-sensitive.
Indentarea este cea care dă structura algoritmică a codului!

Sintaxa fundamentală:
- orice statement care are sub-bloc de logică
- se va termina cu două puncte
- după care codul sub-blocului este indentat


obiectul este o structură de date
- ce are atribute proprii
- și funcții asociate obiectului ce se numesc metode

obiectul este o instanță a unei clase

```python
from datetime import date
# am importat clasa date din modulul datetime

# instanțiem un obiect:
date(2026, 11, 17)

```


Python is dynamically typed

în Python totul este un obiect (!!!!)
în Python totul este o referință!



"Duck typing": if it walks like a duck and it quacks like a duck, it must be a duck.



# Things to read

(cel puțin o dată în viața de programator)

String formatting:
https://docs.python.org/3/library/string.html#format-examples





# Data types

int     numărul întreg
float   numărul cu virgulă
str     string-ul

bool    `True` sau `False`

tuple   immutable
list    mutable


## despre string-uri:

- nu contează dacă sunt scrise cu ghilimele sau apostroafe.
  doar că vor fi închise cu caracterul cu care sunt deschise.
- backslash ( \ ) este escape character. este folosit pentru
  a face escaping la ghilimele/apostroafe _și_ pentru a introduce
  "escape sequences" speciale:
  - `\n`: newline ("line feed")
  - `\r`: carriage return
  - `\t`: tab
  - `\x`: un escape sequence urmat de două caractere hexadecimale ce
    reprezintă poziția caracterului respectiv în tabelul ASCII.

## sequences:

acestea sunt `str`, `tuple` și `list`.
sunt colecții ordonate, indexate.
ele au în comun:

- sunt iterabile
- au acces după index `lst[idx]` (suportă "item access", care este întodeauna nr. întreg)
- au o lungime dată, deci suportă funcția `len()`
- au metodele `.count()` și `.index()`


# Operatori

ce fac operatorii depinde de tipul de date asupra cărora acționează.


## în context aritmetic

operatori specifici Python:

```
//      partea întreagă a împărțirii
%       restul împărțirii
**      ridicare la putere
```

## în context de string

```
+       concatenare
*       multiplicare (concatenare repetată)
%       interpolare
```

"acesta este un string cu %s o interpolare" % "O VALOARE"


## operatori boolean

==
!=
<
>
<=
>=

and
or
not

is      # testează identitate între obiecte. se folosește doar cu True, False și None
is not


# debugging essentials

print()
type()      # returnează data type-ul (clasa) obiectului inspectat
help()      # afișează semnătura și documentația funcției/ într-un pager
            # (din pager se iese cu tasta q)

# Funcția:

se execută astfel:

- nume,
- parenteze rotunde,
- în paranteze (dacă este cazul) argumentele.

returnează o valoare, pe care o putem asigna unei variabile:

```python
value = myfunc(a, b)
```

funcția poate avea side-effects:
- face print
- citește din (sau scrie în) fișiere, rețea, baze da date etc.

scopul fundamental al funcției este să returneze o valoare,
folosind statement-ul

```
return
```


# Excepțiile

SyntaxError         evident
IndentationError    și el evident

NameError           simbolul respectiv nu este definit

TypeError           1) funcție apelată cu combinație invalidă de argumente
                    2) operațiuni cu data-type-uri incompatibile

IndexError          index inexistent
KeyError            cheie inexistentă

# Very useful packages:

ipython



# Working with VSCode:

Ctrl+F5     # run python file
Shift+Enter # run selection in Python terminal

Ctrl+/      # comentează / decomentează linia sau selecția curentă

Tab         # indentează selecția curentă
Shift+Tab   # dez-indentează selecția sau linia curentă


# varia:
There are 2 most difficult problems in computing:
- naming things
- cache invalidation
- off-by-one errors
