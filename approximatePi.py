import math
from decimal import *


# compute the n'th convergent p_n/q_n such that q_n < M is largest
def continuedFraction(M):
    pi = math.pi
    a = []
    b = []
    p = []
    q = []
    b.append(pi)
    a.append(math.floor(pi))
    b.append(1/(pi - a[0]))
    a.append(math.floor(b[1]))

    # compute p[0], q[0], etc.
    p.append(a[0])
    q.append(1)
    p.append(a[1] * a[0] + 1)
    q.append(a[1])
    frac = [a[0], 1]
    
    # start computing with n = 2
    n = 2
    while(frac[1] < M):
        b.append(1/(b[n - 1] - a[n - 1]))
        a.append(math.floor(b[n]))
        p.append(a[n] * p[n - 1] + p[n - 2])
        q.append(a[n] * q[n - 1] + q[n - 2])
        frac = [p[n], q[n]]
        n += 1
    
    frac = [p[n - 2], q[n - 2]]
    # print(frac)
    return frac

def closestFraction(m, M):
    frac = [3, 1]

    pi = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)

    cf = continuedFraction(M)
    m = max(m, cf[1])
    print(m)
    getcontext().prec = 50
    for d in range(m , M + 1):
        n = math.ceil(d * math.pi - 1/2)
        if abs(Decimal(n)/Decimal(d) - pi) < abs(Decimal(frac[0])/Decimal(frac[1]) - pi):
            frac = [n, d]
    return frac

if __name__ == "__main__":
    m, M = map(int, input().split(" "))
    [n, d] = continuedFraction(M)
    print (str(n) +"/"+ str(d))
    # frac = closestFraction(m, M)
    # print(frac)
    #print(str(frac[0]) + "/" + str(frac[1]))
