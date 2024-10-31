def fibo(num):
    nums = []
    a = 0;
    b = 1;
    for i in range(num):
        nums.append(a)
        a, b = b, a+b
    return nums

print(fibo(10))