from math import gcd
def no_prime_to(n):
    ls = [i for i in range(1, n) if gcd(i, n) == 1]
    res = len(ls)
    return res
print(no_prime_to(23))


print('Computing G upto certain value')
def elliptic_crypt2(P, Q, a, mod_val, limit):  # This G is supposed to be found
    ls = [P, P]
    q = 1
    while q < limit:
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
        q += 1
    return ls

print(elliptic_crypt2([7, 2], [7, 2], 1, 11, 3))


