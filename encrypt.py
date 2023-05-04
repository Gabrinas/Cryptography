print(ord('\x86'), ord('Z'))
from math import gcd

def gen_e(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = []
    q =  2
    while q < n:
        val = q
        chk = gcd(val, z)
        if chk == 1:
            e.append(val)
        q += 1
    e =  e[0]
    return e
#print(gen_e(7, 13))
print(gen_e(5, 11))


def gen_d(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    d =  []
    a =  1
    while a < n:
        e = gen_e(p, q)
        vl = ((a * e) - 1)
        chk2 = str(vl / z)
        chk2 = chk2.split('.')
        if chk2[-1] == '0' and a != e:
            d.append(a)
        a += 1    
    d = d[0]
    return d
#print(gen_d(7, 13))
print(gen_d(5, 11))


def encryptme(txt, p, q):
    print('The plain text is: ' + txt)
    txt = txt.lower()
    n = p * q
    z = (p - 1) * (q - 1)
    txtn = txt.split(' ')
    ls = []; ls2 = []
    r = 0
    lt = len(txtn)
    while r < lt:
        ft = txtn[r]
        m = 0
        ltn = len(ft)
        lsc = []; lsc2 = []; 
        while m < ltn:
            ftn = ft[m]
            vn = ord(ftn)
            if ftn.islower():
                res = vn - 96
            else:
                res = vn - 64
            C = (res ** gen_e(p, q)) % n
            resn = chr(C)
            lsc.append(resn)
            lsc2.append(C)
            m += 1
        ls.append(''.join(lsc))
        ls2.append(lsc2)
        r += 1
    rF = ls[0].title() + ' ' + ' '.join(ls[1: ])
    #rF = ' '.join(ls)
    print('The cipher text is: ' + rF)
    return rF, ls2

#print(encryptme('love is sweet', 7, 13))
#print(encryptme('love is sweet', 5, 7))
#print(encryptme('This a fundamental course for all students', 5, 7))
print(encryptme('Covenant University is a good institution', 5, 7))



def decryptme(txt, p, q):
    print('The cipher text is: ' + txt)
    n = p * q
    z = (p - 1) * (q - 1)
    txtn = txt.split(' ')
    lsn = []; lsn2 = []
    g = 0
    lt1 = len(txtn)
    while g < lt1:
        ft = txtn[g]
        m = 0
        ltn = len(ft)
        lscn = []; lscn2 = []
        while m < ltn:
            ftn = ft[m]
            vn = ord(ftn)
            M = (vn ** gen_d(p, q)) % n
            res = chr(M + 96)
            lscn.append(res)
            m += 1
        lsn.append(''.join(lscn))
        g += 1
    rFn = lsn[0].title() + ' ' + ' '.join(lsn[1: ])
    #rFn = ' '.join(lsn)
    print('The original plaintext is: ' + rFn) 
    #return rFn
            
#print(decryptme('&G\x1d\x1f QP P\x04\x1f\x1fL', 7, 13))
#print(decryptme('\x11\x0f\x16\n \x04\x18 \x18\x12\n\n\x14', 5, 7))
#print(decryptme('\x14\x08\x04\x18 \x01 \x06\x15\x0e\t\x01\r\n\x0e\x14\x01\x11 !\x0f\x15\x17\x18\n \x06\x0f\x17 \x01\x11\x11 \x18\x14\x15\t\n\x0e\x14\x18', 5, 7))
print(decryptme('!\x0f\x16\n\x0e\x01\x0e\x14 \x15\x0e\x04\x16\n\x17\x18\x04\x14\x1e \x04\x18 \x01 \x07\x0f\x0f\t \x04\x0e\x18\x14\x04\x14\x15\x14\x04\x0f\x0e', 5, 7))










