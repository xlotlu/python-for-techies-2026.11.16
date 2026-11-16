# o funcție se definește cu statement-ul
# `def`:

def numefunctie():
    #print("logică în interiorul funcției")
    #print("altă logică în interiorul funcției")

    return "o valoare"

value = numefunctie()
print("value a fost:", value)


def add(a, b):
    return a + b
print("adding:", add(5, 7))

# Scrieți of funcție ce returnează rezultatul
# multiplicării
def multiply(a, b):
    return a * b
print("multiplying:", multiply(5, 7))


# Dată fiind variabila globală
M_TO_FT = 3.28084

# scrieți 2 funcții
def m_to_ft(m):
    # și returnează ft
    pass # "no-op" (no operation)

def ft_to_m(ft):
    # și returnează m
    pass

print("10m sunt", m_to_ft(10), "picioare")
print("10ft sunt", ft_to_m(10), "metri")
