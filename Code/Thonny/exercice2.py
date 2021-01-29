n = int(input("Saisir un nombre entier: "))

def somme(n):
    if n == 0: # Condition d'arrêt
        resultat = 0
    else:
        resultat = somme(n - 1) + n*n
    return resultat

print("le résultat est:", somme(n))