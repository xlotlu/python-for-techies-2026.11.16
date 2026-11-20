import random
from time import sleep

def random_generator(a, b):
    while True:
        yield random.randint(a, b)

mygen = random_generator(1, 200)

for elem in mygen:
    print(elem)
    sleep(1)


# utilitate:
# - file pointer-ul este iterabil linie cu linie
# - csv reader-ul primește orice iterabil,
#   deci îl iterează linie cu linie
#   (implicație: până acum nimic nu este acumulat în memorie)
# - dacă facem o funcție care iterează pe un csv.reader
#   și facem yield pe ce citim de acolo
#   totul va fi streaming.

import csv
import datetime

def process_temps(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)
        for tstamp, value in reader:
            yield (
                datetime.time.strptime(tstamp, "%H:%M:%S"),
                float(value)
            )
mytemps = process_temps("data/temp_sensor_data.csv")

from time import sleep
for elem in mytemps:
    print(elem)
    sleep(1)
