def sum_of_intervals(intervals):
    array = []
    for i in range(0, len(intervals)):
        for j in range(0, 2):
            array.append(intervals[i][j])
    num = []
    for i in range(0, len(array) // 2):
        for k in range(array[2 * i], array[2 * i + 1]):
            if k not in num:
                num.append(k)
    return (len(num))
