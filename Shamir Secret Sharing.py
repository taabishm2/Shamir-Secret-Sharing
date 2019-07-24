import random
from math import ceil
from decimal import *

global field_size
field_size = 496025623

def tncombinex(shares): #Combines shares using Lagranges interpolation
    '''shares is an array of shares being combined, t is the threshold in the scheme'''
    global field_size
    
    sums = 0
    prod_arr = []
    for j in range(len(shares)):
        xj,yj = shares[j][0],shares[j][1]
        prod = Decimal(1)
        for i in range(len(shares)):
            xi = shares[i][0]
            if i != j: prod *= Decimal(Decimal(xi-x)/(xi-xj))
        prod *= yj
        
        sums += Decimal(prod) % Decimal(field_size)

    ret = Decimal(sums) % field_size
    if ret < 0: ret += field_size
    return ret
            
            

def polynom(x,coeff):
    '''Evaluates a polynomial in x with coeff being the coefficient matrix with a given x'''
    global field_size
    y = 0
    for i in range(len(coeff)):
        y += (x**(len(coeff)-i-1)) * coeff[i] 
    return y % field_size


def coeff(t,secret):
    '''randomly generate a coefficient array for a polynomial with degree t-1 whose constant = secret'''
    global field_size

    coeff = []
    for i in range(t-1):
        coeff.append(random.randrange(0,field_size-1))
    coeff.append(secret)
    
    return coeff

def tnshares(n,m,secret):
    '''Split secret using SSS into n shares with threshold m'''
    global field_size

    cfs = coeff(m,secret)
    shares = []
    for i in range(1,n+1):
        shares.append([i,polynom(i,cfs)])

    return shares
