#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  15:53
"""

def binarysearch(sorted_sequence, target):
    left = 0
    right = len(sorted_sequence) - 1
    while(left <= right):
        midpoint = (left+right) // 2
        current_item = sorted_sequence[midpoint]
        if current_item == target:
            return midpoint
        elif target < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None