n = 12347984
def getsum(n):
    sum = 0
    for digit in str(n):
        sum +=int(digit)
    return sum

print(getsum(n))    
    