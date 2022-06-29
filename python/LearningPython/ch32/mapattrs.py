import pprint

def trace(X,label='',end='\n'):
    # 출력하기
    print(label + pprint.pformat(X) + end)

def filterdictvals(D,V):
    # 값 V를 갖는 엔트리가 제거된 딕셔너리
    return {K:V2 for (K,V2) in D.items() if V2 != V}

def invertdict(D):
    # 키로 변경된 값을 갖는 딕셔너리 D(값 기준으로 그룹핑)
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}

def dflr(cls):
    """
    cls 지점에서 클래스 트리의 전통적인 깊이 우선, 왼쪽 -> 오른쪽 순서
    반복 불가능 : 파이썬에서 __bases__ 변경할 수 없음
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    """
    상속 순서 시퀀스 : 새로운 형식(MRO) 혹은 고전 형식(DFLR)
    """
    if hasattr(instance.__class__, '__mro__'): # MRO
        return (instance,) + instance.__class__.__mro__
    else: # DFLR
        return [instance] + dflr(instance,__class__)

def mapattrs(instance,withobject=False, bysource = False):
    """
    인스턴스의 모든 상속받은 속성을 제공하는 키와
    각 속성의 상속받은 근원인 객체를 제공하는 값으로 이루어진 딕셔너리
    withobject:False = 내장된 클래스 속성 객체 제거
    bysource: True = 속성 대신 객체에 의한 결과를 그룹화
    인스턴스에서 __dict__를 배제하는 슬롯으로 클래스를 지원  
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj,"__dict__") and attr in obj.__dict__ : # 슬롯 참조
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)


if __name__ == '__main__':

    print("X")
    print("Classic classes in 2.X new-style in 3.X")
    class A:
        attr1 = 1
    class B(A):
        attr2 = 2
    class C(A):
        attr1 = 3
    class D(B,C):
        pass
    I = D()
    print("Py => %s" % I.attr1)
    trace(inheritance(I),           "INH\n")
    trace(mapattrs(I),          'ATTRS\n')
    trace(mapattrs(I,bysource = True), 'OBJS\n')

    print('New-style classes in 2.X and 3.X')
    class A(object):
        attr1 =1 
    class B(A):
        attr2 = 2
    class C(A):
        attr1 = 3
    class D(B,C):
        pass
    I = D()
    print("Py => %s" % I.attr1)
    trace(inheritance(I),           "INH\n")
    trace(mapattrs(I),          'ATTRS\n')
    trace(mapattrs(I,bysource = True), 'OBJS\n')