def fibonacci(n: int) -> int:
    """ Retourne le n-ième terme de la suite de Fibonacci.
    :param n: (int) Numéro du terme souhaité de la suite
    :return: (int) n-ième terme de la suite de Fibonacci
    Condition d'utilisation : n >= 0
    Conditions d'arrêt : n = 0 ou n = 1 """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)