def func(a, b):
    print("» a", a)
    print("» b", b)

# capturează oricâte argumente poziționale:
def func(a, b, *args): # "positional-argument packing"
    print("» a", a)
    print("» b", b)
    print("» args", args) # tuplă

# keyword arguments:
def func(a, b, *args, kw1="un default", kw2="alt default"):
    print("» a", a)
    print("» b", b)
    print("» args", args) # tuplă
    print("» kw1", kw1)
    print("» kw2", kw2)

# oricâet keyword arguments:
def func(a, b, *args, kw1="un default", kw2="alt default", **kwargs): # "keyword-argument packing"
    print("» a", a)
    print("» b", b)
    print("» args", args) # tuplă
    print("» kw1", kw1)
    print("» kw2", kw2)
    print("» kwargs", kwargs)

func(1, 2, un_kw="care nu există", și_altul="aha!!")

# ce am scris mai sus se numește argument packing.
# inversul său: argument unpacking

lst = ["ala", "bala", "porto"]

def myfunc(a, b, c):
    print(a)
    print(b)
    print(c)

myfunc("ala", "bala", "porto")
# exact același lucru
myfunc(*lst)
myfunc(*range(3))

# există și kwarg unpacking:
opts = {
    'end': ' «««\n',
    'sep': ' | ',
}

print("unu", "doi", "trei", **opts)
# echivalent cu
print("unu", "doi", "trei", sep=' | ', end=' «««\n')