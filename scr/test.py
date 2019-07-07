#!/usr/bin/python3


# 一个简单的测试
def findMinAndMax(L):
    if 0 == len(L):
        return None, None
    if 1 == len(L):
        return L[0], L[0]
    # 定义初始值
    minNum = 2 ** 63 - 1
    maxNum = -minNum - 1
    for x in L:
        if x > maxNum:
            maxNum = x
        if x < minNum:
            minNum = x
    return minNum, maxNum


print(findMinAndMax([1234567890]))


# 迭代器
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fibon(10):
    print(x)


# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))