
# Generate keys for DES

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def gen_keys(txtn):
    qy = 0
    lty = len(txtn)
    lsy = []
    while qy < lty:
        valy = txtn[qy]
        vly = chars.index(valy)
        bny = bin(vly)[2: ].zfill(4)
        lsy.append(bny)
        qy += 1
    resy = ''.join(lsy)

    # PC1 Permutation Choice of keys
    pc1_key1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
    pc1_key2 = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    ln = len(pc1_key1)
    r = 0
    l_key1 = []; l_key2 = []
    while r < ln:
        vn1 = pc1_key1[r]
        vn2 = pc1_key2[r]
        rs1 = resy[vn1 - 1]
        rs2 = resy[vn2 - 1]
        l_key1.append(rs1)
        l_key2.append(rs2)
        r += 1
    k1 = ''.join(l_key1)
    k2 = ''.join(l_key2)
    #return k1, k2

    # Shift the keys with respect to the table to generate the 16 rounds keys
    keysk = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    q = 0
    lt = len(keysk)
    lsc1 = [k1]
    lsc2 = [k2]
    tl = []
    while q < lt:
        vk = keysk[q]
        rs1 = lsc1[-1][vk: ] + lsc1[-1][: vk]
        rs2 = lsc2[-1][vk: ] + lsc2[-1][: vk]
        tttl = rs1 + rs2
        lsc1.append(rs1)
        lsc2.append(rs2)
        tl.append(tttl)
        q += 1

    # PC2 Permutation Choice for each round to get 48 bits per round
    pc2_key = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 36, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    lr = len(tl)
    nn = 0
    #l_pc2_key = []
    hexv_keys = []
    while nn < lr:
        vb = tl[nn]
        lc = []
        lf = len(pc2_key)
        e = 0
        while e < lf:
            vf = pc2_key[e]
            res = vb[vf - 1]
            lc.append(res)
            e += 1
        lc = [int(''.join(lc[i: i + 4]), 2) for i in range(0, len(lc), 4)]
        lcc = ''.join([chars[i] for i in lc])
        hexv_keys.append(lcc)
        nn += 1
    return hexv_keys


    
print(gen_keys('0F1571C947D9E859'))
#print(gen_keys('0123456789ABCDEF'))












