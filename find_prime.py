#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:20
"""


def find_prime(num):
    if num > 1:  # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not prime numer")
                print(i, "*", num//i, "=", num)
                break
        else:
            print(num, "is prime number")
    else:
        # 如果输入的数字小于或等于 1，直接返回不是质数
        print(num, "is not prime number")
num = int(input("please one number: "))
find_prime(num)