# 1. 서브클래스의 슬롯은 슈퍼 클래스으ㅔ 슬롯이 없는 경우 의미가 없음
print("case 1 : 서브 클래스에만 슬롯 있음")
class C:
    pass

class D(C):
    __slots__ =['a']

X = D()
X.a,X.b = 1,2
print(X.__dict__)
print(D.__dict__.keys())


# 2 . 슬롯이 슈퍼클래스에는 있으나, 서브클래스에는 없음
print("case 2 : 슈퍼클래스에만 슬롯 있음")
class C :
    __slots__ = ['a']

class D(C):
    pass

X = D()
X.a,X.b = 1,2
print(X.__dict__)
print(C.__dict__.keys())

# 3. 가장 낮은 슬롯에만 접근 가능
class C:
    __slots__=['a']

class D(C):
    __slots__ = ['a']

# 4 . 클래스 레벨의 기본값은 없음

class C:
    __slots__ = ['a']
    a = 99


