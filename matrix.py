#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  15:07
"""
import random

from .vector import Vector

def zeroVector(dimension):  # 零向量的实现
    assert(isinstance(dimension, int))
    return Vector([0]*dimension)

class Matrix(object):
    def __init__(self,matrix,w,h):  # 矩阵的初始化
        self.__matrix = matrix
        self.__width = w
        self.__height = h

    def __str__(self):  # 返回矩阵的字符表达形式
        ans = ""
        for i in range(self.__height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width -1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans

    def changeComponent(self,x,y, value):  # 改变矩阵特定位置的元素
        if x >= 0 and x < self.__height and y >= 0 and y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception ("changeComponent: indices out of bounds")

    def component(self,x,y):  # 返回矩阵特定位置的元素
        if x >= 0 and x < self.__height and y >= 0 and y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception ("changeComponent: indices out of bounds")

    def width(self):  # 返回矩阵的宽度
        return self.__width

    def height(self):  # 返回矩阵的高度
        return self.__height

    def __mul__(self,other):  # 矩阵的乘积
        if isinstance(other, Vector):  # 判断与矩阵乘积的对象是向量
            if (len(other) == self.__width):
                ans = zeroVector(self.__height)
                for i in range(self.__height):
                    summe = 0
                    for j in range(self.__width):
                        summe += other.component(j) * self.__matrix[i][j]
                    ans.changeComponent(i,summe)
                    summe = 0
                return ans
            else:
                raise Exception("vector must have the same size as the " + "number of columns of the matrix!")
        elif isinstance(other,int) or isinstance(other,float): #判断与矩阵乘积的是标量，即数乘
            matrix = [[self.__matrix[i][j] * other for j in range(self.__width)] for i in range(self.__height)]
            return Matrix(matrix,self.__width,self.__height)

    def __add__(self,other):  # 矩阵的加法
        if (self.__width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] + other.component(i,j))
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
        else:
            raise Exception("matrix must have the same dimension!")

    def __sub__(self,other):  # 矩阵的减法
        if (self.__width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] - other.component(i,j))
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
        else:
            raise Exception("matrix must have the same dimension!")

def randomMatrix(W, H, a, b):
    # 随机矩阵的元素在(a,b)范围内，矩阵宽为 W,矩阵高为 H
    random.seed(None)
    matrix = [[random.randint(a,b) for j in range(W)] for i in range(H)]
    return Matrix(matrix,W,H)