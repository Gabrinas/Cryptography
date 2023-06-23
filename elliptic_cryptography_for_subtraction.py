from math import gcd
def no_prime_to(n):
    ls = [i for i in range(1, n) if gcd(i, n) == 1]
    res = len(ls)
    return res
print(no_prime_to(23))


# Elliptic curve for subtraction
# This is a short method which involves changing subtraction to addition
# For instance: [246, 174] - [68, 84] Eq(a, b) = E257(0, 6)
# The second term of the right hand side becomes: -84 % 257 = 173
# finally find: [246, 174] + [68, 173]
def elliptic_crypt1(P, Q, a, mod_val):
    v1 = P
    vt = -Q[-1] % mod_val
    v2 = [Q[0], vt]
    xp = v1[0]; yp = v1[1]
    xq = v2[0]; yq = v2[1]
    ls = []
    if v1 == v2:
        nm = ((3 * (xp ** 2)) + a)
        dn = 2 * yp
        phile = no_prime_to(mod_val) - 1
        euler_tran = (dn ** phile) % mod_val
        wav = (nm * euler_tran) % mod_val
        xR = ((wav ** 2) - xp - xq) % mod_val
        yR = ((wav * (xp - xR)) - yp) % mod_val
        ls.append([xR, yR])
        return ls
    elif v1 != v2:
        nm = (yq - yp); dn = (xq - xp)
        phile = no_prime_to(mod_val) - 1
        euler_tran = (dn ** phile) % mod_val
        wav = (nm * euler_tran) % mod_val
        xR = ((wav ** 2) - xp - xq) % mod_val
        yR = ((wav * (xp - xR)) - yp) % mod_val
        ls.append([xR, yR])
        return ls
        
print(elliptic_crypt1([10, 2], [3, 5], 1, 11))


# Or
 
# Elliptic curve for subtraction
# This is a brute force approach as it tests all the possible combinations
# within (mod_val - 1) * (mod_val - 1)
def elliptic_crypt1(R, Q, a, mod_val):
    
    q = 0
    ls = []
    while q < mod_val:
        vlx = q
        vly = [i for i in range(mod_val)]
        #print(vly)
        m = 0
        lsc = []
        lt = len(vly)
        while m < lt:
            xp = vlx; yp = vly[m]
            xq = Q[0]; yq = Q[1]
            nm = (yq - yp); dn = (xq - xp)
            phile = no_prime_to(mod_val) - 1
            euler_tran = (dn ** phile) % mod_val
            wav = (nm * euler_tran) % mod_val
            xR = ((wav ** 2) - xp - xq) % mod_val
            yR = ((wav * (xp - xR)) - yp) % mod_val
            if [xR, yR] == R and xp != xq:
                lsc.append([xp, yp])
            m += 1
        ls.extend(lsc)
        q += 1
    return ls
            
print(elliptic_crypt1([10, 2], [3, 5], 1, 11))

#print(elliptic_crypt1([246, 174], [68, 84], 0, 257))















