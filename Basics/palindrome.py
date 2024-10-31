# 121 example

def ispalin(num):
    a = int(str(num)[::-1])
    if a==num:
        return True
    return False

print(ispalin(2112))