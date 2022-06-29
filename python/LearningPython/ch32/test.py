class Slotful:
    __slots__ = ['a','b','__dict__']
    def __init__(self,data):
        self.c = data

I = Slotful(3)
I.a,I.b = 1,2
print(I.a,I.b,I.c)
print(I.__dict__)
print([x for x in dir(I) if not x.startswith('__')])
print(I.__dict__['c'])
print(getattr(I, 'c'),getattr(I, 'a'))

for a in (x for x in dir(I) if not x.startswith('__')):
    print(a,getattr(I,a))