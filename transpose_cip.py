def transp_cip(txt):
    txt = txt.replace(' ', '')
    q = 0
    ls = []
    lt = len(txt) // 5
    while q < lt:
        val = txt
        ln = [txt[i] for i in range(q, len(val), 4)]
        ls.append(ln)
        q += 1
    res = [ls[i: i + 2] for i in range(0, len(ls), 2)]
    res = [i[0] + i[1] for i in res]
    if len(res[0]) > len(res[1]):
        ren = list(zip(res[0], res[1]))
        rF = ''.join([''.join(i) for i in ren]) + res[0][-1]
        return rF
    else:
        ren = list(zip(res[0], res[1]))
        rF = ''.join([''.join(i) for i in ren]) + res[1][-1]
        return rF

print(transp_cip('meet me after the toga party'))
