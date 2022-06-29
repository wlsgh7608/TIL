"""
https://www.acmicpc.net/problem/10816
숫자카드 2 / 실버 4 / 75분
20:42 ~ 21:55
"""
import sys
input = sys.stdin.readline

def lower_check(L,target):
    s,e = 0, len(L)
    while s<e:
        m = (s+e)//2
        if L[m] < target:
            s = m+1
        else:
            e = m
    return e

def upper_check(L,target):
    s,e = 0, len(L)
    while s<e:
        m = (s+e)//2
        if L[m] <= target:
            s = m+1
        else:
            e= m
    return e

N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
targets  = list(map(int,input().split()))
numbers.sort()

result = []
for t in targets:
    up = upper_check(numbers,t)
    down = lower_check(numbers,t)
    print(up-down,end = " ")
