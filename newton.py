#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:31
"""

def newton(function, function1, start):
    # function 是 f(x) function1 是 f(x)的导函数，即f'(x)
    x_n = start
    while True:
        x_n1 = x_n-function(x_n)/function1(x_n)  # 递归式
        if abs(x_n-x_n1) < 10**-5:
            return x_n1
        x_n = x_n1


def f(x):
    return (x**3)-2*x-5


def f1(x):
    return 3*(x**2)-2


if __name__ == "__main__":
    print(newton(f, f1, 3))