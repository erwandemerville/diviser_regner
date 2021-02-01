def fusion(L1, L2):
    """ Fonction retournant une liste triée, fusion de deux listes triées.
    :param L1: (list d'int) Liste d'entiers triée
    :param L2: (list d'int) Liste d'entiers triée
    :return: (list d'int) Fusion des deux listes triées """
    
    if L1 == []:
        return L2
    elif L2 == []:
        return L1
    elif L1[0] < L2[0]:
        return [L1[0]] + fusion([L1[i] for i in range(1, len(L1))], L2)
    else:
        return [L2[0]] + fusion(L1, [L2[i] for i in range(1, len(L2))])
    
def tri_fusion(Liste):
    """ Effectue le tri fusion de la liste passée en entrée.
    :param Liste: (list d'int) Liste d'entiers
    :return: (list d'int) Une liste d'entiers triée """
    
    n = len(Liste)
    if n <= 1:
        return Liste
    else:
        m = n // 2
        return fusion(tri_fusion([Liste[i] for i in range(0, m)]),
                      tri_fusion([Liste[i] for i in range(m, n)]))
