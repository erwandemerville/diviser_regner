def maximum_r(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        gauche, droite = liste[:len(liste)//2], liste[len(liste)//2:]
        max_gauche, max_droite = maximum_r(gauche), maximum_r(droite) 
        if max_gauche > max_droite:
            return max_gauche
        else:
            return max_droite