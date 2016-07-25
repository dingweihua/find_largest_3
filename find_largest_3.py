def find_largest_3(l):
    if len(l) < 3:
        return
    largest_3 = sort_3(l[:3])
    if len(l) == 3:
        return largest_3
    for v in l[3:]:
        if v > largest_3[0]:
            largest_3 = [v, largest_3[0], largest_3[1]]
        elif v > largest_3[1] and v <= largest_3[0]:
            largest_3 = [largest_3[0], v, largest_3[1]]
        elif v > largest_3[2] and v <= largest_3[1]:
            largest_3 = [largest_3[0], largest_3[1], v]
    return largest_3

def sort_3(l):
    if len(l) != 3:
        return l
    if (l[0] < l[1]):
        l[0], l[1] = l[1], l[0]
    if (l[1] < l[2]):
        l[1], l[2] = l[2], l[1]
    if (l[0] < l[1]):
        l[0], l[1] = l[1], l[0]
    return l

L1 = [4, 1, 3, 5, 7, 2, 3, 4, 6]
print find_largest_3(L1)
