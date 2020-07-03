
def calculate(total, num, newnum):
    newsum = num + newnum
    if newsum < 4000000:
        if newsum % 2 == 0:
            total += newsum
            print(total)
        return calculate(total, newnum, newsum)
    else:
        return total


print(calculate(2, 1, 2))
