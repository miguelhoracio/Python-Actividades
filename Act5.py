def contar_letras(s):
    h = list(s.lower().replace(" ", ""))
    c = set(h)
    tot = []
    for i in c:
        k = 0
        for j in range(0,len(h)):
            if i == h[j]:
                k += 1
        tot.append(k)
    dic = dict(zip(c, tot))
    return dic.__str__()