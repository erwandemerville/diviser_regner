n = int(input("Saisir un nombre entier: "))

def somme(n):
    resultat = 0
    for i in range (n):
        resultat = resultat + i*i
    return resultat

print("le résultat est:", somme(n+1))

