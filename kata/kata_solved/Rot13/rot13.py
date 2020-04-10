def rot13(message):
    az = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for x in message:
        if x.lower() in az:
            if x.islower():
                s += az[(az.index(x) + 13) % 26]
            else:
                s += az[(az.index(x.lower()) + 13) % 26].upper()
        else:
            s += x
    return s
