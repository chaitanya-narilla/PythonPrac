def triangle(num):
    for i in range(num+1):
        for j in range(0,i):
            print("*", end=" ")
        print()
test = triangle(3)
