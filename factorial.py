#Input: n = 153
#Output: true
#Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

def arms(n):
    m=len(str(n))
    sum = 0
    for i in str(n):
        sum = pow(int(i),m) + sum 
    
    if sum == n:
        return True 
    else:
        return False
    
print(arms(123))