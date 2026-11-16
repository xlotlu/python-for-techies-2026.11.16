# flow control:
# conditional statements

# toate statement-urile care au sub-bloc de logică
# se încheie cu două puncte :
#if condition:
#    # și sub-blocul lor este indentat
#    statement_1
#    statement_2
#    # etc.


age = 18

if age < 18:
    print("Not of the required age")
else:
    print("Accepted")

# sintaxa completă de if:

# if condition1:
#     statements
# elif condition2:
#     statements
# #...
# elif conditionx:
#     statements
# else:
#     statements

if age < 18:
    age_type = "child"
elif age >= 18 and age < 40:
    age_type = "junior"
elif age >= 40 and age < 60:
    age_type = "senior"
else:
    age_type = "retired"

print(age_type)


# Exercițiu:
# scrieți un condițional care să printeze string-ul de salut
# potrivit orei date.
#
# între ora 5 și 10:  "Bună dimineața"
# între ora 10 și 18: "Bună ziua"
# între ora 18 și 22: "Bună seara"
# între ora 22 și 5:  "Noapte bună"

hour = 14

if hour >= 5 and hour < 10:
    greeting = "Bună dimineața"
elif hour >= 10 and hour < 18:
    greeting = "Bună ziua"
elif hour >= 18 and hour < 22:
    greeting = "Bună seara"
else:
    greeting = "Noapte bună"
print(greeting)

# această implementare va da "Noapte bună"
# pentru ore < 0 și >= 24


ora = 7

if ora >= 5 and ora < 10:
    greeting = 'Buna dimineata'
elif ora >= 10 and ora < 18:
    greeting = 'Buna ziua'
elif ora >= 18 and ora < 22:
    greeting = 'Buna seara'
elif ora >= 22 and ora < 24:
    greeting = 'Noapte buna'
elif ora >=0 and ora < 5:
    greeting = 'Noapte buna'
else:
    greeting = 'ora gresita'
print(greeting)

# în comparație cu implementarea riguroasă
# ce acoperă toate intervalele orare

# dar, comentariu, folosește același canal de comunicare pt. erori.
# (ceea ce nu este o idee bună în programare).


# Cerință:
# scrieți o funcție
def get_greeting_for_hour(hour):
    pass
# ce returnează string-ul potrivit drept salut
# pentru acel moment al zilei.


def get_greeting_for_hour(hour):
    if hour >= 5 and hour < 10:
        return 'Buna dimineata'
    elif hour >= 10 and hour < 18:
        return 'Buna ziua'
    elif hour >= 18 and hour < 22:
        return 'Buna seara'
    elif hour >= 22 and hour < 24:
        return 'Noapte buna'
    elif hour >= 0 and hour < 5:
        return 'Noapte buna'
    #else:
    #    greeting = 'ora gresita'

# în Python există operator chaining:
def get_greeting_for_hour(hour):
    if 5 <= hour < 10:
        return 'Buna dimineata'

    elif 10 <= hour < 18:
        return 'Buna ziua'

    elif 18 <= hour < 22:
        return 'Buna seara'

    elif 22 <= hour < 24:
        return 'Noapte buna'

    elif 0 <= hour < 5:
        return 'Noapte buna'
    #else:
    #    greeting = 'ora gresita'


# funcția finală:
# Q: cum facem să nu primim valori orare nepotrivite?
# A: trimitem o excepție înapoi

def get_greeting_for_hour(hour):
    # early exit în caz de valoare nepotrivită:
    if hour < 0 or hour > 23:
        raise ValueError("Invalid hour")

    if 5 <= hour < 10:
        return 'Buna dimineata'
    elif 10 <= hour < 18:
        return 'Buna ziua'
    elif 18 <= hour < 22:
        return 'Buna seara'
    else:
        return 'Noapte buna'


# Exercițiu:
# 1. luați input de la utilizator, cerându-i ora curentă
#    folosim imput()
# 2. trebuie să transformăm input-ul în număr întreg.
#    folosim int(value)
# 3. salutați-l pe utilizator cu salutul potrivit orei
#    executăm funcția get_greeting_for_hour() pe valoarea rezultată
ora = input("Care este ora? ")
try:
    ora = int(ora)
except ValueError:
    print("Nu ai scris o oră corectă")
else: # deci nu a existat excepție
    print(get_greeting_for_hour(ora))


# Scrieți o funcție
def calculate_price(distance, weight):
    pass
# ce returnează costul de livrare conform următorului algoritm:
# - pentru distanțe < 10:
#   - pentru greutate < 5:   5
#   - pentru restul:         8
# - pentru distanțe >= 10:
#   - pentru greutate < 5:  10
#   - pentru restul:        15


def calculate_price(distance, weight):
    if distance < 10:
        if weight < 5:
            price = 5
        else:
            price = 8
    #elif distance >= 10:
    else:
        if weight < 5:
            price = 10
        else:
            price = 15
    return price


# 1. testați cu:
calculate_price(9, 2)
calculate_price(9, 5)
calculate_price(10, 2)
calculate_price(10, 5)

# apoi 2. promptați utilizatorul
# pentru distanță și greutate
# și returnați-i prețul corespunzător
weight = input("Greutatea pachetului tău? ")
dist = input("La ce distanță va fi transportat? ")
# mai am ceva de făcut ca să meargă...
weight = int(weight)
dist = int(dist)
print(calculate_price(dist, weight))

# introducing new-style string formatting (interpolation)

# date fiind variabilele disponibile
weight = 5
distance = 22
price = calculate_price(distance, weight)

print(
    f"pentru greutate {weight}kg la distanța {distance}km, prețul este: {price}"  # "formatted-string" sau f-string
)
