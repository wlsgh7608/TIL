"""
https://www.acmicpc.net/problem/11650
좌표 정렬하기 / 실버 5 / 6분
"""
import sys
input = sys.stdin.readline
N = int(input())

plane = []
for _ in range(N):
    x,y = map(int,input().split())
    plane.append((x,y))
plane.sort(key = lambda x : (x[0],x[1]))
for x,y in plane:
    print(x,y)
