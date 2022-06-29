"""
https://www.acmicpc.net/problem/4195
친구 네트워크 / 골드 2 / 60분
10:51 ~ 11 :50
"""
import sys
input = sys.stdin.readline
T = int(input())

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a< b:
        parent[b] = a
        numbers[a] += numbers[b]
        return a 
    elif a>b:
        parent[a] = b
        numbers[b] += numbers[a]
        return b
    else:
        return a
for _ in range(T):
    F = int(input())
    fn = 0
    parent = []
    numbers = []
    D = {}
    for _ in range(F):
        a,b = input().split()
        for x in (a,b):
            if x not in D:
                D[x] = fn
                parent.append(fn)
                numbers.append(1)
                fn+=1
        a = D[a]
        b = D[b]
        min_n = union(a,b)
        print(numbers[min_n])
        




"""
2
3
Fred Barney
Barney Betty
Betty Wilma
4
Fred Barney
Betty Wilma
Barney Betty
Betty Betty
"""