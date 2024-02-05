def ajoute_dictionnaire(d1, d2):
    d = {}
    for cles in d1:
        d[cles] = d1[cles]
    for cles in d2:
        if cles in d:
            d[cles] += d2[cles]
        else:
            d[cles] = d2[cles]
    return d

print(ajoute_dictionnaire({1:5,2:7},{2:9,3:11}))

