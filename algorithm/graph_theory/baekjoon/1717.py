"""
https://www.acmicpc.net/problem/1717
집합의 표현 / 골드 4 / 8분
10:42 ~ 10:50

"""
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    o, a,b = map(int,input().split()) # 연산,a, b
    r_a = find_parent(a)
    r_b = find_parent(b)
    if o:
        # 확인
        if r_a == r_b:
            print("YES")
        else:
            print("NO")
    else:
        union(r_a,r_b)

    

