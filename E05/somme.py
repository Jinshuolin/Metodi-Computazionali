import numpy as np


def sum (n):
    somma =0
    for i in range (n+1):
        somma = somma + i
    return somma

def sum_root ( n ):
    somma =0
    for i in range (  n+1 ):
        somma = somma + np.sqrt(i)
    return somma
def sumprod ( n):
    somma = 0
    prod = 1
    for i in range ( 1, n+1 ):
        somma = somma + i
        prod = prod * i
    return somma, prod
def sum_exp (n, a=1):
    """
    Si suppone che sia n che a siano appartenenti all'insime dei numeri naturali
    """
    sum = 0
    for i in range ( 1, n+1):
        sum = sum + i**a
    return sum


        
    
