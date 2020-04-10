def infected(s):
    array = s.split("X")
    infected_number = 0
    total = 0
    for continent in array:
        if "1" in continent:
            infected_number += len(continent)
        total += len(continent)
    if total == 0:
        return 0
    return 100 * infected_number / total
