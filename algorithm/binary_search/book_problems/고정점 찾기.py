import sys

input = sys.stdin.readline

n = int(input())
lists = list(map(int,input().split()))

def check():
    lo,hi = 0,n-1
    while lo<=hi:
        m = (lo+hi)//2
        if lists[m] == m:
            return m
        # 인덱스보다 작은 경우
        elif lists[m] < m: 
            lo = m +1
        # 인덱스보다 큰 경우
        elif lists[m] > m: 
            hi = m-1
    return -1

print(check())

"""
input 
5
-15 -6 1 3 7

output 
3

input 
7
-15 -4 2 8 9 13 15

output
2

input
7
-15 -4 3 8 9 13 15

output
-1

input
5
-1 0 1 2 4 

5
-1 0 2 1 3 

16
0 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
16
-4 0 1 2 3 4 5 6 7 8 9 10 11 12 13 15
"""