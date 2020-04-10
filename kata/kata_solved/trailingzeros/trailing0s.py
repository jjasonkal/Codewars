def zeros(n):
    y=0
    for i in range(1,100):
        y+=n//(5**i)
    return(y)
