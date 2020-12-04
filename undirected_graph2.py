#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:12
"""

# 无向图的邻接矩阵实现
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex)]

    def insert(self, u, v):
        # 对存在连接关系的两个点，在矩阵里置1代表存在连接关系，没有连接关系则置0
        self.graph[u - 1][v - 1] = 1
        self.graph[v - 1][u - 1] = 1

    def show(self):  # 展示图
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')


graph = Graph(5)
graph.insert(1, 4)
graph.insert(4, 2)
graph.insert(4, 5)
graph.insert(2, 5)
graph.insert(5, 3)
graph.show()