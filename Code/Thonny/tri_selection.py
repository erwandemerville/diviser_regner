def tri_selection(tab):
    # Pour chaque valeur du tableau :
    for i in range(len(tab)):
        
        # Trouver le minimum parmi les valeurs suivantes
        min = i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
    
        # Echanger la valeur à l'indice i avec la valeur min
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp