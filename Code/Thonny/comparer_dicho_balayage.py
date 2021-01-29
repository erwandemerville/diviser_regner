from time import process_time

""" VALEUR A MODIFIER """
nb_de_valeurs = 1000000
""" ----------------- """

T = [v for v in range(0, nb_de_valeurs + 1, 2)]
derniere_valeur = nb_de_valeurs

temps_debut = process_time() # Définir le temps de début

def dicho_r(liste, elt, g=None, d=None):
    
    # Si g et d ne sont pas définis, on les définit :
    if g == d == None:
        g = 0
        d = len(liste) - 1
    
    # Si l'indice de gauche est supérieur à l'indice de droite
    if g > d:
        return False
    
    m = (g + d) // 2 # Définir le milieu
    if liste[m] == elt:
        return True
    elif elt < liste[m]:
        return dicho_r(liste, elt, g, m - 1)
    else:
        return dicho_r(liste, elt, m + 1, d)

dicho_r(T, derniere_valeur)

temps_fin = process_time() # Définir temps de fin
# On calcule le temps entre debut et fin pour connaître le temps d'exécution de dicho_r :
print("Temps méthode par dichotomie (récursif) : {}".format(temps_fin - temps_debut))

temps_debut = process_time()

def recherche(liste, elt):
    for i in range(len(liste)):
        if liste[i] == elt:
            return True
    return False

recherche(T, derniere_valeur)

temps_fin = process_time()
print("Temps méthode par balayage : {}".format(temps_fin - temps_debut))