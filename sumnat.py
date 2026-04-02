def sumnat(num):
    if num == 0:
        return 0
    return num + sumnat(num-1)

test = sumnat(3)
print(test)