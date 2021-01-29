def dicho_i(liste, elt):
    """ Algorithme itératif de recherche d'un élément dans une liste triée.
    :param liste: (list d'int) Liste triée
    :param elt: (int) Element à chercher
    :CU: len(liste) >= 1 """
    
    deb = 0
    fin = len(liste) - 1
    m = (deb + fin) // 2
    while deb <= fin :
        if liste[m] == elt :
            # L'élément est à l'indice m
            return True
        elif liste[m] > elt :
            # On regarde avant l'indice m
            fin = m - 1
        else :
            # On regarde après l'indice m
            deb = m + 1
        m = (deb + fin) // 2
    return False