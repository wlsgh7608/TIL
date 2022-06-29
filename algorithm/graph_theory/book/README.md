# 41  [여행 계획](https://www.acmicpc.net/problem/1976)
## 여행 가자 / 골드 4/ 50분
## 실패 4(런타임 에러4)
## 인덱스 에러가 나는 이유를 모르겠어서 힌트얻고 품

- union find을 이용하여 구현
- 만약 여행도시에 대한 union 연산 결과 집합이 2개 이상일 경우
 - 해당 도시로 갈 수 없음
``` python
set_list = set(parent[travel-1] for travel in travels)
if len(set_list)>1:
    print("NO")
else:
    print("YES")
```

## 전체 코드
``` python
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
travels = list(map(int,input().split()))
parent= [i for i in range(N)]



def find_parent(x):
    if parent[x]!= x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a] = b

for i in range(N):
    for j in range(N):
        if G[i][j] ==1:
            union(i,j)



set_list = set(parent[travel-1] for travel in travels)
if len(set_list)>1:
    print("NO")
else:
    print("YES")
```

# 42 [탑승구](https://www.acmicpc.net/problem/10775)
## 공항 / 골드 2 / 60분
## 실패2(틀렸습니다 1 , 시간초과 1 )

- 비행기는 먼저 자기 자신의 번호부터 0번까지 도킹 가능성 판별
- 도킹가능한 경우 (해당 번호-1)와 `union`연산 수행
- 만약 도킹가능한 번호가 0번인 경우(`find_parent() 결과 : 0`) 더 이상 진행 불가
``` python
def union(a):
    a = find_parent(a)
    b = find_parent(a-1)
    if a==0:
        return False
    else:
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
        return True
```
## 전체 코드
``` python
import sys
input = sys.stdin.readlineㄴ


G = int(input())
P = int(input())
A = [int(input())for _ in range(P)]
parent  = [i for i in range(G+1)]

def find_parent(x):
    if parent[x]  != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a):
    a = find_parent(a)
    b = find_parent(a-1)
    if a==0:
        return False
    else:
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
        return True
result = 0
for air in A:
    if not union(air):
        break
    result +=1
print(result)
```

# 43 어두운 길
## Kruskal 알고리즘을 이용하여 최소신장트리 구현
- 만약 두 트리의 루트가 같은 경우 같은 집합이므로 절약 가능한 경우
- 두 트리의 루트가 다른 경우 union 연산 진행
  - union 연산
  ``` python
    r_s = find_parent(s)
    r_e = find_parent(e)
    if r_s != r_e:
        union(r_s,r_e)
    else:
        result+=v
  ```
 
## 전체 코드
``` python
N,M = map(int,input().split())
E = []
for _ in range(M):
    s,e,v = map(int,input().split())
    E.append((v,s,e))
parent = [i for  i in range(N)]

def find_parent(v):
    if parent[v] != v:
        parent[v] = find_parent(parent[v])
    return parent[v]
def union(a,b):
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



E.sort()
result = 0
check = 0
for v,s,e in E:
    r_s = find_parent(s)
    r_e = find_parent(e)
    if r_s != r_e:
        union(r_s,r_e)
    else:
        result+=v
    
print(result)
```

# 44 [행성 터널](https://www.acmicpc.net/problem/2887)
## 행성 터널 / 골드 1 / 40분
## 실패 3 (메모리초과 3)
- 기존의 방법을 계속 시도해도 메모리 초과 발생
- 구글링을 통해 힌트 알게됨

- 거리를 계산하는 것은 x,y,z 좌표들의 차이만 이용
 - 따라서 x,y,z별로 가장 가까운 것만 E리스트에 추가
``` python
for k in range(3):
    G.sort(key=lambda x: x[k])
    for i in range(N-1):
        dist = abs(G[i][k] - G[i+1][k])
        a = G[i][3]
        b = G[i+1][3]
        E.append((dist,a,b))
```
## 전체 코드
``` python
import sys
input = sys.stdin.readline
N = int(input())
G=[]
for i in range(N):
    x,y,z = list(map(int,input().split()))
    G.append((x,y,z,i))
    
E = []


def find_parent(v):
    if parent[v]!=v:
        parent[v] = find_parent(parent[v])
    return parent[v]
def union(a,b):
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for k in range(3):
    G.sort(key=lambda x: x[k])
    for i in range(N-1):
        dist = abs(G[i][k] - G[i+1][k])
        a = G[i][3]
        b = G[i+1][3]
        E.append((dist,a,b))

        


parent = [i for i in range(N)]
E.sort()
result = 0
for v,a,b in E:
    r_a = find_parent(a)
    r_b =  find_parent(b)
    if r_a != r_b:
        union(r_a,r_b)
        result+=v
    
print(result)

```