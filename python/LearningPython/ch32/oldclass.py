# class C(object):
#     data = 'spam'
#     def __getattr__(self,name):
#         print("getattr: ",name)
#         return getattr(self.data, name)
# X = C()
# print(X.__getitem__(1))
# # print(X[1])
# # print(type(X).__getitem__(X,1))
# X.__add__('eggs')



# X = C()
# # X[0]
# # print(X)
# X.normal = lambda: 99
# print(X.normal())
# X.__add__ = lambda(y) : 88+y
# X+1


# print("새 형식 클래스")
# class C(object):
#     pass
# X = C()
# X.normal = lambda : 99
# X.normal()

# # X.__add__ = lambda(y):88+y
# X.__add__(1)
# X+1



class C(object):
    data = 'spam'
    def __getattr__(self,name):
        print('getattr: ' + name)
        return getattr(self.data,name)
    
    def __getitem__(self,i):
        print('getitem: ' + str(i))
        return self.data[i]
    
    def __add__(self,other):
        print('add: ' +other)
        return getattr(self.data,"__add__")(other)


X = C()
print(X.upper)
print(X.upper())
print(X[1])
print(X.__getitem__(1))
print(type(X).__getitem__(X,1))
print(X + "eggs")
print(X.__add__('eggs'))
print(type(X).__add__(X,'eggs'))
