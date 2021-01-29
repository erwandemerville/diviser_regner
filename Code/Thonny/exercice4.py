def maximum(liste):
    max = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

def maximum2(liste):
    max = 0
    for v in liste:
        if v > max:
            max = v
    return max