def sum_otr(otr):
    if len(otr) == 0:
        return 0
    count = 0
    if otr[0] < 0:
        count += 1
    return count + sum_otr(otr[1:])


lst = [-3, 5, 7, 9, -1, 2, -111]
print('n =', sum_otr(lst))
