# Program: Python codes to find the 16 rounds of Data Encryption Standard (DES)
# Date: 18 / 04 / 2023
# Author: Sobola Gabriel
# Time: 15:01 (GMT)
# Institution: Covenant University, Ota

# Here succeeding key was generated from the already shifted preceding key
# '0123456789ABCDEF'
txtn = input()

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def hex_bin(txt):
    q = 0
    lt = len(txt)
    ls = []
    while q < lt:
        val = txt[q]
        vl = chars.index(val)
        bn = bin(vl)[2: ].zfill(4)
        ls.append(bn)
        q += 1
    res = ''.join(ls)
    
    # PC1 Permutation Choice of keys
    pc1_key1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
    pc1_key2 = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    ln = len(pc1_key1)
    r = 0
    l_key1 = []; l_key2 = []
    while r < ln:
        vn1 = pc1_key1[r]
        vn2 = pc1_key2[r]
        rs1 = res[vn1 - 1]
        rs2 = res[vn2 - 1]
        l_key1.append(rs1)
        l_key2.append(rs2)
        r += 1
    #print(l_key1, l_key2)

    # Shift key to generate keys for the 16 iterations
    keysk = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    # PC2 Permutation Choice for each round to get 48 bits
    pc2_key = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 36, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    lr = len(pc2_key)
    n = 0
    lg = len(keysk)
    l_pc2_key = []
    l_pc1_key1 = [l_key1]
    l_pc2_key2 = [l_key2]
    #return l_pc1_key1
    hexv_keys = []
    while n < lg:
        idm = keysk[n]
        shf_key1 = l_pc1_key1[n][idm: ]
        shf_key1 = shf_key1 + l_pc1_key1[n][: idm]
        shf_key2 = l_pc2_key2[n][idm: ]
        shf_key2 = shf_key2 + l_pc2_key2[n][: idm]
        key_total = shf_key1 + shf_key2
        l_pc1_key1.append(shf_key1)
        l_pc2_key2.append(shf_key2)
        #return l_pc2_key2
        lsr = []
        lr = len(pc2_key)
        q = 0
        while q < lr:
            vb = pc2_key[q]
            vbn = key_total[vb - 1]
            lsr.append(vbn)   # Each round key needed
            q += 1
        l_pc2_key.append(lsr)
        hexv_keys.append(''.join(lsr))
        n += 1
    #print(l_pc2_key)

    # Just give me the hex value of the key for each round
    qq = len(hexv_keys)
    ql = []
    qw = 0
    while qw < qq:
        qn = hexv_keys[qw]
        qv = ''.join([chars[int(qn[i: i + 4], 2)] for i in range(0, len(qn), 4)])
        ql.append(qv)
        qw += 1
    print('key for each round:   ')
    print(ql)
    #print(l_pc2_key)
    
        
    
    # Plaintext
    pt = res
    #print(len(pt))
    lt = 32
    
    # Initial Permutation
    ini_p = [58, 50, 42, 34, 26, 18, 10, 2,
             60, 52, 44, 36, 28, 20, 12, 4,
             62, 54, 46, 38, 30, 22, 14, 6,
             64, 56, 48, 40, 32, 24, 16, 8,
             57, 49, 41, 33, 25, 17, 9, 1,
             59, 51, 43, 35, 27, 19, 11, 3,
             61, 53, 45, 37, 29, 21, 13, 5,
             63, 55, 47, 39, 31, 23, 15, 7]
    d = 0
    ini_p_res = []
    lg = len(ini_p)
    while d < lg:
        vf = ini_p[d]
        chR = pt[vf - 1]
        ini_p_res.append(chR)
        d+= 1
    
    L0 = ini_p_res[: lt]
    R0 = ini_p_res[lt: ]

    
    l_pc2_key = l_pc2_key   # keys for the 16 round
    Lft = [L0]
    Rgt = [R0]
    n = 0
    ltp = len(l_pc2_key)
    
    while n < ltp:
        vk = l_pc2_key[n]
        Lt = Lft[n]
        Rt = Rgt[n]
      
        # Expansion Permutation of plaintext
        exp_per = [32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]

        f = 0
        exp_res = []
        lt = len(exp_per)
        while f < lt:
            vf = exp_per[f]
            chR = Rt[vf - 1]
            exp_res.append(chR)
            f+= 1

         # exp_res (R0 being expanded) XOR key 
        zp = list(zip(exp_res, vk))

        x = 0
        lf = len(zp)
        lsr = []
        while x < lf:
            vd = zp[x]
            if vd[0] == '0' and vd[1] == '0':
                lsr.append('0')
            elif vd[0] == '1' and vd[1] == '1':
                lsr.append('0')
            elif vd[0] == '0' and vd[1] == '1':
                lsr.append('1')
            elif vd[0] == '1' and vd[1] == '0':
                lsr.append('1')
            x += 1
       # print(lsr)  # len(lsr)

        # S-Box substitution
        # Group lsr into 8 groups of 6 bits per group
        lsd = [lsr[i: i + 6] for i in range(0,len(lsr), 6)]

        S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

        S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

        S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

        S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

        S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

        S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

        S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    
        S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]


        lk = len(lsd)
        r = 0
        s_box_out = []
        while r < lk:
            v = lsd[r]
            R = int((v[0] + v[-1]), 2)
            C = int((''.join(v[1: -1])), 2)
            if r == 0:
                nb = S1[R][C]
                s_box_out.append(nb)
            elif r == 1:
                nb = S2[R][C]
                s_box_out.append(nb)
            elif r == 2:
                nb = S3[R][C]
                s_box_out.append(nb)
            elif r == 3:
                nb = S4[R][C]
                s_box_out.append(nb)
            elif r == 4:
                nb = S5[R][C]
                s_box_out.append(nb)
            elif r == 5:
                nb = S6[R][C]
                s_box_out.append(nb)
            elif r == 6:
                nb = S7[R][C]
                s_box_out.append(nb)
            elif r == 7:
                nb = S8[R][C]
                s_box_out.append(nb)
            r += 1
        bnn = [bin(i)[2: ].zfill(4) for i in s_box_out]  # The 32 bits results after S-Box      
        bnN = ''.join(bnn)
        #print(bnN)
        
        # Applying permutation to get P(B)

        pnew = [16, 7, 20, 21, 29, 12, 28, 17,
                1, 15, 23, 26, 5, 18, 31, 10,
                2, 8, 24, 14, 32, 27, 3, 9,
                19, 13, 30, 6, 22, 11, 4, 25]
        f = 0
        lh = len(pnew)
        pb_val = []
        while f < lh:
            va = pnew[f]
            rd = bnN[va - 1]
            pb_val.append(rd)
            f += 1
        pb_vaL = [''.join(pb_val[i: i + 4]) for i in range(0, len(pb_val), 4)]

        # R1 = P(B) NOR LO

        L0n = ''.join(L0)
        zp2 = list(zip(''.join(pb_val), L0n))

        x = 0
        lf = len(zp2)
        R1 = []
        while x < lf:
            vd = zp2[x]
            if vd[0] == '0' and vd[1] == '0':
                R1.append('0')
            elif vd[0] == '1' and vd[1] == '1':
                R1.append('0')
            elif vd[0] == '0' and vd[1] == '1':
                R1.append('1')
            elif vd[0] == '1' and vd[1] == '0':
                R1.append('1')
            x += 1
        R1_gr = [''.join(R1[i: i + 4]) for i in range(0, len(R1), 4)]
        R1_gr = ''.join(R1_gr)
        R1_gr = [i for i in R1_gr]
        Ln = Rgt[-1]
        Lft.append(Ln)
        Rgt.append(R1_gr)
        n += 1
   
    # Generate round 1 result for me
    R1 = Rgt[1]
    L1 = Lft[1]
    Ciph = L1 + R1
    cipher_text_1 = [int(''.join(Ciph[i: i + 4]), 2) for i in range(0, len(Ciph), 4)]
    print('Generate first round result (cipher_text_1):    ')
    cipher_text_1 = ''.join([chars[i] for i in cipher_text_1])
    print(cipher_text_1)

    # Generate round 1 result for me
    R1 = Rgt[-1]
    L1 = Lft[-1]
    Ciphf = L1 + R1
    cipher_text_final = [int(''.join(Ciphf[i: i + 4]), 2) for i in range(0, len(Ciphf), 4)]
    print('Generate final encrypted message after the 16th round (cipher_text_final):    ')
    cipher_text_final = ''.join([chars[i] for i in cipher_text_final])
    return cipher_text_final 
   
print(hex_bin(txtn))









