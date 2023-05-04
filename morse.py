
def morse_cd(txt):
    q = 0
    lt = len(txt)
    ls = []
    while lt:
        val = txt[: ]
        if val[: 1] == '0':
            ls.append('A')
            txt = txt[1: ]
        elif val[: 2] == '10':
            ls.append('B')
            txt = txt[2: ]
        elif val[: 2] == '11':
            ls.append('C')
            txt = txt[2: ]
        lt = len(txt)
    res = ''.join(ls)
    return res

print(morse_cd('010001101011'))
