#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:31
"""

import math


def bisection(function, a, b):  # 指定函数function,指定区间[a,b]
    start = a
    end = b
    if function(a) == 0:  # a即为零点
        return a
    elif function(b) == 0:  # b即为零点
        return b
    elif function(a) * function(b) > 0:  # 二分法无法在该区间找到零点
        print("couldn't find root in [a,b]")
        return
    else:  # f(a)*f(b)<0 的情况
        mid = (start + end) / 2
        while abs(start - mid) > 10**-7:  # 精确度设置为10**-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = (start + end) / 2
        return mid


def f(x):
    return math.pow(x, 3) - 2*x - 5


if __name__ == "__main__":
    print(bisection(f, 1, 1000))