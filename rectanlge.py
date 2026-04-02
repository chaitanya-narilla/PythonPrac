def printrec(n,m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("*", end=" ")
        print()

test = printrec(3,5)
print(test)