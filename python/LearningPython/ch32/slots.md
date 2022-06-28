## 슬롯 : 속성 선언

- 속성 이름의 시퀀스를  `__slots__` 클래스 속성에 할당 => 새 형식 클래스가 자신의 인스터스가 갖게 될 `속성 제한`
=> 메모리 사용률, 프로그램 속도 `최적화`

단점 : 코드를 복잡하게 만듦, 파이썬의 특징인 `동적  파괴`

- 확실하게 보장된 경우를 제외하면 사용되지 않는 것이 좋음



## 슬롯 사용하기

class문 최상위 속성에 `__slots__` 변수 할당  

-  `__slots__` 리스트에 있는 이름들만이 인스턴스 속성에 할당됨
``` python
class limiter(object):
    __slots__ = ['age','name','job']
x = limiter()
# print(x.age) #  사용되기 전에 할당되어야 함 
x.age = 40
print(x.age)
x. ape = 1000 # __slots__에 없는 속성으로 오류 발생
```

# __slots__ 




# 슬롯과 네임스페이스 딕셔너리
``` python
class C:
    __slots__ = ['a','b']

X = C()
X.a = 1
print(X.a)
# print(X.__dict__)
print(getattr(X,'a'))
```
클래스 `디스크립터` 특성을 사용하여 인스턴스 슬롯 설정을 위해 예약된 공간을 배정하고 관리


여전히 getattr , setattr 사용가능(인스턴스 __dict__너머를 보기 떄문에 슬롯과 같은 클래스 레벨의 이름 포함 가능)
``` python
getattr(X,'a') # 1
setattr(X,'b',2) 
X.b # 2
'a' in dir(X) # True
'b' in dir(X) # True
```



속성 네임스페이스 딕셔너리 없이는 새로운 일므을 슬롯 리스트에 있는 이름이 아닌 인스턴스에 할당 X
``` python
class D:
    __slots__ = ['a','b']
    def __init(self):
        self.d = 4

X = D()
X.d
```


`__slots__` 안에 명시적으로 `__dict__`을 포함함으로써 추가 속성 수용 가능

``` python
class D:
    __slots__ = ['a','b','__dict__']
    c = 3
    def __init__(self):
        self.d = 4

X = D()
X.d # 4
X.c # 3   
X.a # AttributeError: a
X.a = 1
X.__dict__  # {'d': 4}
X.__slots__ # ['a', 'b', '__dict__']
getattr(X,'a'),getattr(X,'c'),getattr(X,'d') #(1, 3, 4)
```



# 슈퍼 클래스의 다중 __slots__ 리스트
- 슬롯 이름은 클래스 레벨의 속성이 되기 때문에 일반적인 상속 규칙에 의거하여 트리의 어느 곳에 있든 상관없이 모든 슬롯 이름 통합 결과 취함

``` python
class E:
    __slots__ = ['c','d'] # 슈퍼클래스 슬롯
    

class D(E):
    __slots__ = ['a','__dict__'] # 서브클래스 슬롯


X = D()
X.a = 1; X.b = 2 ; X.c=3
X.a,X.c #(1, 3)

X.__slots__  # ['a', '__dict__'] 인스턴스는 가장낮은 슬롯 상속
X.__dict__ # 자신만의 속성 딕셔너리 존재
dir(X) # ..생략..'a', 'b', 'c', 'd' dir()은 모든 슬롯 포함
```

### 일반적으로 슬롯과 그 밖의 다른 '가상' 속성 다루기

일반적인 데이터 속성 나열
: 슬롯 + `프로퍼티`,`디스크립터` (가상 인스턴스)

``` python
class Slotful:
    __slots__ = ['a','b','__dict__']
    def __init__(self,data):
        self.c = data


I  = Slotful(3)
I.a,I.b = 1,2
I.a,I.b,I.c # (1, 2, 3)
I.__dict__ # {'c': 3} __dict__와 슬롯 모두 스토리지



```


## 슬롯 사용 규칙
- 서브클래스의 슬롯은 슈퍼클래스에 슬롯이 없는 경우 의미X
    - 슈퍼클래스를 위해 생성된 `__dict__` 속성은 항상 접근 가능하여 서브클래스의 `__slots__` 의미 없게 함
- 슈퍼클래스의 슬롯은 서브클래스에 슬롯이 없는 경우 의미X

   - 서브클래스는 인스턴스 `__dict__`을 생성하여 슈퍼클래스 `__slots__`을 무의미하게 함
- 재정의는 슈퍼클래스의 슬롯을 무의미하게 함
- 슬롯은 클래스 레벨의 기본값 방지
    - 슬롯은 클래스 레벨의 `디스크립터`로서 구현되기 때문에 기본값을 제공하기 위해 동일한 이름의 클래스 속성 사용 X
- 슬롯과 `__dict__` 
    - `__slots__` 은 인스턴스 `__dict__` 을 명시적으로 나열되지 않는 경우 열거되지 않은 이름 할당 막음

## 어떠한 클래스라도 슬롯을 생략하면 네임스페이스 딕셔너리가 생성 => 메모리 최적화 X

``` python
"""
1번 
   서브클래스 :  슬롯O , 슈퍼클래스 : 슬롯X
슬롯이 없는 경우 인스턴스 딕셔너리 생성
여전히 슬롯 이름은 클래스에서 관리
"""
class C: pass

class D(C): __slots__= ['a']

X = D()
X.a,X.b = 1,2
X.__dict__ #{'b': 2}
D.__dict__.keys() #dict_keys(['__module__', '__slots__', 'a', '__doc__'])


"""
2번
   서브클래스 : 슬롯 O , 슈퍼클래스 : 슬롯 X 
슬롯이 없는 경우 인스턴스 딕셔너리 생성
여전히 슬롯 이름은 클래스에서 관리
"""
class C: __slots__ = ['a']

class D(C):pass

X = D()
X.a,X.b = 1,2
X.__dict__ # {'b': 2}
C.__dict__.keys() # dict_keys(['__module__', '__slots__', 'a', '__doc__'])


"""
3번
   가장 낮은 슬롯에만 접근 가능
"""
class C: __slots__  = ['a']

class D(C): __slots__ = ['a']


"""
4번
   클래스 레벨의 기본값 X
"""
class C:
    __slots__ = ['a']
    a=99 #ValueError: 'a' in __slots__ conflicts with class variable
```
## 결론
 - 클래스 전부 `__slots__`가 있거나, 없어야 함

``` python
class C: __slots__ = ['a']

class D(C): __slots__ = ['b']


X = D() 
X.a,X.b = 1,2
# 인스턴스 딕셔너리 생성되지 않음
X.__dict__ #AttributeError: 'D' object has no attribute '__dict__' 
C.__dict__.keys() # dict_keys(['__module__', '__slots__', 'a', '__doc__'])
D.__dict__.keys() # dict_keys(['__module__', '__slots__', 'b', '__doc__'])
```



