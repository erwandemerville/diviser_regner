def factorielle_r(n: int) -> int:
   # Cas de base
   if n == 1:
      return 1
   else:
       # Appel récursif
       return n * factorielle_r(n - 1)
    
def factorielle_i(n: int) -> int:
    fact = 1
    # Boucle exécutant n - 1 itérations
    for i in range(2, n + 1):
        fact = fact * i
    return fact