def sliceNChunks(num, n):
    """Divides a number into chunks of size n."""
    returnList = []
    num = str(num)
    while num:
        returnList = returnList +  [int(num[:n])]
        num = num[n:]
    return returnList

def processOrderedPair(m):
    """Turns string (c1,c2) into integers c1, c2."""
    m = m.replace(" ","")
    m = m.replace("(","")
    m = m.replace(")","")
    m = tuple(map(int, m.split(",")))
    return int(m[0]),int(m[1])

def listToChar(list):
    """Turns a list of ints into a list of ASCII characters."""
    result = []
    for i in range(len(list)):
        result = result + [chr(list[i])]
    return result

def inverse(a,p):
    """Finds the inverse of a mod p."""
    u,g,x,y = 1,a,0,p
    while y != 0:
        q,t = int(g/y), g%y
        s = u - q*x
        u,g = x,y
        x,y = s,t
    while u < 0:
        u = u + p
    return u % p

def fpa(a,n,m):
    """Compute a^n mod m."""
    p=1 # p = the eventual answer
    while n>0:
        if n%2 == 1:
            p = p*a % m
        a,n = (a*a) % m, n//2
    return p

def elGamal(p, a, c1,c2):
    """Computes ASCII Numbers of Elgamal characters"""
    c1Inverse = inverse(c1,p)
    c1 = fpa(c1Inverse,a,p)
    return (c2*c1) % p

print("Be sure to run Pohlig-Hellman first to obtain the private key a.")
p = int(input("Prime p: "))
a = int(input("Private Key a: "))
numMessages = int(input("How many messages (c1,c2): "))
charList = []
for i in range(numMessages):
    m = input("Message (c1,c2): ")
    c1, c2 = processOrderedPair(m)
    message = elGamal(p, a, c1,c2)
    charList = charList + [str(message)]

result = "".join(charList)
asciiList = sliceNChunks(int(result), 2)
charList = listToChar(asciiList)
print("List of ASCII values: ",asciiList)
print("Plaintext:", "".join(charList))