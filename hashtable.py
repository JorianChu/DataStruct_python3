#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:21
"""


class hashtable(object):
    def __init__(self):
        self.items=[None]*100

    def hash(self,a):
        return a*1+1  # 线性映射关系

    def put(self,k,v):
        # 根据哈希结果，添加映射关系
        self.items[self.hash(k)] = v

    def get(self,k):
        hashcode=self.hash(k)
        # 根据哈希结果，返回正确匹配出结果
        return self.items[hashcode]

class hashtable(object):
    def __init__(self):
        self.capacity = 10
        self.hash_table = [[None, None]for i in range(self.capacity)]
        self.num = 0
        self.load_factor = 0.75

    def hash(self, k, i):
        h_value = (k+i) % self.capacity
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i = i+1
            h_value = self.hash(k, i)
        return h_value

    def resize(self):
        # 扩容到原有元素数量的两倍
        self.capacity = self.num*2
        temp = self.hash_table[:]
        self.hash_table = [[None, None]for i in range(self.capacity)]
        for i in temp:
            # 把原来已有的元素存入
            if(i[0] != None):
                hash_v = self.hash(i[0], 0)
                self.hash_table[hash_v][0] = i[0]
                self.hash_table[hash_v][1] = i[1]

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v
        # 暂不考虑 key 重复的情况，具体自己可以优化
        self.num = self.num+1
        # 如果比例大于载荷因子
        if(self.num/len(self.hash_table) > self.load_factor):
            self.resize()

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


table = hashtable()
for i in range(1, 13):
    table.put(i, i)
print(table.get(3))
print(table.hash_table)