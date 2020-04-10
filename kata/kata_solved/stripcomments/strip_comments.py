def solution(string, markers):
    s = ''
    deleted = False
    for x in string:
        if x == "\n":
            deleted = False
            s += x
        elif x not in markers and deleted == False:
            s += x
        elif x in markers:
            deleted = True
    st = ''
    for x in range(len(s) - 1):
        if s[x + 1] == '\n' and s[x] == " ":
            None
        else:
            st += s[x]
    if len(s) >= 1:
        if s[len(s) - 1] != " ":
            st += s[len(s) - 1]
    return st
