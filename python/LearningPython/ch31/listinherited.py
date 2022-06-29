class ListInherited:
    """
    dir()을 사용하여 인스턴스 속성과 그 인스턴스의 클래스로부터 상속받은 이름을 수집
    3.X 버전은 2.X보다 많은 이름을 보여주는 데 
    그 이유는 암묵적으로 object 클래스를 상속받기 때문
    """
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__': # 스페셜 메소드
                result += f'\t{attr}\n'
            else:
                result += f'\t{attr} ={getattr(self,attr)} \n' # 스페셜 메소드가 아닌 경우
        return result

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}: \n{self.__attrnames()}>'

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)