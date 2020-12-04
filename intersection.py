#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:32
"""

'''
如果题目不提供导函数，只提供本函数表达式，但是提供一个合理区间，如何求解该区间内的零点？
'''

def intersection(function, start1, start2):
    # function 是 f(x),start1,start2 是区间端点
    x_n = start1
    x_n1 = start2
    while True:
        x_n2 = x_n1-(function(x_n1) /
                     ((function(x_n1)-function(x_n))/(x_n1-x_n)))  # 递归式
        if abs(x_n2-x_n1) < 10**-5:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2


def f(x):
    return (x**3)-2*x-5


if __name__ == "__main__":
    print(intersection(f, 3, 3.5))