"""
https://www.acmicpc.net/problem/9372
상근이의 여행 / 실버 3 / 3분
09:15 ~ 09:17
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V,E= map(int,input().split())
    for _ in range(E):
        a,b = map(int,input().split())
    print(V-1)

