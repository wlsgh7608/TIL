"""
https://www.acmicpc.net/problem/4386
별자리 만들기 / 골드 4 /  13분
09:18 ~ 09:31
"""
import sys
input = sys.stdin.readline

def get_distance(a,b):
    # 거리구하기
    dx = abs(a[0]-b[0])
    dy = abs(a[1]-b[1])
    return (dx**2+dy**2)**0.5

def find_parent(x):
    # 부모 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    # 합집합
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
G = []
E = []
parent = [i for i in range(n)]

for _ in range(n):
    x,y = map(float,input().split())
    G.append((x,y))

for i in range(n):
    for j in range(i+1,n):
        dist = get_distance(G[i],G[j])
        E.append((dist,i,j))

E.sort()
result = 0
for w,a,b in E:
    r_a = find_parent(a)
    r_b = find_parent(b)
    if r_a != r_b:
        union(r_a,r_b)
        result+=w
    
print('%.2f'%result)





