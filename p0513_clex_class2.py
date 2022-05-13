result = 0
result2 = 0

def add(num) :
    global result
    result += num
    return result

def add2(num) :
    global result2
    result2 += num
    return result2


print(add(2))
print(add(3))
print(add(4))
print(add2(4))
print(add2(6))
print(add(5))
print(add2(8))






