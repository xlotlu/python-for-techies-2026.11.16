print("Salut!")

# vrem să definim o vriabilă
name = "Numele Meu"

# și să printăm un string de forma
# "Salut Numele Meu!"

# astfel încât să faceți concatenarea
# între
# "Salut", variabila name și "!" de la final

print("Salut " + name + "!")

output = "Salut %s!" % name
print(output)

template = "Salut, tu ești %s, ai %d ani și înălțime de %f"

# multiple interpolation:
print(template % ("Ion", 88.5, 1.80))

# Exercițiu:
# știind că funcția `input()` așteaptă input de la utilizator
# și îl returnează (deci poate fi capturat într-o variabilă):
#
# 1) cereți numele utilizatorului și
# 2) faceți print string-ului de forma
#    "Salut <nume>, bine ai venit!"

#print("Care este numele tău?")
#name = input() # în clipa asta terminalul așteaptă input
#print("Salut %s, bine ai venit!" % name)

# funcția input acceptă un argument opțional,
# prompt-ul pe care să îl prezinte utilizatorului
name = input("Numele tău? ")
print("Salut %s, bine ai venit!" % name)
