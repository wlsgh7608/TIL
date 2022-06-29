# 37 플로이드
## 플로이드 / 골드 5 / 10분
## 실패1(출력초과 1)
- 모든 지점에서 출발하여 모든 지점에 도착하는 거리를 계산하는 문제
- 플로이드 워셜을 이용하여 계산
- 플로이드 워셜의 경우 O(n^3)이므로 입력 범위를 잘 생각하는 것이 좋을 것 같음
- 플로이드 워셜의 k값은 지나가는 도시를 의미
``` python
def floyd_warshall():
    for k in range(N): # k: 지나가는 도시
        for i in range(N): # 시작
            for j in range(N): # 끝
                G[i][j] = min(G[i][j],G[i][k]+G[k][j]) # i에서 j를 가는 경우와 i에서 k를 거쳐 j가는 경우 비교
```
## 전체 코드
``` python
import sys
INF = sys.maxsize
input = sys.stdin.readline

def floyd_warshall():
    for k in range(N): # k: 지나가는 도시
        for i in range(N): # 시작
            for j in range(N): # 끝
                G[i][j] = min(G[i][j],G[i][k]+G[k][j]) # i에서 j를 가는 경우와 i에서 k를 거쳐 j가는 경우 비교

N = int(input())
M = int(input())
G = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s,e,w = map(int,input().split())
    s,e = s-1,e-1
    G[s][e] = min(G[s][e],w)

floyd_warshall()

for i in range(N):
    for j in range(N):
        if i==j or G[i][j]== INF:
            print(0,end=" ")
        else:
            print(G[i][j],end=" ")
    print()

```

# 38 정확한 순위
- A->B로 가는 길이 있다
 - A는 B보다 순위가 높다
- C->A로 가는 길이 있다
 -  C는 A보다 순위가 높다
- 모든 지점에서 다른 모든 지점 체크해야함 -> 플로이드워셜
- `G[i][j]` 값과 `G[j][i]` 값이 둘다 INF라면 순위를 알 수 없음 
``` python
        if G[i][j] == INF and G[j][i] == INF: # 순위를 알 수 없음
```

## 전체 코드
``` python
import sys
input = sys.stdin.readline
INF = sys.maxsize

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j],G[i][k]+G[k][j])


N,M = map(int,input().split())
G = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s,e = map(int,input().split())
    s,e = s-1,e-1
    G[s][e] = 1 # s->e로 가는 길이 있다.


floyd_warshall()
cnt = 0
for i in range(N):
    for j in range(N):
        """
        i,j 비교
        i->j 로 가는 길이 있다. i는 j보다 순위가 높다
        j->i 로 가는 길이 있다. j는 i보다 순위가 높다
        """
        if i==j:
            continue
        if G[i][j] == INF and G[j][i] == INF: # 순위를 알 수 없음
            break
    else:
        cnt +=1

print(cnt)



```

# 39 화성 탐사
- (0,0) -> (N-1,N-1)로 가는 최단 경로만 찾으면 됨
 -  다익스트라 알고리즘

- 방문하지 않은 정점은 큐에 추가
``` python
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: 
```
## 전체 코드
``` python
import sys
INF = sys.maxsize
imput = sys.stdin.readline
import heapq
X = [-1,1,0,0]
Y = [0,0,-1,1]
def dijkstra(v):
    visited = [[False for _ in range(N)] for _ in range(N)]
    Q = []
    heapq.heappush(Q,(G[v][v],v,v))
    while Q:
        w,x,y = heapq.heappop(Q)
        visited[x][y] = True
        if x==y== N-1: # 도착
            print(w)
            break
        for dx,dy in zip(X,Y):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: 
                heapq.heappush(Q,(w+G[nx][ny],nx,ny)) # 경로 추가

T = int(input())
for _ in range(T):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    M = [INF for _ in range(N)]
    dijkstra(0)
```



# 40 숨바꼭질
- 0에서 모든 지점까지의 최단 경로 -> 다익스트라
- 숨는 번호를 계산할 때 값이 INF라면 갈 수 없는 경우이므로 패스
- dist가 더 큰 경우 `max_size`,`max_idx` 할당
``` python
for idx,dist in enumerate(distance):
    # 숨는 번호, 거리 계산
    if dist== INF:
        continue
    if max_size< dist:
        max_idx = idx
        max_size = dist

```

## 전체 코드
``` python

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
```