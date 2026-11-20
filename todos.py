# strategie de ordonat import-urile:
# 1. cele din standard library
import json
import csv
from pathlib import Path
# 2. cele din module externe instalate
import requests

# 3. cele care au legătură strictă cu aplicație
from config import TODOS_URL, TODOS_DIRECTORY


def load_todos(url=TODOS_URL):
    """
    returns a list of todos.
    each todo is a dictionary.
    """
    response = requests.get(url)
    return response.json()

# vrem să salvăm în directorul de output
# fiecare TODO drept un fișier json
# de sine stătător, cu numele
# "<id>.json"

def save_todos(todos, target_dir=TODOS_DIRECTORY):
    """
    receives a list of todos, each a dictionary
    and saves them as separate json files
    in `target_dir`.
    """
    # este creat target_dir?
    target_dir = Path(target_dir)
    if not target_dir.exists():
        target_dir.mkdir()

    for todo in todos:
        # todo este dict
        # să îl salvăm drept json

        # scriem fișierele în target_dir
        fpath = target_dir / f"{todo['id']}.json"

        # deschidem fișierul în mod write:
        with open(fpath, 'w') as f:
            json.dump(todo, f)


def todos_to_csv(todos, csvfile, completed=None):
    """
    saves the given `todos` to `csvfile`
    filtering by `completed`.

    if `completed` is None, save all todos.
    """

    with open(csvfile, 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=('id', 'userId', 'title', 'completed')
        )

        # dacă vrem să-i scriem header-ul:
        writer.writeheader()

        for todo in todos:
            # we must filter
            if (
                completed is None
                or
                todo['completed'] == completed
            ):
                writer.writerow(todo)


# Q: dacă vrem să facem un modul hibrid
# care funcționează și ca library
# (se poate face import din el)
# și ca executabil
# (ca script)

# A: găsim o cale pt. a ne da seama
# dacă suntem executați sau importați

# print(__name__) # numele modulului curent

# # 1) când este executat:
# "__main__"
# # 2) când este importat:
# "todos"

if __name__ == "__main__":
    # eu sunt app entry point
    print("o să execut toate astea!!!")
    todos = load_todos()
    save_todos(todos)
    todos_to_csv(todos, "todos.csv", completed=False)

    # notă: dacă vă găsiți cu nevoia de a crea
    # script-uri complexe (cu varii argumente)
    # folosiți modulul `argparse`

