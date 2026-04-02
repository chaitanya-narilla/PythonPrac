def close(num,m):
    a = []
    for i in range(num):
        if i % m == 0 : 
            a.append(i)
    return a[-1]

test = close(13,4)
print(test)
