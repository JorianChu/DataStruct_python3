#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:17
"""

# 并查集实现
'''
1、维护无向图的连通性。支持判断两个点是否在同一连通块内，和判断增加一条边是否会产生环。
2、用在求解最小生成树的 Kruskal 算法里。
'''
def union(self, node_a, node_b):
    # 对合并的两个节点做初步判断，判断是否为空
    if node_a is None or node_b is None:
        return
    # 分别查找两个节点的父节点
    a_head = self.find(node_a)
    b_head = self.find(node_b)
    # 当两个节点的父节点不一样时，才能做合并操作
    if (a_head != b_head):
        a_set_size = self.size_dict[a_head]
        b_set_size = self.size_dict[b_head]
        # 根据集合的大小做判断，尽量使小集合并到大集合
        if (a_set_size >= b_set_size):
            self.father_dict[b_head] = a_head
            self.size_dict[a_head] = a_set_size + b_set_size
        else:
            self.father_dict[a_head] = b_head
            self.size_dict[b_head] = a_set_size + b_set_size