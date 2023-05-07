from sympy import factorint
import random

def inverse(a,p):
    """Finds the inverse of a mod p
    using the Extended Euclidean Algorithm."""
    u,g,x,y = 1,a,0,p
    while y != 0:
        q,t = g//y, g%y
        s = u - q*x
        u,g = x,y
        x,y = s,t
    while u < 0:
        u = u + p
    return u % p

def suntzu(a,m,b,n):
    """Find x so that x = a mod m and x = b mod n.
    AKA the Chinese Remainder Theorem."""
    x, y = inverse(n, m), inverse(m, n)
    N = m * n
    return (a * x * n + b * y * m) % N

def multisuntzu(a,m):
    """Apply Sun Tzu to multiple congruences."""
    while len(a) > 1:
        a[1],m[1] = suntzu(a[0],m[0],a[1],m[1]), m[0]*m[1]
        del a[0]
        del m[0]

    return a[0]

def fpa(a,n,m):
    """Compute a^n mod m."""
    p=1 # p = the eventual answer
    while n>0:
        if n%2 == 1:
            p = p*a % m
        a,n = (a*a) % m, n//2
    return p

def gcd(a,b):
    """Computes gcd of a and b."""
    while b!= 0:
        a,b = b,a%b
    return a

def primeFactor(n):
    """Returns the prime factoriztion of n. 
    Works but is slow."""
    orig = n
    list = []
    while n%2 == 0:
        list, n = list + [2], n//2   
    i = 3
    while i <= n and n != 1:
        #print(i*i, n)
        while n%i == 0:
            list,n = list + [i],n//i
        i += 2
    list.sort()
    check = 1
    for i in range(len(list)):
        check = check * list[i]
    return list

def uniqueLists(list):
    """Returns unique numbers in one list and the multiplicity
    of each number in another list."""
    numList = []
    multiplicityList = []
    while len(list) != 0:
        target = list[0]
        numList, mult = numList + [target], 0
        for i in range (len(list)):
            if list[i] == target:
                mult += 1
        multiplicityList.append(mult)
        list = [x for x in list if x!=target]

    return numList,multiplicityList

def factor(n):
    """Computes all factors of n, including 1 and n."""
    list = []
    i = 1
    while i*i <= n: #loops from 1 to sqrt(n)
        if n%i == 0:
            list = list + [i]
            if n//i != i:
                list = list + [n//i]
        i += 1
    list.sort()
    return list

def order(g,n):
    """Computes the order of g mod n."""
    divisors = factor(n-1)
    for i in range(len(divisors)):
        if fpa(g,divisors[i],n) == 1:
            return divisors[i]    
    return False

def simpleDLPSolver(g,h,p):
    """Solves the DLP g^x = h mod p using brute force.
    Useful for small values of p."""
    temp = 1
    for i in range(p):
        if h == temp:
            return i
        temp = (temp*g)%p
    return False

def babyStep(g, p, N):
    """Returns the baby step list in Shanks' Algorithm"""
    baby = {}
    temp = 1
    for i in range(N+1):
        baby[temp], temp = i, (temp * g) % p
    return baby

def giantStep(baby,h,u,N,p):
    """Returns the giant step values of i,j for Shanks' Algorithm"""
    target = h
    for j in range(N+1):
        if target in baby:
            return (baby[target], j)
        target = (target * u) % p
    return False, False

def shanks(g,h,p): 
    """Solve the DLP g^x = h mod p using
    Shanks' Babystep-Giantstep Algorithm."""
    
    #Note that the order can be hard-coded to p-1
    #if g is a primitive root (faster)
    order_g = order(g,p)
    N = int((order_g)**(0.5)) + 1
    u = fpa(inverse(g,p),N,p) # u = g^{-n}
    baby = babyStep(g,p,N)
    i,j = giantStep(baby, h, u, N, p)
    return (i + (j*N))

def pohligHellman(g,h,p):
    """Solves the DLP g^x = h mod p using
    the Pohlig-Hellman Algorithm."""
    
    #Sympy factorization was used. The function
    #primeFactor above works, but is slow.
    print("Beginning Factorization of p =",p)
    primeFactorDict = factorint(p-1)
    primeList = list(primeFactorDict.keys()) #changes dictionary keys to list
    multList = list(primeFactorDict.values())#changes dictionary values to list
    print("Factorization Complete:", p,"=",primeList, "with exponents", multList)
    
    congList = []
    for i in range (len(primeList)):
        pPrime = fpa(primeList[i],multList[i],p) #pPrime = (p_{e_i})^{e_i}
        primeList[i] = pPrime #Necessary for suntzu to work with repeated prime factors
        r = (p-1)//pPrime
        hPrime = fpa(h,r,p) #h^{(p-1) / (p_{e_i}^{e_i})}
        gPrime = fpa(g,r,p) #g^{(p-1) / (p_{e_i}^{e_i})}
        print("Solving h^(",r,")= (g^x)^(",r,") mod p")
        if primeList[i] < 1000: #brute force DLP solve if small prime #
            congList = congList + [simpleDLPSolver(gPrime,hPrime,p)]
        else: #Shanks DLP solve if large prime #
            congList = congList + [shanks(gPrime,hPrime,p)]
        print("Solved! x =", congList[i], "mod",pPrime)
    print("Beginning Chinese Remainder Theorem")
    return multisuntzu(congList,primeList)

def kQCalculator(n):
    """Find k,q in equation n-1 = q*2^k"""
    k = 0
    q = n-1
    while q % 2 == 0:
        q = q // 2
        k += 1
    return k,q

def millerRabin(n,t):
    """Returns True if n is Prime and False if 
    n is composite."""
    numTrials = t
    t = 0
    if n == 2:
        return True

    while t < numTrials:    
        a = random.randint(1,n-1)
        witness = a
        if (n % 2 == 0) or (gcd(a,n) > 1):
            return False
        
        k,q = kQCalculator(n)
        a = fpa(a,q,n)
        doSquaring = True
        if a == 1:
            t += 1
            doSquaring = False
        
        i = 0
        keepLooping = True
        while keepLooping and doSquaring:
            if (a+1)%n == 0:
                t += 1
                keepLooping = False
            if i >= k+1:
                return False
            i += 1
            a = a*a%n
    return True

print("g^x = h mod p")
p = int(input("p:"))
g = int(input("g:"))
h = int(input("h:"))

choice = "y"
if (not millerRabin(p,10)):
    choice = input("It appears that p is not prime. Try anyways? (y/n):")

if choice[0].lower() == "y":
    print("x =",pohligHellman(g,h,p))