"""
0에서 모든 지점까지의 최단 경로 -> 다익스트라

"""

import sys
input = sys.stdin.readline

def dijkstra(v):
    import heapq
    Q = []
    visited = [False for _ in range(N)]
    distance = [INF for _ in range(N)]
    heapq.heappush(Q,(0,v))
    while Q:
        w,current = heapq.heappop(Q)
        visited[current] = True
        for next in G[current]:
            if not visited[next] and distance[next]>w+1:
                distance[next] = w+1
                heapq.heappush(Q,(w+1,next))
    return distance


INF = sys.maxsize
N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s,e = map(int,input().split())
    s,e= s-1,e-1
    G[s].append(e)
    G[e].append(s)

distance = dijkstra(0)
max_size = 0
max_idx = 0

for idx,dist in enumerate(distance):
    # 숨는 번호, 거리 계산
    if dist== INF:
        continue
    if max_size< dist:
        max_idx = idx
        max_size = dist
# 개수 계산
max_count = distance.count(max_size)

print(max_idx+1,max_size,max_count)
"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

"""