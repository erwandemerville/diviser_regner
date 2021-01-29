def tri_insertion(tab):
    taille = len(tab)
    for j in range(1, taille):
        cle = tab[j]
        i = j - 1
        while i >= 0 and tab[i] > cle:
            tab[i + 1] = tab[i]
            i = i - 1
        tab[i + 1] = cle