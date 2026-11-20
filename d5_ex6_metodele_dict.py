d = {
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    'Iași': 390,
    'Constanța': 225,
    'Brașov': 180,
}

# returnează o valoare default
d.get('o cheie')    # valoarea default este None
d.get('o cheie', 'default') # --> 'default'
d.get('Cluj-Napoca', 'default') # --> 450

# inversul lui .get(),
# setează valoarea doar dacă cheia nu există:
d.setdefault("Constanța", 500) # --> 225
d.setdefault("Arad", 600) # --> 600

# des util,
# updatează valorile din dicționarul existent cu cele din
# dicționarul primit ca argument.
# (le schimbă pe cele vechi sau creează unele noi)
d.update({
    'Constanța': 300,
    'Brașov': 190,
    'Buzău': 120,
    'Craiova': 300,
})


# șterge cheia din dicționar, returnează valoarea
d.pop('Timișoara') # --> 550

# șterge ultima pereche cheie-valoare în timp ce o returnează
d.popitem()

# use-case:
# dat fiind dicționarul
dcities = {
    'Cluj-Napoca': 450,
    'Timișoara': 550,
    'Iași': 390,
    'Constanța': 225,
    'Brașov': 180,
    'Craiova': 230,
    'Galați': 250,
    'Ploiești': 60,
    'Oradea': 610,
    'Sibiu': 275,
    'Arad': 560,
    'Bacău': 300,
    'Brăila': 200,
    'Buzău': 110,
    'Suceava': 450,
    'Pitești': 120,
    'Târgu Mureș': 330,
    'Baia Mare': 600,
}
# creați două dicționare noi
far_cities = {}
# și
close_cities = {}
# unde cele distante sunt cu distanță > 200.
#
# faceți asta eliberând memoria de elementele
# din dicționarul inițial. (consumându-l în timp ce iterați în el.)

while dcities:
    key, value = dcities.popitem()

    if value > 200:
        far_cities[key] = value
    else:
        close_cities[key] = value


# aceasta este o metodă pe clasa dict:
dict.fromkeys(["ceva", "altceva", "etc."])
dict.fromkeys(range(10), '-- default value --')
# instanțiază un obiect nou cu aceste chei
# (și eventual o valoare default opțională)



# Exercițiu:
# Care este cel mai succint și simplu și direct mod
# să obținem un dicționar nou dintr-unul existent
# sucind cheile <--> valorile?
