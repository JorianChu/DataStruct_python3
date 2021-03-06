# -*- coding: utf-8 -*-
# @Time    : 2020/12/4
# @Author  : Jorian (jiangchao.zhu@foxmail.com)
# @File    : balanced_parentheses.py
# @Software: PyCharm


class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):
        # 判断栈容量是否超出范围
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            # 空栈不能弹出元素
            raise IndexError('pop from an empty stack')

    def peek(self):  # 查看栈顶元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):  #　判断栈是否为空
        return not bool(self.stack)

    def size(self):  # 返回栈的大小
        return len(self.stack)


def balanced_parentheses(parentheses):
    '''
    使用一个堆栈检查括号字符串是否平衡
    '''
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))