def plus_grand(elt1, elt2):
    if elt1 > elt2:
        return elt1
    else:
        return elt2

def maximum_r(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        # On définit gauche et droite par compréhension :
        gauche = [liste[i] for i in range(0, len(liste)//2)]
        droite = [liste[i] for i in range(len(liste)//2, len(liste))]
        return plus_grand(maximum_r(gauche), maximum_r(droite))

# Autre méthode :
def maximum_r2(liste, gauche=None, droite=None):
    if gauche == droite == None:
        gauche = 0
        droite = len(liste) - 1
        
    if gauche == droite:
        return liste[gauche]
    else:
        milieu = (droite + gauche)//2
        return plus_grand(maximum_r2(liste, gauche, milieu), maximum_r2(liste, milieu + 1, droite))