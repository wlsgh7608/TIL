"""
https://www.acmicpc.net/problem/15686
- [✔] 완전탐색(브루트 포스) 
- [ ] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
    - 조합을 이용하여 M개의 치킨집을 선정
    - 각 집에 대하여 가장 짧은 치킨집 거리 계산
"""
from itertools import combinations


def manhattan_distance(x1,y1,x2,y2):
    dist = abs(x1-x2) + abs(y1-y2)
    return dist 

G = []
N,M = map(int,input().split())
for _ in range(N):
    G.append(list(map(int,input().split())))

chickens = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 2:
            chickens.append((i,j)) # 치킨 리스트
availables = list(combinations(chickens,M))
answer = 1_000_000_000
for available in availables:
    avail_dist = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                one_distance = 1_000_000_000
                for c in available:
                    cx,cy = c
                    one_distance = min(one_distance,manhattan_distance(i,j,cx,cy)) # 가장 짧은 치킨집
                avail_dist+= one_distance 
    answer = min(answer,avail_dist) # 선택된 치킨집의 총 최소 거리와 비교

print(answer)
                


