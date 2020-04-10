def courier(arr, n):
    delivery = [[], [], [], []]
    minutes = 2 * len(arr)
    done = 0
    count = 0
    for x in arr:
        if x[0] == "w":
            delivery[0].append(int(x[1:]))
        elif x[0] == "e":
            delivery[1].append(int(x[1:]))
        elif x[0] == "n":
            delivery[2].append(int(x[1:]))
        elif x[0] == "s":
            delivery[3].append(int(x[1:]))
    for x in delivery:
        x.sort(reverse=True)
    for x in range(len(delivery)):
        for y in range(0, len(delivery[x]) // n):
            minutes += 2 * max(delivery[x])
            minutes += 2
            delivery[x] = delivery[x][n:]

    while delivery != [[], [], [], []]:
        for y in range(len(delivery)):
            mlen = max(len(l) for l in delivery)
            plus = n - mlen
            if delivery[y] != [] and len(delivery[y]) == mlen:
                minutes += 2 * max(delivery[y])
                minutes += 2
                delivery[y] = []
                while plus != 0:
                    for j in range(plus, 0, -1):
                        for z in range(len(delivery)):
                            if delivery[z] != [] and len(delivery[z]) == j and j <= plus:
                                minutes += 2 * max(delivery[z])
                                delivery[z] = []
                                plus -= j
                            if plus == 0:
                                break
                    plus = 0
    return minutes