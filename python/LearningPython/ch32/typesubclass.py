"""
사용자 정의 class문을 이용하여 내장된 타입의 행위를 바꾸거나 확장 가능
"""
class MyList(list):
    # 오버라이딩
    def __getitem__(self, offset): # 내장된 list의 __getitem__ 인덱싱 메소드를 확장
        print(f'Indexing {self} at {offset}')
        # return super().__getitem__(offset-1)  or
        return list.__getitem__(self, offset-1)
    

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)

    print(x[1]) # a
    print(x[3]) # c

    x.append('spam')
    print(x)
    x.reverse()
    print(x)


