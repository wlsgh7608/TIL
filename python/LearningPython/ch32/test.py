class ListTree:
    """
    전체 클래스트 트리와 self와 그 위로 존재하는 모든 객체들의 속성에 대한 __str__ 추적 결과 반환
    클라이언트에 영향을 주는 것을 피하기 위해 __X 속성 이름 사용
    """

    def __attrnames(self,obj,indent):
        spaces = ' ' *(indent+1)
        result =''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + f'{attr}\n'
            else:
                result += spaces + f'{attr} = {getattr(obj,attr)}\n'
        return result

    def __listclass(self,aClass,indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return f'\n{dots}<Class {aClass.__name__}:, address {id(aClass)}: (see above)>\n'
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super,indent+4)
            return f'\n{dots}<Class {aClass.__name__}, address {id(aClass)}:\n {here}{above}{dots}>\n'

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return f'<Instance of {self.__class__.__name__}, address {id(self)}: \n {here}{above}'


class C(ListTree): pass

X = C()
print(X)

class C(ListTree): __slots__ = ['a','b']

X = C()
X.c = 3
print(X)