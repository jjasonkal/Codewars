def ips_between(start, end):
    st = start.split(".")
    s = 0
    for x in range(len(st)):
        s += int(st[x]) * 256 ** (len(st) - x - 1)
    en = end.split(".")
    e = 0
    for y in range(len(en)):
        e += int(en[y]) * 256 ** (len(en) - y - 1)
    return e - s
