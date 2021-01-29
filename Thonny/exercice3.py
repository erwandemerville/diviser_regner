NB_COMP = 0

def maximum(liste):
    global NB_COMP
    max = liste[0]
    for i in range(1, len(liste)):
        NB_COMP += 1
        if liste[i] > max:
            max = liste[i]
    return max

def maximum2(liste):
    max = 0
    for v in liste:
        if v > max:
            max = v
    return max

maximum([2,4,6,8,10,12,14,16,18, 20, 22, 24, 25, 26, 27, 28])
print(NB_COMP)