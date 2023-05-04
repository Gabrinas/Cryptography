import math as m
n = 15244346903
e = 751
d = 8545627279
c = [971896385, 3249912096, 4079022731, 8771096382, 10148198704]

def gen_plaintx(cipher):
    q = 0
    ls = []
    lt = len(cipher)
    while q < lt:
        val = cipher[q]
        vn = pow(val, d, n) # note that phile n is actually needed not n
        ls.append(vn)
        q += 1
    return ls

print(gen_plaintx(c))
