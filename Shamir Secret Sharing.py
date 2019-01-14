import random
from math import ceil

def lagrange(shares,t):
    sums = 0
    prod_arr = []
    if len(shares) < t:
        raise Exception("Shares provided less than threshold. Secret generation not possible")
    for j in range(len(shares)):
        xj,yj = shares[j][0],shares[j][1]
        prod = 1
        for i in range(len(shares)):
            xi = shares[i][0]
            if i != j: prod *= xi/(xi-xj)  
        prod *= yj
        sums += prod
    return ceil(sums)
            

def polynom(x,coeff):
    y = 0
    for i in range(len(coeff)):
        y += (x**(len(coeff)-i-1)) * coeff[i]
    return y

def code(key):
    res = []
    for i in key:
        res.append(str(ord(i.upper())))
    return int(''.join(res))

def coeff(t,secret):
    coeff = []
    for i in range(t-1):
        coeff.append(random.randrange(0,secret))
    coeff.append(secret)
    return coeff

def shares(n,m,secret):
    cfs = coeff(m,secret)
    shares = []
    for i in range(1,n+1):
        shares.append([i,polynom(i,cfs)])
    return shares

def main():
    print("1.Generate Shares 2.Reconstruct Secret")
    i = int(input())
    if i == 1:
        print("Participants: ",end=" ")
        n = int(input())
        print("Threshold:    ",end=" ")
        m = int(input())
        print("Secret:       ",end=" ")
        secret = int(input())
        share = shares(n,m,secret)
        for s in share:
            print(s[0],s[1])
        return
    elif i == 2:
        print("Threshold: ",end=" ")
        thres = int(input())
        print("No. of attempting shares: ",end=" ")
        s_no = int(input())
        s_arr = []
        for c in range(1,s_no+1):
            print("Enter share number:",end=" ")
            share_no = int(input())
            print("Enter share value:",end="")
            inp = int(input())
            s_arr.append([share_no,inp])
        print("Secret is :",lagrange(s_arr,thres))
        return
        
while True:
    main()

    
