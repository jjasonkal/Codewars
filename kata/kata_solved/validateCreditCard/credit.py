def validate(n):
    a = [int(x) for x in str(n)]
    if len(a) % 2 == 1:
        for x in range(len(a)):
            if x % 2 == 1:
                a[x] = 2 * a[x]
                while a[x] > 9:
                    a[x] -= 9
    else:
        for x in range(len(a)):
            if x % 2 == 0:
                a[x] = 2 * a[x]
                while a[x] > 9:
                    a[x] -= 9
    if sum(a) % 10 == 0:
        return True
    return False
