#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:33
"""

def fibo(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibo(num-1)+fibo(num-2)
    else:
        print("False")

# 使用列表生成式打印出斐波那契数列
l = [fibo(i) for i in range(1, 5)]
print(l)


def fibo(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    l = [1, 1]
    for i in range(2, num):
        # 将列表最后两项的值求和，将值添加到列表最后
        l.append(l[-2]+l[-1])
    return l

print(fibo(4))

def fibo(num):
    a, b = 1, 1
    l = []
    for _ in range(num):
        l.append(a)
        a, b = b, a+b
    return l

print(fibo(4))