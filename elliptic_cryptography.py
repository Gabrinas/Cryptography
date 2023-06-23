from math import gcd
def no_prime_to(n):
    ls = [i for i in range(1, n) if gcd(i, n) == 1]
    res = len(ls)
    return res
print(no_prime_to(23))

# Elliptic curve for finding k; discrete logarithm
def elliptic_crypt1(P, Q, a, mod_val):
    ls = [P, P]
    q = 1
    while q:
        v1 = ls[0]
        v2 = ls[-1]
        xp = v1[0]; yp = v1[1]
        xq = v2[0]; yq = v2[1]
        if v1 == v2:
            nm = ((3 * (xp ** 2)) + a)
            dn = 2 * yp
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        elif v1 != v2:
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        if ls[-1] == Q:
            res = q + 1
            return res
        q += 1

print(elliptic_crypt1([16, 5], [4, 5], 9, 23))


# For finding G
print('To find the point of G:    ')
def elliptic_crypt1(P, Q, a, mod_val):
    ls = [P, P]
    q = 0
    while q < 244:
        v1 = ls[0]
        v2 = ls[-1]
        xp = v1[0]; yp = v1[1]
        xq = v2[0]; yq = v2[1]
        if v1 == v2:
            nm = ((3 * (xp ** 2)) + a)
            dn = 2 * yp
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        elif v1 != v2:
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        
        
        if ls[-1][0] == Q[0]:
            res = q + 1
            return res
        
        q += 1
   # return ls, len(ls)

print(elliptic_crypt1([2, 2], [2, -2], 0, 211))


# For finding public keys

print('give me:  pA')
def elliptic_crypt2(P, Q, a, mod_val, G, nA):  # This G is supposed to be found
    ls = [P, P]
    q = 1
    while q < G:
        v1 = ls[0]
        v2 = ls[-1]
        xp = v1[0]; yp = v1[1]
        xq = v2[0]; yq = v2[1]
        if v1 == v2:
            nm = ((3 * (xp ** 2)) + a)
            dn = 2 * yp
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        elif v1 != v2:
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        if q == nA - 1:
            return ls[-1]
        q += 1

print(elliptic_crypt2([2, 2], [0, 0], 0, 211, 240, 121))


print('give me:  pB')
def elliptic_crypt3(P, Q, a, mod_val, G, nB):  # This G is supposed to be found
    ls = [P, P]
    q = 1
    while q < G:
        v1 = ls[0]
        v2 = ls[-1]
        xp = v1[0]; yp = v1[1]
        xq = v2[0]; yq = v2[1]
        if v1 == v2:
            nm = ((3 * (xp ** 2)) + a)
            dn = 2 * yp
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        elif v1 != v2:
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        if q == nB - 1:
            return ls[-1]
        q += 1

print(elliptic_crypt3([2, 2], [0, 0], 0, 211, 240, 203))


 # getting the secret key from nA and pB
print('give me:  secret_key from nA and pB (pB = nB * G)')
def elliptic_crypt4(P, Q, a, mod_val, G, nA):  # This G is supposed to be found
    ls = [P, P]
    q = 0
    while q < G:
        #cll_me = elliptic_crypt3([2, 2], [0, 0], 0, 211, 240, 203)
        v1 = ls[0]
        v2 = ls[-1]
        xp = v1[0]; yp = v1[1]
        xq = v2[0]; yq = v2[1]
        if v1 == v2:
            nm = ((3 * (xp ** 2)) + a)
            dn = 2 * yp
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        elif v1 != v2:
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        if q == nA:
            return ls[1: ][-3]
        q += 1
cll_me = elliptic_crypt3([2, 2], [0, 0], 0, 211, 240, 203) # getting the secret key from nA and pB
#print(cll_me)
print(elliptic_crypt4(cll_me, [0, 0], 0, 211, 240, 121))



 # getting the secret key from nB and pA
print('give me:  secret_key from nB and pA (pA = nA * G)')
def elliptic_crypt5(P, Q, a, mod_val, G, nB):  # This G is supposed to be found
    ls = [P, P]
    q = 0
    while q < G:
        #cll_me = elliptic_crypt3([2, 2], [0, 0], 0, 211, 240, 203)
        v1 = ls[0]
        v2 = ls[-1]
        xp = v1[0]; yp = v1[1]
        xq = v2[0]; yq = v2[1]
        if v1 == v2:
            nm = ((3 * (xp ** 2)) + a)
            dn = 2 * yp
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        elif v1 != v2:
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            ls.append([xR, yR])
        if q == nB:
            return ls[1: ][-3]
        q += 1
cll_me = elliptic_crypt2([2, 2], [0, 0], 0, 211, 240, 121) # getting the secret key from nB and pA
print(cll_me)
print(elliptic_crypt5(cll_me, [0, 0], 0, 211, 240, 203))





