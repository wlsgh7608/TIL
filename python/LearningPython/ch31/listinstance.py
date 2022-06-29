class ListInstance:
    """
    print() or str()을 제공하는 혼합 클래스
    __X 이름은 클라이언트의 속성과 충돌을 피하기 위함

    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\t{attr}={self.__dict__[attr]}\n' 
        return result
    
    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}: \n{self.__attrnames()}>'

if __name__ == '__main__':
    import testmixin
    # print("HI")
    testmixin.tester(ListInstance)