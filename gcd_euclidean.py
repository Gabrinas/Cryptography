# 31 / 03 / 2023
# Python implementation for finding the greatest common denominator using Euclid   g = gcd(a, b)
import math as m
# Using Euclidean Algorithm a = qb + r
def gcdm(a, b):
    ls = [[a, b]]
    qt = [] # collect the quotients
    #d = []
    q = 1
    while q:
        v1 = ls[-1][0]
        v2 = ls[-1][1]
        val = v1 // v2
        qt.append(val)
        rst = v1 - (v2 * val)
        #d1 = m.gcd(v2, rst)
        #d.append(d1)  to check for gcd
        ls.append([v2, rst])
        if rst == 0:
            return ls, q, qt
        q += 1

#print(gcdm(1160718174, 316258250))
print(gcdm(1759, 550))


# Using Euclidean Algorithm g gcd(a, b) = gcd(b, a mod b)
def gcdm(a, b):
    ls = []
    while b != 0:
        p = a; q = b
        res = p % q
        ls.append([b, res])
        a = b; b = res
    return a, ls

print(gcdm(1160718174, 316258250))


# Using Euclidean Algorithm g gcd(a, b) = gcd(b, a mod b) with recursion
def gcdm(a, b):
    res = 0
    if b == 0:
        return a
    else:
        res = gcdm(b, a % b)
        return res
print(gcdm(1160718174, 316258250))


def gcdm(a, b):
    res = 0
    if b == 0:
        return a
    else:
        res = gcdm(b, a % b)
        return res
print(gcdm(42, 30))


# Equation of the form: ax mod n = 1 and gcd(a, n) = 1
def inv_mod(a, n):
    fn = [i for i in range(1, n) if m.gcd(i, n) == 1]
    fn1 = len(fn)
    fnn = fn1 - 1
    x = (a ** fnn) % n
    return x


print(inv_mod(17, 100))


# Using extended Euclidean Algorithm: g = ax1 + by1
def extend_eclud(a, b):
    x = [[1, 0]]
    y = [[0, 1]]
    r = [[a, b]]
    q = [0, 0]
    m = 1
    rn = 1
    while rn != 0:
        r1 = r[-1][0]; x1 = x[-1][0]; y1 = y[-1][0]
        r2 = r[-1][1]; x2 = x[-1][1]; y2 = y[-1][1]
        rn = r1 % r2
        qn = r1 // r2
        xn = x1 - (qn * x2)
        yn = y1 - (qn * y2)
        r.append([r2, rn])
        q.append(qn)
        x.append([x2, xn])
        y.append([y2, yn])
        m += 1
    ltn = len(r)
    i = [i for i in range(-1, ltn)] + ['']
    rnn = [i[0] for i in r] + [rn]
    q = q + [qn]
    xnn = [i[0] for i in x] + ['']
    ynn = [i[0] for i in y] + ['']
    zp = list(zip(i, rnn, q, xnn, ynn))
    rF = (a * xnn[-2]) + (b * ynn[-2]) 
    return zp, rF


print(extend_eclud(30, 35))



















    












