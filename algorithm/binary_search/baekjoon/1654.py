"""
https://www.acmicpc.net/problem/1654
랜선 자르기 / 실버 3 / 15분
22:00 ~ 22:15
"""
import sys
input = sys.stdin.readline
K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]
lines.sort()

s,e = 1,lines[-1]
ans = s
while s<=e:
    m = (s+e)//2
    numbers = [line//m for line in lines]
    if sum(numbers)>=N:
        ans = m
        s=m+1
    else:
        e= m-1
print(ans)
