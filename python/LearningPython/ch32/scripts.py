"""
새 형식 클래스틑 클래스의 핵심 행위 변경
ex) 다이아몬드 패턴의 상속 검색, 내장된 동작과의 상호 작용, 


# 새 형식 클래스 변경 내역


1. 내장된 클래스의 속성 가져오기 : 인스턴스 생략
__getattr__와 __getattribute__의 일반적인 속성 가르채기 메소드는 암묵적으로 가져오는 속성에는 사용 X
이름 검색은 인스턴스가 아니라 클래스에서 시작 -> 내장된 작업에 영향을 주는 변경 내역

내장된 인덱스 오버로딩 메소드 구현 시
X[I] => X.__getitem__(I) - 레거시 클래스
        type(X).__getitem__(X,I) - 새 형식 클래스 

검색 변경 이유
 - 최적화 경로
 - 불분명한 호출 패턴의 이슈 

클래스는 스스로 타입이자 인스턴스
"""


"""
class C(object):
    data = 'spam'
    def __getattr__(self,name):
        print('getattr: '+name)
        return getattr(self.data, name)

X = C()
# __getitem__ : 인덱싱, 슬라이싱에 사용
print(X.__getitem__(1))
# print(X[1]) TypeError: 'C' object is not subscriptable
# print(type(X).__getitem__(X,1))  AttributeError: type object 'C' has no attribute '__getitem__'
print(X.__add__('eggs')) # 인스턴스 표현식은 표현식에 대해서만 생략
# print(X+'eggs') TypeError: unsupported operand type(s) for +: 'C' and 'str'
# print(type(X).__add__(X,'eggs')) AttributeError: type object 'C' has no attribute '__add__'


"""


"""
class C(object):
    data = 'spam'
    def __getattr__(self,name):
        print('getattr: '+name)
        return getattr(self.data, name)
    
    def __getitem__(self,i):
        print('getitem' +str(i))
        return self.data[i]
    def __add__(self,other):
        print('add: '+other)
        return getattr(self.data, '__add__')(other)


X = C()
print(X.upper)
print(X.upper())
print(X[1])
print(X.__getitem__(1))
print(type(X).__getitem__(X, 1))
print(X+'eggs')
print(X.__add__('eggs'))
print(type(X).__add__(X, 'eggs'))
"""


class C:
    pass

I = C()
print(type(I),I.__class__) # 인스턴스의 타입은 인스턴스가 유래된 클래스
print(type(C),C.__class__) #클래스는 타입, 타입은 클래스
print(type([1,2,3]),[1,2,3].__class__)
print(type(list),list.__class__)

"""
각 클래스는 메타클래스에 의해 생성
메타클래스는 type의 서브클래스

"""