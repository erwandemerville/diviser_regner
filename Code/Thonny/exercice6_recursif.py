def dicho_r(liste, elt, g=None, d=None):
    """ Algorithme récursif de recherche d'un élément dans une liste triée.
    :param liste: (list d'int) Liste triée
    :param elt: (int) Element à chercher
    :param g: (int) Premier élément pris en compte dans la liste
    :param d: (int) Dernier élément pris en compte dans la liste
    :CU: len(liste) >= 1
    :Conditions d'arrêt: Si g > d, ou si l'élément est trouvé. """
    
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


""" AUTRES ALGORITHMES RECURSIFS MOINS EFFICACES (car on fait des copies de la liste) """
""" DANS LE PIRE DES CAS : Complexité linéaire """

def dicho_r2(liste, elt):
    """ Algorithme récursif de recherche d'un élément dans une liste triée.
    :param liste: (list d'int) Liste triée
    :param elt: (int) Element à chercher
    :CU: len(liste) >= 1
    :Condition d'arrêt: La liste ne contient qu'un élément """
    
    if len(liste) == 1:
        if liste[0] == elt:
            return True
        else:
            return False
    else:
        m = (len(liste) - 1) // 2
        if liste[m] >= elt:
            return dicho_r2(liste[:m + 1], elt)
        else:
            return dicho_r2(liste[m + 1:len(liste)], elt)

def dicho_r3(liste, elt):
    """ Algorithme récursif de recherche d'un élément dans une liste triée.
    :param liste: (list d'int) Liste triée
    :param elt: (int) Element à chercher
    :CU: len(liste) >= 1
    :Condition d'arrêt: L'indice m est supérieur à la taille de la liste 
    ou l'élément au milieu est l'élément recherche"""
    
    m = len(liste) // 2
    
    if m >= len(liste):
        return False
    elif liste[m] == elt:
        return True
    elif liste[m] > elt:
        return dicho_r3(liste[:m], elt)
    else:
        return dicho_r3(liste[m + 1:], elt)