# https://www.acmicpc.net/problem/11399
"""
### 체크리스트
- [X] 현재 상황에서 가장 좋은 것만 고르는가? 
 -시간이 가장 짧은 사람부터 사용한다

- [X] 해당 해법이 정당한가? 
 - 기다리는 시간의 경우 앞의 사람들의 시간을 더함
 t1 : 0
 t2 : t1
 t3 : t1+t2
 t4 : t1+t2+t3

 따라서 가장 작은 시간의 사람부터 사용해야 최소의 시간이 나옴


시간복잡도 : O(nlogn) - sort
"""



n = int(input())
t_list=  list(map(int,input().split()))

t_list.sort()
w = 0 # waiting
total = 0
for t in t_list:
    total += w+t
    w +=t
print(total)