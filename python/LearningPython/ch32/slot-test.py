from ListTree import ListTree


class C(ListTree):
    pass

X = C()
print(X)

class C(ListTree):
    __slots__ = ['a','b']
X = C()
X.c = 3
print(X)