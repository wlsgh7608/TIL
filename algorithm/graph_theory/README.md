# 다양한 그래프 알고리즘


__그래프__ 란 __노드__ 와 노드 사이에 연결된 __간선__ 의 정보를 가지고 있는 자료구조
서로 다른 개체가 연결되어 있다 -> 그래프 알고리즘

__트리(Tree)__ 자료구조는 다양한 알고리즘에서 사용됨


## 그래프 vs 트리
||그래프|트리|
|-------|----------|--------|
|방향성|방향 그래프 혹은 무방향 그래프| 방향그래프|
|순환성 | 순환 및 비순환| 비순환|
|루트 노드 존재 유무| 루트 노드가 없음 | 루트 노드가 존재|
|노드간 관계성| 부모와 자식 관계 없음| 부모와 자식 관계|
|모델의 종류| 네트워크 모델| 계층 모델|


## 그래프 구현 방법
- 인접 행렬(Adjacency Matrix) : 2차원 배열을 사용하는 방식
- 인접 리스트(Adjacency List) : 리스트를 사용하는 방식

노드의 개수가 V, 간선의 개수가 E인 그래프

메모리 공간
- 인접 행렬 : O(V^2)
- 인접 리스트 : O(E)

간선 연결 유무 시간복잡도
- 인접 행렬 : O(1)
- 인접 리스트 : O(V)


# 서로소 집합(Disjoint Set)
서로소 집합 : 고통 원소가 없는 두 집합

서로소 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
 - union 연산 : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
 - find 연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산


# 서로소 집합 자료구조
1️⃣ union 연산을 확인하여, 서로 연결된 두 노 드 A,B 확인
   1. A와 B의 루트 노드 A', B'를 각각 찾는다
   2. A'를 B'의 부모 노드로 설정
2️⃣ 모든 union 연산을 처리할 때 까지 1️⃣번 과정 반복


1,2,3,4,5의 노드에서 
다음과 같은 연산을 한다고 가정해 봅시다
union 3,4
union 2,5
union 1,5
union 2,4 

위의 과정을 그림으로 나타내면 다음과 같습니다.
<img src="https://user-images.githubusercontent.com/62232531/163657140-10df7bc3-d0db-4cdb-8277-4dee41674aa4.gif">


## 파이썬 코드
``` python
def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0]*(v+1)

# 자기 자신 초기화
for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)


print("각 원소가 속한 집합")
for i in range(1,v+1):
    print(find_parent(parent,i),end=" ")
print()

print("부모 테이블")
for i in range(1,v+1):
    print(parent[i],end=" ")

"""
input 
5 4 
3 4
2 5
1 5
2 4
"""

```

## 이 알고리즘의 문제점
- __부모 노드__ 를 거슬러 찾아서 업데이트를 해줘야 함 
__경로 압축__ 을 이용하여 시간 복잡도 개선

### 경로 압축
``` python
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
```

## 전체 코드
``` python
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0]*(v+1)

# 자기 자신 초기화
for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)


print("각 원소가 속한 집합")
for i in range(1,v+1):
    print(find_parent(parent,i),end=" ")
print()

print("부모 테이블")
for i in range(1,v+1):
    print(parent[i],end=" ")
"""
input 
5 4 
3 4
2 5
1 5
2 4
"""
```

# 서로소 집합을 활용한 사이클 판별
- 무방향 그래프에서의 사이클 판별 - 서로소 집합 
- 방향 그래프에서의 사이클 판별 - DFS

그래프의 간선(edge)을 union 연산으로 표현하여 사이클 판별
1️⃣ 각 간선을 확인하여 두 노드의 루트 노드를 확인
   1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행
   2. 루트 노드가 같다면 사이클(Cycle) 발생
2️⃣ 그래프에 포함되어 있는 모든 간선에 대하여 1️⃣번 과정을 반복

``` python
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0]*(v+1)

# 자기 자신 초기화
for i in range(1,v+1):
    parent[i] = i

cycle = True
for i in range(e):
    a,b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 X")

"""
input 
3 3
1 2
1 3
2 3
"""
```



# 신장 트리(Spanning Tree)
- 하나의 그래프가 있을 떄 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 크루스칼 알고리즘(Kruskal Algorithm)
- 최소 신장 알고리즘중 하나
- 가장 적은 비용으로 모든 노드를 연결하는 알고리즘


1️⃣ 간선 데이터를 비용에 따라 오름차순 정렬
2️⃣ 간선을 하나씩 확인하여 현재의 간선이 사이클을 발생하는 지 확인
   1. 사이클이 발생하는 경우 최소 신장 트리에 포함 X
   2. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
3️⃣ 모든 간선에 대하여 2️⃣번의 과정 반복

- 시간복잡도 : O(ElogE)
``` python
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0]*(v+1)
result = 0 
# 자기 자신 초기화
for i in range(1,v+1):
    parent[i] = i

cycle = True
E = []
for i in range(e):
    a,b,cost = map(int,input().split())
    E.append((cost,a,b))

E.sort()
for edge in E:
    cost,a,b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result+=cost
print(result)

"""
input 
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""


```

# 위상 정렬(Topology Sort)
- 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
- 시간 복잡도 : O(V+E)

``` python
from collections import deque

v,e = map(int,input().split())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
        
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i]==0:
                q.append(i)
    print(*result)
topology_sort()

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

"""
```
