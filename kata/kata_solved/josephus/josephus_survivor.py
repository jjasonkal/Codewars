def josephus_survivor(n, k):
    a = []
    i = 1
    while i <= n:
        a.append(i)
        i += 1
    j = k - 1
    while len(a) > 1:
        if j < len(a):
            out = j % len(a)
            a.pop(out)
        else:
            out = (j - len(a)) % len(a)
            j = out
            a.pop(out)
        j += k - 1

    return (a[0])