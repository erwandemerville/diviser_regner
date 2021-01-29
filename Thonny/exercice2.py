def somme(n):
    if n == 0: # Condition d'arrêt
        return 0
    else:
        return somme(n - 1) + n*n