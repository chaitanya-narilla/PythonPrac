def pali(n):
    a = str(n)

    if a == a[::-1]:
        return True 
    else:
        return False

print(pali(1234))