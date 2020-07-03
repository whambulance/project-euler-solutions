
def compute():
    for i in range(600851475143//2, 0, -1):
        if 600851475143 % i == 0:
            return i


print(compute())
