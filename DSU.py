class DSU:
    def __init__(self, n):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]

    def find (self,x):
        if (self.parent[x]!=x):
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if (px==py):
            return

        if (self.rank[px] < self.rank[py]):
            self.parent[px] = py
        elif (self.rank[px] > self.rank[py]):
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] = self.rank[px]+1

ob = DSU(5)
ob.union(0, 2)
ob.union(4, 2)
ob.union(3, 1)
if ob.find(4) == ob.find(0):
    print('Yes')
else:
    print('No')
if ob.find(1) == ob.find(0):
    print('Yes')
else:
    print('No')