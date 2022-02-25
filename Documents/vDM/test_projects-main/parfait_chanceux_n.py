from math import sqrt

from itertools import count, islice

def estPremier(n):
    if n < 2:
        return False

    #je prefere chercher les diviseurs de n inclure entre 2 a racine carree de n.
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


def  sommeDiv(n):
    divider = 1
   
    for number in islice(count(2), int(n/2 +1) ):
        if n % number == 0:
            divider +=number
    return divider

    
def estParfait(n):
    sum = sommeDiv(n)
    if sum == n:
        return True
    return False

def estChanceux(n):
   
    for i in range(0, n-1):
        if estPremier(n+i+i**2):
            return True 
        else: 
            return False
    return 


# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def verif(entree, reference, precision=0, comment="") :
    """Vérifie que le nombre <entree> est égal à <référence>, à la précision près."""
    print("{} [{}, {}]".format(comment, entree, reference), end="")
    


# test automatique
if __name__=='__main__' :
    n=8
    verif( sommeDiv(n), 7, comment="\nTeste la fonction 'sommDiv' :")
    verif( estParfait(n), False, comment="\nTeste la fonction 'estParfait' :")
    verif( estPremier(n), False, comment="\nTeste la fonction 'estParfait' :")
    verif( estChanceux(n), False, comment="\nTeste la fonction 'estParfait' :")

