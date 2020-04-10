def last_digit(lst):
    if lst==[]:
        return 1
    if lst[0]==1:
        return 1
    if len(lst)==1:
        return lst[0]%10
    while len(lst)>1:
        last=lst[len(lst)-1]
        previous=lst[len(lst)-2]
        lst.pop(len(lst)-1)
        lst.pop(len(lst)-1)
        if last==0:
            lst.append(1)
        elif previous==0:
            lst.append(0)
        elif previous==1:
            lst.append(1)
        elif len(lst)>=1:
            x=pow(previous, last, 4 )
            lst.append(x+4)
        else:
            x=pow(previous, last, 10 )
            lst.append(x)
    return lst[0]