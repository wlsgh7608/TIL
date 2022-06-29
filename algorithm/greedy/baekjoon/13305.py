"""
https://www.acmicpc.net/problem/13305
### 체크리스트
- [X] 현재 상황에서 가장 좋은 것만 고르는가? 
해당 주유소보다 값이 싼 주유소가 나올 때까지 기름을 담음
- [X] 해당 해법이 정당한가?
최소의 비용이 나오기 위해서는 싼 가격의 기름을 이용해야 함


시간복잡도 : O(n)
"""



n = int(input())
d = list(map(int,input().split()))
v = list(map(int,input().split()))

min_v = v[0]
sum_d = 0
total = 0


for cur_d,cur_v in zip(d,v[1:]):
    total += min_v*cur_d
    if cur_v < min_v:
        min_v = cur_v
    
print(total)
    




