
def calculate():
    nums = []
    for i in range(0, 1000):
        if i % 3 == 0:
            nums.append(i)
        elif i % 5 == 0:
            nums.append(i)

    return sum(nums) 

print(calculate())
