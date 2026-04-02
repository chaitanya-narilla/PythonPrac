def nu(n):
    if n == 0:
        return 0
    nu(n-1)
    print(n, end =" ")

test = nu(5)
