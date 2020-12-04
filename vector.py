#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  14:30
"""

class Vector(object):
    def __init__(self, components=[]):  # 向量的初始化
        self.__components = list(components)

    def set(self, components):  # 改变向量内的数组
        if len(components) > 0:
            self.__components = list(components)
        else:
            raise Exception("please give any vector")

    def __str__(self):  # 返回向量的字符形式
        return "(" + ",".join(map(str, self.__components)) + ")"

    def component(self, i):  # 返回向量的某个元素
        if type(i) is int and -len(self.__components) <= i < len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def __len__(self):  # 返回向量的长度
        return len(self.__components)

    def eulidLength(self):  # 返回向量的欧几里得长度
        summe = 0
        for c in self.__components:
            summe += c**2
        return math.sqrt(summe)

    def changeComponent(self, pos, value):  # 改变向量指定位置的元素
        assert (-len(self.__components) <= pos < len(self.__components))
        self.__components[pos] = value

    def __add__(self, other):  # 向量的加法
        size = len(self)
        if size == len(other):
            result = [self.__components[i] +
                      other.component(i) for i in range(size)]
            return Vector(result)
        else:
            raise Exception("must have the same size")

    def __sub__(self, other):  # 向量的减法
        size = len(self)
        if size == len(other):
            result = [self.__components[i] -
                      other.component(i) for i in range(size)]
            return result
        else:
            raise Exception("must have the same size")

    def __mul__(self, other):  # 向量的数乘
        if isinstance(other, float) or isinstance(other, int):
            ans = [c*other for c in self.__components]
            return ans
        elif (isinstance(other, Vector) and (len(self) == len(other))):
            size = len(self)
            summe = 0
            for i in range(size):
                summe += self.__components[i] * other.component(i)
            return summe
        else:  # error case
            raise Exception("invalide operand!")