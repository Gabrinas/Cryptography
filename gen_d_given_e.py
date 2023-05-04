import math as m
e_val = int(input("Enter the value of e:  "))
def gen_d_given_e(p, q):
    n = p * q
    ls = [i for i in range(1, n + 1) if m.gcd(n, i) == 1]
    phil = len(ls)
    print(phil)
    lc = []
    t = 1
    while t:
        val = ((e_val * t) - 1)/phil
        chk = str(val).split(".")[-1]
        if chk == '0':
            return t
        t += 1


print(gen_d_given_e(59, 83))
