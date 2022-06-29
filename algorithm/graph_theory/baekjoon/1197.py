"""
https://www.acmicpc.net/problem/1197

최소 스패닝 트리 / 골드 4 / 10분
"""

import sys



def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    if a>b:
        parent[a] = b
    else:
        parent[b] = a 

input = sys.stdin.readline
INF = sys.maxsize
V,E = map(int,input().split())
parent = [i for i in range(V+1)]
D = [INF for _ in range(V+1)]
edges = []

for _ in range(E):
    s,e,w = map(int,input().split())
    edges.append((w,s,e))

edges.sort()
result = 0
for w,s,e in edges:
    root_s = find_parent(s)
    root_e = find_parent(e)
    if root_s !=root_e:
        union(root_s,root_e)
        result+=w
print(result)






