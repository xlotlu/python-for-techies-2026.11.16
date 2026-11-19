import csv

f = open("data/crazy-csv.csv")
reader = csv.DictReader(f)

# implementare 1:
for row in reader:
    print(row)

    c = row['conturi']
    s = row['sume']

    accounts = c.split("|")
    #sums = list(map(int, s.split('|')))
    sums = [
        int(v)
        for v in s.split('|')
    ]

    mapping = dict(zip(accounts, sums))
    print(mapping)

# implementare 2:
# din dicționarul inițial de row
# îmi înlăturez coloanele specifice
# de conturi și sume, pentru a le splita
# într-un alt dicționar
f = open("data/crazy-csv.csv")
reader = csv.DictReader(f)

for row in reader:
    c = row.pop('conturi')
    s = row.pop('sume')

    accounts = c.split("|")
    #sums = list(map(int, s.split('|')))
    sums = [
        int(v)
        for v in s.split('|')
    ]

    mapping = dict(zip(accounts, sums))

    # și la sfârșit îl extind pe row
    # cu mapping-ul de conturi
    #row.update(mapping)
    print(row)



# problem statement:
# un csv, în care avem, row cu row,
# informații liniare, dar ep 2 coloane avem o dimensiune nouă
#
# și ce vrem să obținem:
# dimensiunea nouă să fie "flattened"
# rezultat final:
# coloană_1, coloană_2, subdimension_value_1, subdimension_value_2

# versiunea finală:
# (incluzând cum se lucrează corect, curat, cu fișiere)

with open("data/crazy-csv.csv") as f, open("report.csv", 'w') as fout:
    reader = csv.DictReader(f)

    #writer = csv.DictWriter(fout,
    #                        fieldnames=('nume', 'telefon', 'cont', 'suma', 'address'),
    #                        extrasaction='ignore',
    #                        )

    # în loc să folosim versiunea de sus cu numele coloanelor hardcoded,
    #
    # generalizăm ca să ne rămână toate coloanele din sursă
    # în afară de 'conturi' și 'sume':
    fields = reader.fieldnames.copy()
    fields.remove('conturi')
    fields.remove('sume')
    fields += ['cont', 'suma']

    writer = csv.DictWriter(fout, fieldnames=fields)
    writer.writeheader()

    for row in reader:
        c = row.pop('conturi')
        s = row.pop('sume')

        accounts = c.split("|")
        #sums = list(map(int, s.split('|')))
        sums = [
            int(v)
            for v in s.split('|')
        ]

        accounts = dict(zip(accounts, sums))

        # aici voi vrea coloanele rămase din row
        # împreunate cu fiecare pereche din mapping
        #
        # deci vrem un row nou pentru fiecare
        # pereche din mapping

        for item in accounts.items():
            # și la sfârșit îl extind pe row
            # cu mapping-ul de conturi
            #row.update(mapping)

            # ba nu, vreau o să iau invers:
            # îmi creez un dicționar pentru
            # contul-suma curente,
            # și pe el îl extind cu ce a rămas din row


            data = dict(zip(['cont', 'suma'], item))
            data.update(row)

            writer.writerow(data)
