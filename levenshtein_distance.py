#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  16:25
"""

def levenshtein_distance(first_word, second_word):
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_world)
    if len(second_word) == 0:
        return len(first_word)
    previous_row = range(len(second_word)+1)
    for i, c1 in enumerate(first_word):
        current_row = [i+1]
        for j, c2 in enumerate(second_word):
            # 计算增加，删除，修改次数
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            # 得到最小值，添加到current_row
            current_row.append(min(insertions, deletions, substitutions))
        # 储存previous_row
        previous_row = current_row
    # 返回最后的编辑距离
    return previous_row[-1]