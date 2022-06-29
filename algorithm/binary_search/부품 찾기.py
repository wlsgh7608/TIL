# 부품 찾기
import sys
input = sys.stdin.readline
N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

for target in m_list:
    s,e = 0,N-1
    while s<=e:
        m = (s+e)//2
        if n_list[m] == target:
            print("yes",end = ' ')
            break
        elif n_list[m] > target:
            e = m-1
        else:
            s = m+1
    else:
        print("no",end =' ')

"""
1. 이진 탐색
2. 계수정렬
3. 집합자료형


5
8 3 7 9 2
3 
5 7 9


"""