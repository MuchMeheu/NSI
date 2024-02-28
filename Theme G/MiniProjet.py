def eratosthene(n):
    crible = [True] * (n + 1)
    crible[0] = False
    if n > 0:
        crible[1] = False
    for p in range(2, int(n**0.5) + 1):
        if crible[p] == True:
            # p est premier
            for kp in range(2*p, n + 1, p):
                crible[kp] = False
    return crible

def premiers_jusque(n):
    crible = eratosthene(n)
    premiers = [i for i in range(len(crible)) if crible[i]]
    return premiers


# tests

assert eratosthene(5) == [False, False, True, True, False, True]
assert eratosthene(6) == [False, False, True, True, False, True, False]
assert premiers_jusque(5) == [2, 3, 5]
assert premiers_jusque(6) == [2, 3, 5]
assert premiers_jusque(20) == [2, 3, 5, 7, 11, 13, 17, 19]