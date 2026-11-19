# exceptions

try:
    print("execut ceva ce ar putea crăpa")
    #s = ""
    #s[0]
    #int("nu e număr")
    1 / 0
except IndexError:
    print("a fost IndexError")
except ValueError:
    print("a fost ValueError")
except Exception as e:
    print("catch-all, prinde orice")
    # TODO: log this serious bug!
    print(type(e), e.args)
else:
    print("totul în regulă!")
finally:
    print("mă execut întotdeauna")


http_methods = ["GET", "POST", "HEAD", "PUT"]
dct = {
    "GET": "get_func",
    "POST": "post_func",
    "HEAD": "head_func",
}

def get_func(idx):
    method = http_methods[idx]
    func = dct[method]
    return func

method_index = 0
try:
    get_func(method_index)
except IndexError:
    print("îi zic celui care m-a chemat:")
    print("unknown index")
except KeyError:
    print("îi zic celui care m-a chemat:")
    print("unsupported method")


try:
    get_func(method_index)
except IndexError, KeyError:
    print("îi zic celui care m-a chemat:")
    print("eroare generică")



# variațiunile de exception handling:

try:
    pass
except: # except Exception as e # etc..
    pass

try:
    pass
except IndexError:
    pass
except KeyError:
    pass
# ... except ....

try:
    pass
except:
    pass
else: # poate să existe doar dacă a existat except
    pass

try:
    pass
finally:
    # tot va exploda dar am avut ocazia să facem cleanup
    pass