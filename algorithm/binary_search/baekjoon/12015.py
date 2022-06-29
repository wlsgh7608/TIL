"""
https://www.acmicpc.net/problem/12015
가장 긴 증가하는 부분 수열 2 / 골드 2 / 40분
"""
import sys
input =  sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))

max_lists = []

# lower bound 
# target값 보다 같거나 큰 가장 작은 인덱스
def idx_check(arr,target):
    lo ,hi = 0, len(arr)-1
    while lo <= hi:
        m = (lo+hi)//2
        if arr[m] >= target:
            hi = m-1
        else:
            lo = m+1
    return lo

for number in n_list:
    idx = idx_check(max_lists,number)
    if idx == len(max_lists):
        max_lists.append(number)
    else:
        max_lists[idx] = number

print(len(max_lists))

"""
input 
1
10 5


10 20 10 30 20 50

1. 10인경우
리스트가 비어있으니 
2. 20 인 경우
리스트에 추가
3. 10 인 경우
리스트[0] = 10
4. 30
리스트에 추가
5. 20 인 경우 
리스트[1]= 20
6. 50인 경우
리스트에 추가

리스트 = [10,20,30,50]


"""