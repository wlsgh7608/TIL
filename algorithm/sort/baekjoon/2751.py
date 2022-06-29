"""
https://www.acmicpc.net/problem/2751
수 정렬하기 2 / 실버 5 / 3분
"""
import sys
input = sys.stdin.readline
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# 내부 sort 이용(tim sort)
numbers.sort()
for i in numbers:
    print(i)