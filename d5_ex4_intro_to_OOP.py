# în python totul este un obiect.
# un obiect = o instanță a unei clase.

class MyClass:
    pass

class MyClass:
    def mymethod(self): # "self" este obiectul curent
        print("sunt o metodă")
        print("mă rulez pe obiectul", self)

obj = MyClass()
obj.mymethod()

class MyClass:
    # aceasta dă semnătura clasei
    def __init__(self, arg):
        # assignment de atribut
        self.value = arg

import math

class Point:
    "describes a 2-dimensional point"
    def __init__(self, x, y):
        self.x = x # acesta este un atribut
        self.y = y

    # aceasta dă reprezentarea obiectului
    def __repr__(self):
        # returnează un string
        return f"Point({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

p = Point(1, 2)
print(p)
p.translate(2, 2)
print(p)
print(p.get_distance_from_origin())


# un decorator important în context de clase:
# @property
class Point:
    "describes a 2-dimensional point"
    def __init__(self, x, y):
        self.x = x # acesta este un atribut
        self.y = y

    # aceasta dă reprezentarea obiectului
    def __repr__(self):
        # returnează un string
        return f"Point({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        print("m-a transformat într-un atribut aparent")
        print("dar de fapt sunt funcție care se execută")
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

p = Point(3, 4)
print(p.distance_from_origin)
p.translate(3, 4)
print(p.distance_from_origin)
