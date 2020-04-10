def diamond(n):
    s = ''
    if n <= 0 or n % 2 == 0:
        return None
    if n == 1:
        return "*\n"
    for x in range(1, n // 2 + 2):
        s += " " * (n // 2 + 1 - x)
        s += '*' * (2 * x - 1)
        s += "\n"
    for x in range(n // 2 + 2, n + 1):
        s += " " * (x - n // 2 - 1)
        s += '*' * (2 * n - 2 * x + 1)
        s += "\n"
    return s
