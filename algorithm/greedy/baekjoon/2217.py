import sys
input = sys.stdin.readline
N = int(input())
from collections import deque

ropes  = [int(input()) for _ in range(N)]

ropes.sort()
ropes = deque(ropes)
max_weight = 0
while ropes:
    size = len(ropes)
    min_rope = ropes.popleft()
    max_weight = max(max_weight,min_rope*size)
print(max_weight)