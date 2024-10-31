def isprime(num):
    if num <=1:
        return False
    
    for i in range(2, num):
        if num %i ==0:
            return False
    
    return True

print(isprime(23))
    
# int(num ** 0.5) + 1 ,, it is  a schema to check prime number in  a better way use this insteadd of num in for loop

# count total prime 
def totalprime(limit):
    nums = []
    for num in range(2,limit+1):
        if isprime(num):
            nums.append(num)
    return nums

print(totalprime(23))
