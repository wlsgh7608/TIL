class ListInherited:
    """
    dir()을 사용하여 인스턴스 속성과 그 인스턴스의 클래스로부터 상속받은 이름을 수집
    3.X 버전은 2.X보다 많은 이름을 보여주는 데 
    그 이유는 암묵적으로 object 클래스를 상속받기 때문
    """
    def __attrnames(self,indent=' '*4):
        # %%는 뭐징
        # result = f'Unders{'-'*77}\n{indent}  
        result = 'Unders%s\n%s%%s\nOthers%s\n'%('-'*77,indent,'-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__': # 스페셜 메소드
                unders.append(attr)
            else:
                display = str(getattr(self,attr))[:82-len(indent)+len(attr)]
                result += '%s%s=%s\n' %(indent,attr,display)
        return result % ', '.join(unders)

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}: \n{self.__attrnames()}>'

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)