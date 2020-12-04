#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:28
"""
'''
对于任意大于 1 的自然数 n，若该数为偶数则将其变为原来的一半，
若为奇数则将其变为 3n+1。反复进行上述过程，直到结果为 1 时停止。
这就是著名的“3n+1”问题。要求输入 n，
输出按“3n+1”规则变换到 1 所需要的数字变换次数。（n<=10^9）
'''

def function(num):
    mylist = [num]
    while num != 1:
        # 如果为奇数
        if num % 2 == 1:
            num = 3*num+1
            mylist.append(num)
        # 为偶数
        else:
            num = num//2
            mylist.append(num)
    return mylist, len(mylist)-1


print(function(43))