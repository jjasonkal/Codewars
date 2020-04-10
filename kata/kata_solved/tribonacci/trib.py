def tribonacci(signature, n):
    i = signature[0]
    j = signature[1]
    k = signature[2]
    l = 0
    a = [i, j, k]
    if n == 0:
        return []
    if n == 1:
        return [i]
    if n == 2:
        return [i, j]
    if n == 2:
        return [i, j, k]
    while l < n - 3:
        new = i + j + k
        a.append(new)
        i = j
        j = k
        k = new
        l += 1
    return a
